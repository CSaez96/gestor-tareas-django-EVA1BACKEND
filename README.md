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

> Esta primera versión no utiliza modelos, migraciones, CRUD ni persistencia de datos, de acuerdo con el alcance de la evaluación.

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
git clone https://github.com/TU-USUARIO/gestor-tareas-django.git
cd gestor-tareas-django
```

Crear el ambiente virtual:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

> El ZIP trae un archivo `.env` configurado para pruebas **locales con SQLite** y una clave Django aleatoria de desarrollo. **No lo publiques ni lo subas a GitHub**. Si descargas el proyecto desde GitHub en vez del ZIP, crea tu propio `.env`: `Copy-Item .env.example .env` y reemplaza `DJANGO_SECRET_KEY` por una clave aleatoria segura.
>
> Para generar una clave: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`.

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py migrate
python manage.py test -v 2
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

Las tareas se mantienen en memoria durante la ejecución del servidor. No existe persistencia en base de datos en esta evaluación.

## Paquete externo

Se utiliza `django-widget-tweaks` para personalizar los campos del formulario desde la plantilla mediante la etiqueta `render_field`. Esto permite aplicar atributos HTML sin duplicar la definición de los campos en la plantilla.

## Autor

<<<<<<< HEAD
Nombre del estudiante
=======
## 3. Archivos y estructura

```text
config/
  settings.py                 # dotenv, bases de datos, DRF, apps
  urls.py                     # /admin/, /api/, /, /api-auth/
tasks/
  models.py                   # Task y validadores
  migrations/0001_initial.py # Creación del modelo y restricción de horas
  admin.py                    # Registro y búsqueda en Django Admin
  forms.py                    # ModelForm web
  views.py                    # Interfaz web con persistencia
  urls.py                     # Rutas web
  api/serializers.py          # TaskSerializer
  api/views.py                # TaskViewSet
  api/urls.py                 # DefaultRouter
  tests.py                    # Tests modelos, web y API
scripts/sql/                   # Scripts CREATE DATABASE / USER / GRANT
templates/                     # Interfaz conservada y extendida
docs/                          # API, defensa, rúbrica, GitHub y evidencias
.env.example / .env.*.example # Plantillas públicas sin secretos
.env                           # Solo LOCAL: excluido por .gitignore
requirements.txt
requirements-mariadb.txt
```

## 4. Endpoints CRUD

| Operación | HTTP | Endpoint | Descripción |
|---|---|---|---|
| Listar | GET | `/api/tasks/` | Lista las tareas |
| Detalle | GET | `/api/tasks/1/` | Consulta una tarea |
| Crear | POST | `/api/tasks/` | Guarda un registro |
| Reemplazar | PUT | `/api/tasks/1/` | Actualiza todos los campos editables |
| Actualización parcial | PATCH | `/api/tasks/1/` | Modifica solo campos enviados |
| Eliminar | DELETE | `/api/tasks/1/` | Elimina el registro |

Ejemplo JSON de POST:

```json
{"name": "Preparar evaluación", "priority": "Alta", "hours": "3.00", "completed": false}
```

Campos de respuesta: `id`, `name`, `priority`, `hours`, `completed`, `created_at`, `updated_at`. `id`, fechas y horas de actualización son de solo lectura; las prioridades aceptadas son `Alta`, `Media` y `Baja`; `hours` es numérica, no negativa y con dos decimales. En POST, `name` y `hours` son obligatorios; `priority` es opcional (predeterminada `Media`) y `completed` es opcional (predeterminada `false`). Más ejemplos en [`docs/API.md`](docs/API.md).

La interfaz web permite crear/consultar/editar/eliminar en `/`, y Django Admin permite gestionar tareas mediante `/admin/` (para usarlo ejecutar `python manage.py createsuperuser`).

## 5. Evidencias, rúbrica y defensa

- `docs/EVIDENCIAS.md`: lista de qué mostrar o fotografiar, sin inventar resultados.
- `docs/RUBRICA_CHECKLIST.md`: relación de cada subcriterio con su implementación.
- `docs/DEFENSA.md`: cinco preguntas con respuestas preparatorias para la defensa individual.
- `docs/GITHUB.md`: cómo subir el proyecto sin filtrar `.env` y preservando el historial del repositorio previo.
- `scripts/VERIFICAR_WINDOWS.ps1`: comandos para comprobar configuración, migraciones y pruebas.

## 6. Advertencias y alcance

La pauta solicita una API CRUD, pero no especifica autenticación. Por ello las rutas API usan `AllowAny` para **demostración local**. **No exponer este servidor a Internet ni utilizarlo en producción** sin autenticación, autorizaciones, HTTPS, secretos seguros y `DEBUG=False`.

El ZIP se prepara con una estructura Git local que parte del ZIP recibido y agrega cambios de la evaluación 2; este historial reconstruido **no sustituye los commits ni el repositorio GitHub original**. El proyecto aún debe ejecutarse en tu computador con sus dependencias y con la base elegida para generar evidencias verificables.
>>>>>>> be88511 (Evaluación 2: precisión de contrato API y estado honesto de verificación)
