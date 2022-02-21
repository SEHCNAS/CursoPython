use vw;
create table if not exists cidades ( # so permite criar a tabela caso a condição seja verdadeira
	id int unsigned not null auto_increment, # unsigned - defini que os valores sempre serão positivos
    nome varchar(255) not null,
    estado_id int not null,
    area decimal(10,2),
    primary key(id),
    foreign key(estado_id) references estados(id) # Defini a chave estrangeira, refenrenciando a outra tabela
);

