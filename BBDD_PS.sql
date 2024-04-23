CREATE DATABASE IF NOT EXISTS django_tfg_ps_db;

USE django_tfg_ps_db;

-- tabla de jugadores
CREATE TABLE IF NOT EXISTS Jugadores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dinero INT DEFAULT 0
);


-- tabla de objetos
CREATE TABLE IF NOT EXISTS Objetos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT,
    precio INT NOT NULL,
    tipo_objeto ENUM('Arma', 'Municion', 'Curacion', 'Armadura', 'Skin'),
    imagen MEDIUMBLOB,
    extension VARCHAR(4)
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




/*Ejemplo datos introducidos en la BBDD

INSERT INTO Jugadores (id) VALUES
(1),
(2),
(3),
(4),
(5);

INSERT INTO Objetos (nombre, descripcion, precio, tipo_objeto, imagen) VALUES
('Pistola Samurai Edge', 'Una pistola de mano personalizada utilizada por los miembros de S.T.A.R.S.', 500, 'Arma', NULL),
('Escopeta M3', 'Una escopeta de doble cañón que dispara cartuchos de escopeta.', 800, 'Arma', NULL),
('Granada de Fragmentación', 'Una granada de mano que explota en fragmentos metálicos.', 300, 'Municion', NULL),
('Botiquín de Primeros Auxilios', 'Restaura la salud del personaje.', 200, 'Curacion', NULL),
('Spray de Primeros Auxilios', 'Restaura completamente la salud del personaje.', 400, 'Curacion', NULL),
('Chaleco antibalas', 'Ofrece protección adicional contra el daño de las balas.', 600, 'Armadura', NULL),
('Granada Flash', 'Una granada que emite una luz cegadora temporalmente.', 250, 'Municion', NULL),
('Lanzagranadas', 'Un lanzagranadas que dispara granadas explosivas.', 1200, 'Arma', NULL),
('Mina Terrestre', 'Una mina explosiva que se activa cuando alguien se acerca.', 350, 'Municion', NULL),
('Granada Incendiaria', 'Una granada que explota y genera fuego.', 300, 'Municion', NULL);

INSERT INTO Inventario (jugador_id, objeto_id, cantidad) VALUES
(1, 1, 1),
(1, 3, 5),
(1, 4, 3),
(2, 2, 1),
(2, 5, 2),
(2, 7, 4),
(2, 8, 1),
(3, 1, 1),
(3, 2, 1),
(3, 4, 2),
(4, 3, 2),
(4, 5, 1),
(4, 6, 1),
(4, 9, 3),
(5, 1, 1),
(5, 2, 1),
(5, 4, 2),
(5, 6, 1),
(5, 10, 4);

*/