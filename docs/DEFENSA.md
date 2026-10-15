# Preparación para la defensa individual (5 preguntas)

La pauta indica **cinco preguntas sobre la implementación**. Las siguientes son ejemplos para practicar; las preguntas reales pueden ser distintas.

### 1) ¿Qué cambió respecto de la Evaluación 1?

En la primera evaluación las tareas estaban en una lista de Python (`TASKS`): se perdían al reiniciar el proceso. Ahora cada tarea es una fila persistente en la base de datos mediante el modelo `Task` (`tasks/models.py`), y puede gestionarse desde la interfaz web, Admin o API REST.

### 2) ¿Para qué sirve `makemigrations` y para qué sirve `migrate`?

`makemigrations` genera un archivo de migración al detectar cambios en modelos. `migrate` aplica dichas operaciones sobre la base real. La migración `tasks/migrations/0001_initial.py` crea la tabla y la restricción que prohíbe horas negativas. `python manage.py showmigrations tasks` muestra qué migraciones se aplicaron.

### 3) ¿Qué hacen `ModelSerializer` y `ModelViewSet`?

`TaskSerializer` transforma modelos a JSON y comprueba datos recibidos, incluidos horas y nombre. `TaskViewSet(ModelViewSet)` implementa listado, detalle, creación, actualización total, actualización parcial y eliminación reutilizando la lógica genérica de DRF.

### 4) ¿Qué hace el Router y qué significan GET, POST, PUT, PATCH y DELETE?

`DefaultRouter` construye automáticamente `/api/tasks/` y `/api/tasks/<id>/`. GET consulta; POST crea; PUT sustituye todos los campos editables; PATCH modifica algunos; DELETE elimina. Por ejemplo un POST a `/api/tasks/` con JSON válido responde 201 y devuelve el ID creado.

### 5) ¿Cómo se protege la contraseña de la base y cuál es el rol de GitHub?

Los valores de conexión y `DJANGO_SECRET_KEY` se leen desde `.env` mediante `python-dotenv` y `os.environ`. `.gitignore` evita subir el `.env` real al repositorio. Los archivos `.env.*.example` son plantillas sin credenciales. Los tres scripts SQL para MySQL crean `gestor_tareas_db`, el usuario local y los permisos en la base de aplicación y en la base temporal para tests. GitHub guarda el código y el historial de cambios. La API está abierta solo para pruebas académicas locales: necesitaría autenticación antes de publicar.

## Demostración sugerida en clase

1. Mostrar modelo `Task`, SQL y `.env` **con contraseña y SECRET_KEY ocultas**.
2. `python manage.py showmigrations tasks` para confirmar `0001_initial [X]`.
3. `python manage.py runserver`, abrir `/` y `/api/tasks/`.
4. Crear tarea (POST), listarla (GET), editarla (PUT/PATCH) y borrarla (DELETE).
5. Mostrar `python manage.py test -v 2`, Git commits y el repositorio remoto.
