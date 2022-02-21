insert into empresas
	(nome, cnpj)
values 
	('Bradesco', 95694186000132),
    ('Bradesco', 27887148000146),
    ('Bradesco', 01598317000134);
    
update empresas
set nome = 'Vale'
where id = 2;

update empresas
set nome = 'Itau'
where id = 3;
    
alter table empresas
modify cnpj varchar(14);

desc empresas; # mostra campos da tabela, informações dos campos

select * from empresas;
select * from cidades;

insert into empresa_unidades
	(empresa_id, cidade_id, sede)
values
	(1, 8, 1),
    (1, 9, 0),
    (2, 8, 0),
    (2, 9, 1);
