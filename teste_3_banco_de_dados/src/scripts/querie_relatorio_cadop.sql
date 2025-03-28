CREATE DATABASE teste3_banco_de_dados;

CREATE TABLE operadoras_ativas (
    registro_ans INT PRIMARY KEY,
    cnpj BIGINT,
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(255),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(10),
    ddd CHAR(3),
    telefone VARCHAR(20), 
    fax VARCHAR(15),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    regiao_comercializacao INT,
    data_registro_ans DATE
);

COPY operadoras_ativas FROM 'C:\Projetos\testes_nivelamento_estagio\data\Relatorio_cadop.csv' WITH CSV HEADER ENCODING 'UTF8' DELIMITER ';' NULL '';
