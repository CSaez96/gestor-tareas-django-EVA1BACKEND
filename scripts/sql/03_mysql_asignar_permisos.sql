-- MySQL Community Server 8.4 LTS — ejecutar con root.
-- Script 3 de 3: permisos solo para la BD de la app y la BD temporal de tests.
-- El permiso sobre test_gestor_tareas_db permite que Django cree y elimine
-- esa base temporal al ejecutar `python manage.py test`.
GRANT ALL PRIVILEGES ON `gestor_tareas_db`.*
    TO 'gestor_tareas_user'@'127.0.0.1';
GRANT ALL PRIVILEGES ON `test_gestor_tareas_db`.*
    TO 'gestor_tareas_user'@'127.0.0.1';
-- GRANT se aplica inmediatamente en MySQL 8.4; FLUSH PRIVILEGES no es necesario.
