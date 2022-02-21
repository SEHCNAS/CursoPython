# inner join - Dados relacionados entre duas tabelas - tabela A - chave primaria e tabela b foreign key
select 
	A.nome as estados, 
    B.nome as cidade, 
    regiao 
from estados A
inner join cidades B
	on A.id = B.estado_id;
    
# Left Join - Dados relacionados entre as duas tabelas mas o conteudo da tabela A (tabela da esquerda)
select 
	A.nome as estados, 
    B.nome as cidade, 
    regiao 
from estados A
Left join cidades B
	on A.id = B.estado_id;
    
# Right Join - Dados relacionados entre as duas tabelas mas o conteudo da tabela B(tabela da direita)
select 
	A.nome as estados, 
    B.nome as cidade, 
    regiao 
from estados A
Right join cidades B
	on A.id = B.estado_id;
    
#full join - junção do left e do right 