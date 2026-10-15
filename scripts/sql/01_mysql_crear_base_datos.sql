-- MySQL Community Server 8.4 LTS — ejecutar con conexion administrativa (root).
-- Script 1 de 3: crea la BD en Unicode, tablas se crean con Django migrate.
CREATE DATABASE IF NOT EXISTS `gestor_tareas_db`
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_0900_ai_ci;
