DROP DATABASE biblioteca;

CREATE DATABASE biblioteca;

USE biblioteca;

CREATE TABLE categoria ( 
	categoria varchar(20),
    id_colecao int4
);

CREATE TABLE colecao(
	id_colecao int4,
    id_livro serial primary key
);

CREATE TABLE livro(
	id_livro serial primary key,
    nm_livro varchar(50),
    autor varchar(30)
);