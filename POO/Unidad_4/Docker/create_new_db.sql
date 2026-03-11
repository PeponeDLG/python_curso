-- create_new_db.sql
CREATE DATABASE IF NOT EXISTS cursosformacion;
GRANT ALL PRIVILEGES ON cursosformacion.* TO 'user'@'%';
FLUSH PRIVILEGES;