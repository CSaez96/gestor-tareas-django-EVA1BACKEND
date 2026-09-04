# Gestor de Tareas - Backend con Python y Django

## Descripción

Aplicación web sencilla desarrollada con Python y Django para la Evaluación 1 de Backend.

El proyecto demuestra:

- Uso de variables y tipos de datos de Python.
- Asignaciones y operaciones.
- Operadores de comparación y lógicos.
- Estructuras de control `if`, `elif`, `else` y `for`.
- Integración de lógica Python dentro de una vista Django.
- Rutas propias.
- Página de bienvenida.
- Página personalizada de error 404.
- Uso de un paquete externo: `django-widget-tweaks` para personalizar campos del formulario.

## Tecnologías

- Python 3
- Django
- django-widget-tweaks
- Git
- GitHub

## Requisitos

- Python 3 instalado.
- Git instalado.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/CSaez96/gestor-tareas-django-EVA1BACKEND
cd gestor-tareas-django
```

Crear el ambiente virtual:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Verificación

```bash
python manage.py check
```

## Ejecución

```bash
python manage.py runserver
```

Abrir:

http://127.0.0.1:8000/

## Rutas

- `/` — gestor de tareas.
- `/about/` — información del proyecto.
- Cualquier ruta inexistente — página 404 personalizada.

## Funcionamiento

La aplicación permite ingresar una tarea, seleccionar su prioridad, indicar horas estimadas y si está completada.

La vista procesa los datos y determina:

- Estado de la tarea.
- Nivel de prioridad.
- Clasificación según horas estimadas.
- Mensaje de resultado.

## Paquete externo

Se utiliza `django-widget-tweaks` para personalizar los campos del formulario desde la plantilla mediante la etiqueta `render_field`. Esto permite aplicar atributos HTML sin duplicar la definición de los campos en la plantilla.
