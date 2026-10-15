"""Pruebas de la Evaluación 2: modelo, web y CRUD API completo."""
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task


def new_task(**overrides):
    values = {
        "name": "Preparar evaluación", "priority": "Alta",
        "hours": Decimal("3.00"), "completed": False,
    }
    values.update(overrides)
    return Task.objects.create(**values)


class TaskModelTests(TestCase):
    def test_creacion_y_propiedades(self):
        task = new_task()
        self.assertIsNotNone(task.pk)
        self.assertEqual(str(task), "Preparar evaluación")
        self.assertEqual(task.status, "Pendiente")
        self.assertEqual(task.workload, "Carga media")
        self.assertEqual(task.priority_message, "Requiere atención prioritaria.")

    def test_clasificacion_segun_horas(self):
        task = new_task(hours=Decimal("1.00"))
        self.assertEqual(task.workload, "Carga baja")
        task.hours = Decimal("4.00")
        self.assertEqual(task.workload, "Carga media")
        task.hours = Decimal("4.01")
        self.assertEqual(task.workload, "Carga alta")

    def test_no_acepta_horas_negativas_en_validacion(self):
        task = Task(name="Inválida", priority="Media", hours=Decimal("-1.00"))
        with self.assertRaises(ValidationError):
            task.full_clean()

    def test_persiste_en_base_de_datos(self):
        task = new_task()
        other = Task.objects.get(pk=task.pk)
        self.assertEqual(other.name, task.name)
        self.assertEqual(other.hours, Decimal("3.00"))


class TaskWebTests(TestCase):
    def test_inicio_sin_registros(self):
        response = self.client.get(reverse("task_manager"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aún no hay tareas registradas")
        self.assertEqual(response.context["total_tasks"], 0)

    def test_formulario_crea_y_muestra_estadisticas(self):
        response = self.client.post(reverse("task_manager"), {
            "name": " Repasar Django ", "priority": "Media",
            "hours": "2.50", "completed": "on",
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().name, "Repasar Django")
        self.assertEqual(response.context["completed_tasks"], 1)
        self.assertEqual(response.context["completion_percentage"], 100)
        self.assertContains(response, "Resultado de la tarea guardada")

    def test_web_no_acepta_formulario_invalido(self):
        response = self.client.post(reverse("task_manager"), {
            "name": " ", "priority": "Alta", "hours": "-2",
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.count(), 0)
        self.assertTrue(response.context["form"].errors)

    def test_web_edita_tarea(self):
        task = new_task()
        url = reverse("task_edit", args=[task.pk])
        self.assertEqual(self.client.get(url).status_code, 200)
        response = self.client.post(url, {
            "name": "Tarea actualizada", "priority": "Baja",
            "hours": "5", "completed": "on",
        })
        self.assertRedirects(response, reverse("task_manager"))
        task.refresh_from_db()
        self.assertEqual(task.name, "Tarea actualizada")
        self.assertTrue(task.completed)

    def test_web_elimina_solo_con_post(self):
        task = new_task()
        url = reverse("task_delete", args=[task.pk])
        self.assertEqual(self.client.get(url).status_code, 405)
        self.assertTrue(Task.objects.filter(pk=task.pk).exists())
        self.assertRedirects(self.client.post(url), reverse("task_manager"))
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())

    def test_paginas_auxiliares_y_404(self):
        self.assertEqual(self.client.get(reverse("about")).status_code, 200)
        self.assertEqual(self.client.get("/ruta-inexistente/").status_code, 404)


class TaskAPITests(APITestCase):
    def setUp(self):
        self.list_url = reverse("task-list")

    def test_api_root_y_listado_vacio(self):
        self.assertEqual(self.client.get("/api/").status_code, 200)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_creacion_get_list_y_get_detail(self):
        response = self.client.post(self.list_url, {
            "name": "Prueba API", "priority": "Alta",
            "hours": "1.50", "completed": False,
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        pk = response.data["id"]
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(response.data["hours"], "1.50")
        self.assertIn("created_at", response.data)
        self.assertEqual(self.client.get(self.list_url).data[0]["id"], pk)
        detail = self.client.get(reverse("task-detail", args=[pk]))
        self.assertEqual(detail.status_code, status.HTTP_200_OK)
        self.assertEqual(detail.data["name"], "Prueba API")

    def test_put_reemplaza_campos_y_patch_actualiza_parcial(self):
        task = new_task()
        url = reverse("task-detail", args=[task.pk])
        response = self.client.put(url, {
            "name": "Editar por PUT", "priority": "Media",
            "hours": "4.00", "completed": True,
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertTrue(task.completed)
        response = self.client.patch(url, {"priority": "Baja"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.priority, "Baja")
        self.assertEqual(task.name, "Editar por PUT")

    def test_delete(self):
        task = new_task()
        url = reverse("task-detail", args=[task.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)

    def test_rechaza_datos_invalidos(self):
        for payload in (
            {"name": "", "priority": "Alta", "hours": "1"},
            {"name": "Ejemplo", "priority": "Urgente", "hours": "1"},
            {"name": "Ejemplo", "priority": "Media", "hours": "-1"},
            {"name": "Ejemplo", "priority": "Media", "hours": "99999.99"},
        ):
            with self.subTest(payload=payload):
                response = self.client.post(self.list_url, payload, format="json")
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 0)

    def test_método_no_permitido(self):
        self.assertEqual(self.client.put(self.list_url, {}, format="json").status_code, 405)
