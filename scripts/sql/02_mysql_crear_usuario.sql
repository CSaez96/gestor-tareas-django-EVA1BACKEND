-- MySQL Community Server 8.4 LTS — ejecutar con root.
-- Script 2 de 3: usuario propio para la app.
-- REEMPLAZA 'REEMPLAZAR_CON_CONTRASENA_SEGURA' EN EL EDITOR DE WORKBENCH,
-- EJECUTA SIN GUARDAR LA CONTRASENA REAL EN ESTE ARCHIVO DEL REPOSITORIO.
-- Copia esa misma contrasena a DB_PASSWORD de tu .env LOCAL.
-- ATENCION: ALTER USER cambia la contrasena si el usuario ya existe.
CREATE USER IF NOT EXISTS 'gestor_tareas_user'@'127.0.0.1'
    IDENTIFIED BY 'REEMPLAZAR_CON_CONTRASENA_SEGURA';
ALTER USER 'gestor_tareas_user'@'127.0.0.1'
    IDENTIFIED BY 'REEMPLAZAR_CON_CONTRASENA_SEGURA';
