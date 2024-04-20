CREATE DATABASE IF NOT EXISTS django_tfg_ps_db;

USE django_tfg_ps_db;

-- tabla de jugadores
CREATE TABLE IF NOT EXISTS Jugadores (
    id INT AUTO_INCREMENT PRIMARY KEY
);

-- tabla de objetos
CREATE TABLE IF NOT EXISTS Objetos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT,
    precio INT NOT NULL,
    tipo_objeto ENUM('Arma', 'Municion', 'Curacion', 'Armadura', 'Skin'),
    imagen MEDIUMBLOB
);

-- tabla de inventario
CREATE TABLE IF NOT EXISTS Inventario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jugador_id INT,
    objeto_id INT,
    cantidad INT,
    FOREIGN KEY (jugador_id) REFERENCES Jugadores(id),
    FOREIGN KEY (objeto_id) REFERENCES Objetos(id),
    UNIQUE (jugador_id, objeto_id)
);


