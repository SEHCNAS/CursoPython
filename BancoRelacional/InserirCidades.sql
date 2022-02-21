use vw;
insert into cidades(nome, area, estado_id)
values ('Campinas', 795.0, 25);

insert into cidades(nome, area, estado_id)
values ('Niteroi', 133.9, 19);

select * from cidades;

insert into cidades(nome, area, estado_id) # INSERT COM SELECT PARA PROCURAR O ID DO ESTADO
values (
'Caruaru',
 920.6, 
(select id from estados where sigla = 'PE')); 

insert into cidades
(nome, area, estado_id) 
values (
'Juazeiro do Norte',
 248.2, 
(select id from estados where sigla = 'CE')); 