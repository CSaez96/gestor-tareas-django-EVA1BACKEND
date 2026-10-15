# Gestor de Tareas — Evaluación N.º 2 de Backend

**Asignatura:** Programación Backend · **Docente:** Erick Bailey Rebolledo  
**Estudiante:** Christian Ignacio Sáez Sáez · **Modalidad:** individual

## Qué se entrega

Continuación del proyecto de Evaluación 1: conserva interfaz web, formulario, prioridades, cálculo de carga, estadísticas y página 404. La Evaluación 2 incorpora un modelo **Task** persistente, migración, Django REST Framework, `ModelSerializer`, `ModelViewSet`, `DefaultRouter` y CRUD completo con GET / POST / PUT / PATCH / DELETE, además de base de datos parametrizable, scripts SQL, pruebas y Git.

**Base de datos:** SQLite para probar en cualquier PC; PostgreSQL o MariaDB para demostrar los scripts de creación de base de datos, usuario y permisos pedidos en la pauta. No se ha impuesto un motor que la pauta no especifica. Puedes elegir PostgreSQL o MariaDB antes de generar las evidencias finales.

## 1. Inicio rápido en Windows / PowerShell

Requisitos: Python 3.10 o superior, Git; para PostgreSQL/MariaDB necesitas instalar el servidor correspondiente.

```powershell
cd ruta\a\gestor_tareas_django
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
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

Abrir **http://127.0.0.1:8000/** (interfaz), **http://127.0.0.1:8000/api/** (API), **http://127.0.0.1:8000/api/tasks/** (CRUD REST).

Si PowerShell impide activar el entorno, puedes ejecutar directamente `.\.venv\Scripts\python.exe` en los comandos o cambiar la política solo para la sesión: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.

En macOS o Linux: `python3 -m venv .venv`, `source .venv/bin/activate` y continúa con los comandos `python`.

## 2. Usar una base SQL con usuario y permisos

**Importante:** el motor SQL requiere un servicio instalado y configurado. Los scripts del proyecto están **listos para ejecutar**, pero sus contraseñas son intencionalmente marcadores que debes reemplazar. Ninguna contraseña real va en GitHub.

### Opción A — PostgreSQL (recomendada)

1. Instala PostgreSQL y verifica que esté iniciado.
2. Edita `scripts/sql/01_postgresql_crear_bd_usuario_permisos.sql`: reemplaza `REEMPLAZAR_CON_PASSWORD_SEGURA` por tu contraseña local segura. Usa una contraseña sin comillas simples para este script, o escápalas según SQL.
3. Abre una terminal en la carpeta raíz y ejecuta (administrador PostgreSQL):
   ```powershell
   psql -U postgres -h localhost -f scripts/sql/01_postgresql_crear_bd_usuario_permisos.sql
   ```
4. Sustituye `.env` por una copia de `.env.postgresql.example` y cambia `DJANGO_SECRET_KEY` y `DB_PASSWORD`. El usuario y el nombre de base deben coincidir con el script. Si el puerto o el host son otros, ajústalos.
5. Instala `requirements.txt`, ejecuta `python manage.py migrate` y `python manage.py test -v 2`.

El script crea la base `gestor_tareas_db`, el usuario `gestor_tareas_user`, asigna la propiedad de la base y otorga permisos. Se ejecuta solo una vez. Las tablas se crean **con migraciones Django**, no manualmente.

### Opción B — MariaDB / MySQL

1. Instala e inicia MariaDB o MySQL.
2. Edita `scripts/sql/02_mariadb_crear_bd_usuario_permisos.sql` y reemplaza el marcador de contraseña.
3. Ejecuta como administrador:
   ```powershell
   mysql -u root -p
   ```
   Dentro de MySQL, ejecuta `SOURCE ruta/absoluta/al/proyecto/scripts/sql/02_mariadb_crear_bd_usuario_permisos.sql;` (usa barras `/`, sin espacios en la ruta o con ruta apropiadamente entre comillas según tu cliente).
4. `Copy-Item .env.mariadb.example .env -Force` y reemplaza clave Django y contraseña de BD.
5. `pip install -r requirements-mariadb.txt`, `python manage.py migrate`, `python manage.py test -v 2`.

> MariaDB/MySQL utilizan el paquete `mysqlclient`; en algunos Windows se necesitan herramientas de compilación o un wheel compatible. Si la instalación falla, PostgreSQL es una alternativa respaldada por `requirements.txt`.

**Nota:** SQLite no admite el mismo modelo de `CREATE USER`/`GRANT` por tratarse de una BD basada en archivo. Para evidenciar los scripts SQL requeridos por la pauta, demuestra PostgreSQL o MariaDB además de las pruebas locales.

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
