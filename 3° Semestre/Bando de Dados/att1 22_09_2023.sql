CREATE DATABASE EXERCICIO;
USE EXERCICIO;

CREATE TABLE camisas (
  idCamisa TINYINT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(25),
  tamanho ENUM('pequena','média','grande','extra-grande')
);


INSERT INTO camisas (nome, tamanho)
VALUES ('regata', 'grande');

INSERT INTO camisas (nome, tamanho)
VALUES ('social', 'medium'); /* erro */

INSERT INTO camisas (nome, tamanho)
VALUES
('social', 'média'),
('polo', 'pequena'),
('polo', 'grande'),
('camiseta', 'extra-grande');



CREATE TABLE pedidos (
  idPedido SMALLINT PRIMARY KEY AUTO_INCREMENT,
  lanche ENUM ('Presunto','Frango','Salame'),
  tempero SET ('Azeite','Vinagre','Sal','Orégano','Pimenta')
);

-------

INSERT INTO pedidos (lanche, tempero)
VALUES
('Presunto','Sal,Orégano'),
('Salame','Azeite,Pimenta'),
('Frango','Azeite,Sal,Orégano'),
('Presunto','');


-------------


CREATE TABLE venda (
  idVenda SMALLINT PRIMARY KEY AUTO_INCREMENT,
  horaVenda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  dataEntrega DATE,
  horaEntrega TIME
);

INSERT INTO venda (dataEntrega, horaEntrega)
VALUES ("2018-12-03", "13:40:00");

INSERT INTO venda (dataEntrega, horaEntrega)
VALUES ("20181223", "134000");

SELECT * FROM venda;

----------- /*AULA 22-09-2023*/;

CREATE TABLE Eventos (
	evento_id INT AUTO_INCREMENT PRIMARY KEY,
    nome_evento VARCHAR(100),
    descricao TEXT,
    categoria ENUM('TRABALHO', 'LAZER', 'ESTUDO', 'OUTRO') NOT NULL,
    dias_semana SET('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo') NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_evento DATE NOT NULL,
    hora_evento DATE,
    data_hora_evento DATETIME,
    ano_evento YEAR
);