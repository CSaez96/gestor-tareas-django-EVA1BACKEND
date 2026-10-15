# Ejecutar en PowerShell desde la carpeta raíz del proyecto.
# Antes: activar .venv, instalar requirements y configurar .env.
$ErrorActionPreference = 'Stop'
python manage.py check
if ($LASTEXITCODE -ne 0) { throw 'Falló manage.py check' }
python manage.py makemigrations --check --dry-run
if ($LASTEXITCODE -ne 0) { throw 'Las migraciones tienen cambios pendientes' }
python manage.py migrate --noinput
if ($LASTEXITCODE -ne 0) { throw 'Falló migrate' }
python manage.py test -v 2
if ($LASTEXITCODE -ne 0) { throw 'Fallaron los tests' }
Write-Host 'Verificaciones completadas. Inicia el servidor con: python manage.py runserver'
