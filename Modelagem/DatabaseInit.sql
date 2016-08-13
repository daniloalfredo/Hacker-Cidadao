DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Relatorio;
DROP TABLE IF EXISTS Sensor;
DROP TABLE IF EXISTS Agenda;
DROP TABLE IF EXISTS Local;
DROP TABLE IF EXISTS Cidade;


CREATE TABLE Cidade(
  Id INT PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(40)
);

CREATE TABLE Local(
  Id INT PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(40),
  Address TEXT,
  Tipo VARCHAR(40),
  Area NUMERIC,
  Perimeter NUMERIC,
  CodBairro NUMERIC,
  NomeBairro VARCHAR(40),
  Clogra NUMERIC,
  Id_City INT NOT NULL,
  constraint fk_id_city foreign key (Id_City) references Cidade(Id) on delete restrict on update cascade
);

CREATE TABLE Agenda(
  Id INT PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(40),
  Dia DATE,
  HoraBegin TIME,
  HoraEnd TIME,
  Id_Local INT NOT NULL,
  constraint fk_id_local foreign key (Id_Local) references Local(Id) on delete restrict on update cascade
);

CREATE TABLE Sensor(
  Id INT PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(40),
  Tipo VARCHAR(40),
  Unidade VARCHAR(10),
  Valor real,
  Id_Local INT NOT NULL,
  constraint fk_id_local2 foreign key (Id_Local) references Local(Id) on delete restrict on update cascade
);

CREATE TABLE Relatorio(
  Id INT PRIMARY KEY AUTO_INCREMENT,
  Descricao TEXT,
  Categ VARCHAR(40),
  Id_Local INT NOT NULL,
  constraint fk_id_local3 foreign key (Id_Local) references Local(Id) on delete restrict on update cascade
);

CREATE TABLE User(
  Id INT PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(100),
  login VARCHAR(40),
  password VARCHAR(40)
);
