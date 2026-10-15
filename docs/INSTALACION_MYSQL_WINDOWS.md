# Instalación y ejecución en Windows — MySQL 8.4 LTS

Esta guía forma parte de la **Evaluación N.º 2**. El proyecto está programado; la instalación del servidor MySQL, las contraseñas personales, las pruebas locales y el push requieren acciones en tu computadora.

## 1. Instalar servidor y administración

1. Descarga **MySQL Community Server 8.4 LTS**, el paquete **MSI para Windows** desde <https://dev.mysql.com/downloads/mysql/8.4.html>. En MySQL 8.4 se instala y configura por medio de **MySQL Configurator** (no depende del antiguo instalador 8.0).
2. Sigue el asistente y configura: servidor local, puerto TCP/IP `3306`, clave para `root` (guárdala en privado), e inicio del servicio con Windows.
3. Instala **MySQL Workbench 8.0** por separado desde <https://dev.mysql.com/downloads/workbench/>. Aunque Workbench puede conectarse a 8.4, ciertas funciones de administración están enfocadas en servidor 8.0; para la evaluación usaremos **editor SQL** y consultas.
4. Abre Workbench y crea la conexión `MySQL local`: host `127.0.0.1`, puerto `3306`, usuario `root`. Prueba la conexión.

> Si ya tienes MySQL instalado y operativo, no lo reinstales. Comprueba primero `SELECT VERSION();`.

## 2. Crear la base, usuario y permisos (en MySQL Workbench)

Abre una pestaña SQL conectada como `root`. Ejecuta **en orden** el contenido de estos archivos desde `File > Open SQL Script` y el botón del rayo:

1. `scripts/sql/01_mysql_crear_base_datos.sql` — `CREATE DATABASE`.
2. `scripts/sql/02_mysql_crear_usuario.sql` — `CREATE USER` y `ALTER USER`. **Antes de ejecutar**, sustituye las DOS apariciones de `REEMPLAZAR_CON_CONTRASENA_SEGURA` en el editor por una contraseña local de tu elección (no uses comilla simple). **No guardes el archivo con la contraseña real**.
3. `scripts/sql/03_mysql_asignar_permisos.sql` — otorga permisos a la BD `gestor_tareas_db` y a la temporal `test_gestor_tareas_db` usada por las pruebas automatizadas.

Usa una contraseña distinta a la de root para el usuario `gestor_tareas_user`.

Comprueba con `SHOW DATABASES;` y `SHOW GRANTS FOR 'gestor_tareas_user'@'127.0.0.1';` (también hay consultas en `04_mysql_consultas_evidencia.sql`).

> Si has modificado la contraseña del script y se guardó por error en Git, **restaura el marcador** antes del commit; si se publicó una contraseña real, cámbiala inmediatamente.

## 3. Crear entorno Python

Extrae el ZIP. Abre PowerShell en la carpeta que contiene **`manage.py`**, por ejemplo:

```powershell
cd "$HOME\Desktop\gestor_tareas_django"
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Requiere Python **3.12 o 3.13** de 64 bits instalado previamente. Si `py -3.12` no existe y tienes Python 3.13, usa `py -3.13`. Si hay bloqueo al activar scripts en PowerShell, puedes usar `.\.venv\Scripts\python.exe` en lugar de `python`, o `Set-ExecutionPolicy -Scope Process Bypass` solo para esa terminal.

## 4. Completar el archivo privado `.env`

El ZIP incluye un `.env` LOCAL con una `DJANGO_SECRET_KEY` aleatoria de desarrollo, pero la contraseña de MySQL está deliberadamente como marcador. Ábrelo en un editor de texto y reemplaza:

```ini
DB_ENGINE=mysql
DB_NAME=gestor_tareas_db
DB_USER=gestor_tareas_user
DB_PASSWORD=LA_MISMA_CONTRASENA_QUE_USASTE_EN_WORKBENCH
DB_HOST=127.0.0.1
DB_PORT=3306
DB_TEST_NAME=test_gestor_tareas_db
```

No copies el archivo `.env` a GitHub; solo debes publicar la plantilla `.env.example` sin credenciales.

## 5. Aplicar migraciones y comprobar funcionamiento

Desde la terminal, dentro del entorno virtual:

```powershell
python manage.py check --database default
python manage.py makemigrations --check --dry-run
python manage.py migrate
python manage.py showmigrations tasks
python manage.py test -v 2
python manage.py runserver
```

Los tests crean **temporalmente** `test_gestor_tareas_db` y luego la eliminan; no destruyen la base principal. Verifica:

- Interfaz web: <http://127.0.0.1:8000/>
- API REST: <http://127.0.0.1:8000/api/>
- CRUD de tareas: <http://127.0.0.1:8000/api/tasks/>
- Django Admin: <http://127.0.0.1:8000/admin/> (opcional crear admin con `python manage.py createsuperuser`)

En Workbench, ejecuta `scripts/sql/04_mysql_consultas_evidencia.sql` para confirmar que `tasks_task` se ha creado y contiene los registros guardados desde Django. En API sigue `docs/API.md` para verificar GET/POST/PUT/PATCH/DELETE.

## 6. Problemas frecuentes

- **`ModuleNotFoundError: No module named 'MySQLdb'`:** faltó instalar `mysqlclient`, verifica entorno activo y `python -m pip install -r requirements.txt`.
- **`Access denied for user` (1045):** password, host y cuenta `'gestor_tareas_user'@'127.0.0.1'` deben coincidir. En Windows `localhost` puede comportarse distinto; usa **127.0.0.1** para conexión TCP/IP.
- **`Can't connect to MySQL server` (2003):** revisa servicio MySQL, puerto 3306 y MySQL Configurator.
- **`Unknown database 'gestor_tareas_db'`:** falta ejecutar script 01.
- **`Access denied ... test_gestor_tareas_db`:** falta ejecutar script 03 para el esquema temporal de las pruebas.
- **`ModuleNotFoundError: No module named 'django'`:** activa `.venv` e instala dependencias.
- **`.env` no encontrado o `DJANGO_SECRET_KEY` faltante:** usa `.env` del ZIP o copia `.env.example` a `.env` y genera una clave segura en tu PC: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`.

## 7. Evidencias para la pauta

Captura la ejecución exitosa de scripts 01–03, salida de `SHOW GRANTS`, la tabla `tasks_task`, migración `0001_initial [X]`, CRUD REST, resultados de `python manage.py test` y repositorio GitHub. Consulta `docs/EVIDENCIAS.md` y `docs/GITHUB.md`.
