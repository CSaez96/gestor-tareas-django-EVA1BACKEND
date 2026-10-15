-- Consultas de evidencia. Conectate con root en MySQL Workbench.
SELECT VERSION() AS version_mysql;
SHOW DATABASES LIKE 'gestor_tareas_db';
SHOW GRANTS FOR 'gestor_tareas_user'@'127.0.0.1';
-- Ejecuta la migracion Django antes de consultar las tablas de la app:
USE `gestor_tareas_db`;
SHOW TABLES;
SELECT * FROM `tasks_task`;
