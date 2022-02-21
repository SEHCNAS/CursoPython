# Buscar dados em duas tabelas 
select * from estados e, cidades c
where e.id = c.estado_id;

select e.nome as estados, c.nome as cidade, regiao from estados e, cidades c
where e.id = c.estado_id;

select 
	e.nome as estados, 
    c.nome as cidade, 
    regiao 
from estados e
inner join cidades c
	on e.id = c.estado_id;

