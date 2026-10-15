# Rúbrica Evaluación N.º 2 — checklist de implementación

La rúbrica contiene **15 subcriterios** en 6 criterios, con niveles 0, 1, 2 y 3. Este checklist muestra dónde está implementado cada aspecto, sin afirmar que el docente lo haya evaluado ni que la ejecución local del estudiante ya esté verificada.

| Subcriterio rúbrica | Archivo / verificación |
|---|---|
| 1.1 Ambiente virtual | README: `py -m venv .venv`, activar entorno |
| 1.2 Aplicación Django y settings/urls | `tasks/apps.py`, `config/settings.py`, `config/urls.py` |
| 1.3 Aplicación particular | `tasks/`, interfaz y CRUD web |
| 2.1 Modelo de datos | `tasks/models.py` (`Task`, elecciones, validadores) |
| 2.2 Registro de modelos | `tasks/admin.py` (`@admin.register(Task)`) |
| 2.3 Migraciones creadas/aplicadas | `tasks/migrations/0001_initial.py`; comprobar `python manage.py migrate`, `showmigrations` |
| 3.1 Instalación REST Framework | `requirements.txt`: `djangorestframework`; comprobar con pip |
| 3.2 Configuración REST Framework | `config/settings.py`: `rest_framework` y `REST_FRAMEWORK` |
| 4.1 Serialización modelo | `tasks/api/serializers.py`: `TaskSerializer` |
| 4.2 ModelViewSet | `tasks/api/views.py`: `TaskViewSet` |
| 4.3 URLs para vistas | `tasks/api/urls.py`: `DefaultRouter` |
| 4.4 Integración URLs con Django | `config/urls.py`: `path('api/', include(...))` |
| 5.1 Proyecto inicia/URLs accesibles | `python manage.py check`, `migrate`, `runserver`; navegación web/API |
| 5.2 CRUD completo | `tasks/tests.py`, `docs/API.md`, pruebas manuales GET/POST/PUT/PATCH/DELETE |
| 6. Control de versiones en nube | `.gitignore`, historial local incluido y `docs/GITHUB.md` para subir el repo a GitHub |

## Requerimientos explícitos de la pauta, además de la rúbrica

| Exigencia adicional | Evidencia / archivo |
|---|---|
| Scripts SQL: crear BD/usuario/permisos | `scripts/sql/01_postgresql...sql`, `scripts/sql/02_mariadb...sql` |
| `.env` para conexión y `SECRET_KEY` | `.env` local, `.env.example`, `config/settings.py` |
| Historial de commits en GitHub | Requiere configurar remoto y realizar `git push`; **no se puede completar sin tu cuenta/repositorio** |
| Evidencia de modelo, migraciones y funcionamiento | `docs/EVIDENCIAS.md` explica qué capturar en tu PC |
| Defensa individual | `docs/DEFENSA.md` |
| Estructura mínima | app, serializers, views, URLs, SQL, requirements y README incluidos |

**Nota:** la pauta no establece cuál motor SQL usar ni pide relaciones adicionales al modelo original. Por eso se conserva el modelo `Task` del diseño original, sin inventar entidades ajenas a la asignación.
