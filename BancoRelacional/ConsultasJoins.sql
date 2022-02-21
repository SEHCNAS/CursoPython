use vw;

# Inner Join - retorna relacinados entre as duas tabelas que tem a referencia de cidade.id = prefeitos.cidade_id 
select * from cidades c inner join prefeitos p on c.id = p.cidade_id;

# Left Join - Retona os dados relacionados entre as tabelas e todas as cidades (cidades seria a tabela a esquerda)
select * from cidades c left join prefeitos p on c.id = p.cidade_id;

# Right Join - Retona os dados relacionados entre as tabelas e todos o prefeitos (Prefeitos seria a tabela a direita)
select * from cidades c Right join prefeitos p on c.id = p.cidade_id;

#full join - retorna todos os dados
# select * from cidades c full join prefeitos p on c.id = p.cidade_id;
select * from cidades c left join prefeitos p on c.id = p.cidade_id
union
select * from cidades c Right join prefeitos p on c.id = p.cidade_id;
