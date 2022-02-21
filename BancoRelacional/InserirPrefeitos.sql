use vw;

select * from cidades;

select * from prefeitos;

insert into prefeitos
	(nome, cidade_id)
values
	('Rodrigo Neves', 9),
    ('Raquel Lira', 10),
    ('Joao Null ', null);
    
insert into prefeitos # Permite repetição de null
	(nome, cidade_id)
values
    ('Rafael Greca', null);
    
insert into prefeitos # Erro por coluna com valor duplicada
	(nome, cidade_id)
values
    ('Rodrigo Pinheiro', 9);