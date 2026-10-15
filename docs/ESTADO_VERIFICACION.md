# Estado real de verificación (preparación del paquete)

Esta hoja separa lo implementado de lo que **debes comprobar en tu equipo** antes de la entrega.

## Comprobaciones realizadas al preparar el ZIP

- Revisión del proyecto original de Evaluación 1: 21 archivos de base.
- Elaboración de modelo, migración, configuraciones, serializers, vistas, router, CRUD web y scripts SQL.
- Verificación sintáctica con Python `compileall` para todos los módulos: **correcta**.
- Análisis sintáctico del código Python y presencia de archivos obligatorios: **correctos**.
- Historial Git local reconstruido con commits diferenciados; `.env` **ignorado** por Git.
- Se configuró MySQL 8.4 LTS como opción principal, `mysqlclient` en requisitos y una base temporal con permisos para ejecutar tests.
- Se corrigieron los documentos y los scripts SQL específicos para MySQL.

## Pendiente de comprobar / no fingir evidencias

- La instalación de Django y DRF **no pudo ejecutarse en el entorno de preparación** porque no había conexión al índice de paquetes; por ello **no se han ejecutado** `manage.py check`, `migrate`, `test` ni el servidor aquí.
- No se ha instalado ni iniciado MySQL 8.4 en el PC del estudiante ni se han ejecutado scripts SQL contra un servidor real; la contraseña privada debe fijarse localmente.
- No se ha publicado un repositorio en GitHub: necesitas tu cuenta o enlazar el repositorio existente.
- No se han generado capturas de pantalla simuladas. Se deben capturar resultados reales tras ejecutar los pasos de `docs/EVIDENCIAS.md`.

## Comandos finales que faltan en tu PC

```powershell
python -m pip install -r requirements.txt
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py migrate
python manage.py showmigrations tasks
python manage.py test -v 2
python manage.py runserver
```

Antes ejecutar scripts SQL 01 a 03 con Workbench y completar DB_PASSWORD en .env; después ejecutar una secuencia manual GET/POST/PUT/PATCH/DELETE en `/api/tasks/`, ejecutar scripts SQL y hacer push a GitHub. Si un comando falla, revisar el error antes de declararlo completo.
