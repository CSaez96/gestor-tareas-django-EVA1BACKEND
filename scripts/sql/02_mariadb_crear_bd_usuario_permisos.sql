-- MariaDB / MySQL; ejecutar desde un usuario administrador:
-- mysql -u root -p < scripts/sql/02_mariadb_crear_bd_usuario_permisos.sql
-- IMPORTANTE: cambiar la contraseña aquí y en DB_PASSWORD del archivo .env.
-- Conexión local por 127.0.0.1. Si tu configuración usa otro host, ajusta ambos.
CREATE DATABASE IF NOT EXISTS gestor_tareas_db
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'gestor_tareas_user'@'127.0.0.1'
    IDENTIFIED BY 'REEMPLAZAR_CON_PASSWORD_SEGURA';
GRANT ALL PRIVILEGES ON gestor_tareas_db.*
    TO 'gestor_tareas_user'@'127.0.0.1';
FLUSH PRIVILEGES;
-- Al cambiar contraseñas de usuarios existentes usar ALTER USER explícitamente.
