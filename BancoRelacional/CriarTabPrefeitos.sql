use vw;
create table if not exists prefeitos(
	id int unsigned not null auto_increment,
    nome varchar(255) not null,
    cidade_id int unsigned,
    primary key(id),
    unique key(cidade_id), # so pode haver uma coluna para cada cidade, não permite repeticao
    foreign key(cidade_id) references cidades(id)
);

