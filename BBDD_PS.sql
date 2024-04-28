-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS django_tfg_ps_db;
USE django_tfg_ps_db;

-- Crear la tabla de jugadores
CREATE TABLE IF NOT EXISTS Jugadores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNIQUE,
    dinero INT DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES auth_user(id)
);

-- Crear la tabla de objetos
CREATE TABLE IF NOT EXISTS Objetos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT,
    precio INT NOT NULL,
    tipo_objeto ENUM('Arma', 'Municion', 'Curacion', 'Armadura', 'Skin'),
    imagen MEDIUMBLOB,
    extension VARCHAR(4)
);

-- Crear la tabla de inventario
CREATE TABLE IF NOT EXISTS Inventario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jugador_id INT,
    objeto_id INT,
    cantidad INT,
    FOREIGN KEY (jugador_id) REFERENCES Jugadores(id),
    FOREIGN KEY (objeto_id) REFERENCES Objetos(id),
    UNIQUE (jugador_id, objeto_id)
);

/*
EJEMPLO DE DATOS

-- Insertar datos de jugadores
INSERT INTO Jugadores (user_id, dinero) VALUES
(1, 1000),
(2, 800),
(3, 600),
(4, 1200),
(5, 1500);

-- Insertar datos de objetos
INSERT INTO Objetos (nombre, descripcion, precio, tipo_objeto, imagen, extension) VALUES
('Cuchillo', 'Un cuchillo afilado, ideal para combates cuerpo a cuerpo.', 50, 'Arma', NULL, ''),
('Pistola Samurai Edge', 'La icónica pistola de S.T.A.R.S., modelo Samurai Edge.', 150, 'Arma', NULL, ''),
('Escopeta M37', 'Una poderosa escopeta de doble cañón, ideal para enfrentarse a hordas de enemigos.', 200, 'Arma', NULL, ''),
('Granada de Fragmentación', 'Una granada explosiva que causa daño en un área determinada.', 80, 'Municion', NULL, ''),
('Spray Medicinal', 'Un spray medicinal que restaura una cantidad moderada de salud.', 30, 'Curacion', NULL, ''),
('Chaleco Táctico', 'Un chaleco táctico que proporciona una protección moderada.', 100, 'Armadura', NULL, ''),
('Traje de Kevlar', 'Un traje de kevlar que proporciona una protección excepcional.', 200, 'Armadura', NULL, ''),
('Poción Verde', 'Una poción verde que restaura una gran cantidad de salud.', 150, 'Curacion', NULL, ''),
('Poción Roja', 'Una poción roja que otorga temporalmente invencibilidad al jugador.', 250, 'Curacion', NULL, ''),
('Spray de Primeros Auxilios', 'Un spray de primeros auxilios que restaura completamente la salud.', 300, 'Curacion', NULL, ''),
('Munición de 9mm', 'Munición estándar para la pistola.', 10, 'Municion', NULL, ''),
('Munición de Escopeta', 'Munición de escopeta de calibre 12.', 15, 'Municion', NULL, ''),
('Munición de Granada', 'Munición especial para granadas.', 5, 'Municion', NULL, ''),
('Munición de Cuchillo', 'Afilar el cuchillo', 10, 'Municion', NULL, ''),
('Botiquín de Primeros Auxilios', 'Un botiquín básico que restaura una cantidad moderada de salud.', 40, 'Curacion', NULL, ''),
('Botiquín Avanzado', 'Un botiquín avanzado que restaura una cantidad considerable de salud.', 80, 'Curacion', NULL, ''),
('Escudo Anti-Criaturas', 'Un escudo diseñado específicamente para protegerse de las criaturas.', 50, 'Armadura', NULL, ''),
('Granada de Humo', 'Granada de humo para encubrir.', 25, 'Municion', NULL, ''),
('Granada Paralizante', 'Granada paralizante que aturde temporalmente a los enemigos.', 35, 'Municion', NULL, ''),
('Poción de Velocidad', 'Poción que aumenta temporalmente la velocidad del jugador.', 30, 'Curacion', NULL, '');

-- Insertar datos de inventario
INSERT INTO Inventario (jugador_id, objeto_id, cantidad) VALUES
(1, 1, 1), (1, 4, 5), (1, 7, 2), (1, 10, 1),
(2, 2, 1), (2, 5, 3), (2, 8, 1), (2, 11, 3),
(3, 3, 1), (3, 6, 2), (3, 9, 1), (3, 12, 2),
(4, 1, 2), (4, 4, 4), (4, 7, 1), (4, 10, 2),
(5, 2, 2), (5, 5, 4), (5, 8, 2), (5, 11, 4);


INSERT INTO Objetos (nombre, descripcion, precio, tipo_objeto, imagen, extension) VALUES
('Skin de Leon S. Kennedy', 'Una skin que transforma el aspecto del personaje en Leon S. Kennedy, el protagonista de Resident Evil 2.', 800, 'Skin', NULL, NULL),
('Skin de Jill Valentine', 'Una skin que cambia el aspecto del personaje en Jill Valentine, la heroína de Resident Evil 3.', 850, 'Skin', NULL, NULL),
('Skin de Nemesis', 'Una skin que convierte al personaje en Nemesis, la temible criatura de Resident Evil 3.', 1000, 'Skin', NULL, NULL);

*/