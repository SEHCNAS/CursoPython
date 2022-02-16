#Comentario no mySql

create database vw; #criar banco/schemma

use vw;

create table estados (
    id int not null auto_increment,
    nome varchar(45) not null,
    sigla varchar(2) not null,
    regiao enum('Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul') not null,
    populacao decimal(5,2) not null,
    primary key(id), #Defini qual valor vai ser chave primaria
    unique key(nome), #Defini qual campo vai ser unico 
    unique key(sigla)
);