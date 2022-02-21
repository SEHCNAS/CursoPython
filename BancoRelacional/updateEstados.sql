update estados
set nome = 'Maranhão'
where sigla = 'MA';

SELECT NOME FROM ESTADOS WHERE SIGLA = 'MA';

update estados
set nome = 'Paraná', populacao = 11.32
where sigla = 'PR';

SELECT NOME, POPULACAO FROM ESTADOS WHERE SIGLA = 'PR';