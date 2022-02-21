select * from estados; # selecionar tudo

select nome as 'Nome do estado', sigla from estados; #colocar um nome em uma coluna

select nome as 'Nome do estado', sigla from estados #filtro
where regiao = 'sul';

select nome as 'Nome do estado', sigla, populacao from estados #Organização
where populacao >= 10
order by populacao;

select nome as 'Nome do estado', sigla, populacao from estados
where populacao >= 10
order by populacao desc;