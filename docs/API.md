# Guía de uso de la API REST

URL base: `http://127.0.0.1:8000/api/tasks/`. Antes de probar, ejecutar `python manage.py migrate` y `python manage.py runserver`.

## Navegador

Abrir `http://127.0.0.1:8000/api/tasks/`. Django REST Framework habilita la interfaz Browsable API. Permite consultar y registrar tareas con formularios HTTP.

## PowerShell (Windows)

```powershell
$base = 'http://127.0.0.1:8000/api/tasks/'

# GET — Consultar lista
Invoke-RestMethod -Uri $base -Method Get

# POST — Crear
$tarea = Invoke-RestMethod -Uri $base -Method Post -ContentType 'application/json' -Body '{"name":"Estudiar DRF","priority":"Alta","hours":"2.50","completed":false}'
$tarea
$id = $tarea.id

# GET — Detalle
Invoke-RestMethod -Uri "$base$id/" -Method Get

# PUT — Reemplazo completo
Invoke-RestMethod -Uri "$base$id/" -Method Put -ContentType 'application/json' -Body '{"name":"Estudiar API REST","priority":"Media","hours":"3.00","completed":false}'

# PATCH — Actualización parcial
Invoke-RestMethod -Uri "$base$id/" -Method Patch -ContentType 'application/json' -Body '{"completed":true}'

# DELETE — Eliminar
Invoke-RestMethod -Uri "$base$id/" -Method Delete
```

Códigos esperados: GET `200`; POST `201`; PUT/PATCH `200`; DELETE `204`; datos inválidos `400`; ID inexistente `404`; método no soportado `405`.

## Reglas de validación

- `name`: texto no vacío de hasta 100 caracteres (se recortan espacios iniciales/finales).
- `priority`: exactamente `Alta`, `Media` o `Baja`; en POST, si se omite se usa `Media`.
- `hours`: número con hasta 6 dígitos en total, 2 decimales, mayor o igual que cero.
- `completed`: verdadero o falso; en POST es opcional y asume `false`.
- `id`, `created_at`, `updated_at`: campos generados en el servidor, solo lectura.

## Qué hace cada archivo

1. `tasks/models.py`: describe el registro persistido.
2. `tasks/api/serializers.py`: convierte el registro Django a JSON y valida las entradas.
3. `tasks/api/views.py`: `TaskViewSet(ModelViewSet)` implementa las cinco operaciones requeridas.
4. `tasks/api/urls.py`: `DefaultRouter` genera las rutas REST automáticamente.
5. `config/urls.py`: integra el router bajo `/api/`.

**Seguridad:** por requisitos académicos es una API abierta para localhost. No publicar tal como está.
