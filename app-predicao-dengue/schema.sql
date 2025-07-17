create table if not exists casos_diarios (
    id serial primary key,
    municipio varchar not null,
    data date not null,
    casos int not null
);
create index on casos_diarios(municipio);
create index on casos_diarios(data);