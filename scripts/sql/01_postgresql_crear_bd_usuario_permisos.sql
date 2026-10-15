-- PostgreSQL 14+; ejecutar con un usuario administrador (por ejemplo postgres):
-- psql -U postgres -h localhost -f scripts/sql/01_postgresql_crear_bd_usuario_permisos.sql
-- IMPORTANTE: reemplazar REEMPLAZAR_CON_PASSWORD_SEGURA por una contraseña real
-- y colocar esa MISMA contraseña en DB_PASSWORD del archivo .env.
-- Ejecutar sin -1 / --single-transaction: CREATE DATABASE requiere autocommit.
CREATE USER gestor_tareas_user WITH LOGIN PASSWORD 'REEMPLAZAR_CON_PASSWORD_SEGURA';
CREATE DATABASE gestor_tareas_db OWNER gestor_tareas_user ENCODING 'UTF8';
GRANT ALL PRIVILEGES ON DATABASE gestor_tareas_db TO gestor_tareas_user;
-- El usuario es dueño de la nueva base; Django creará las tablas al ejecutar migrate.
-- Ejecutar solo una vez; una segunda ejecución puede fallar por objetos existentes.
