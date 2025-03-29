CREATE TABLE dados_financeiros (
    data DATE,
    reg_ans INTEGER,
    cd_conta_contabil BIGINT,
    descricao TEXT,
    vl_saldo_inicial DECIMAL(15,2),
    vl_saldo_final DECIMAL(15,2)
);

-- Alterar conforme o arquivo que desejar importar para a tabelar
COPY dados_financeiros FROM 'C:\Projetos\testes_nivelamento_estagio\extract_data\1T2023\1T2023.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');

-- Quais as 10 operadoras com maiores despesas - Intervalo de 1 ano
SELECT 
    reg_ans,
    cd_conta_contabil,
    descricao,
    SUM(vl_saldo_final - vl_saldo_inicial) AS despesas_total
FROM 
    dados_financeiros
WHERE
    descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR %'
    AND data >= CURRENT_DATE - INTERVAL '3 months' 
GROUP BY
    reg_ans, cd_conta_contabil, descricao
ORDER BY
    despesas_total DESC
LIMIT 10;

-- Quais as 10 operadoras com maiores despesas Intervalo de 3 meses
SELECT 
    reg_ans,
    cd_conta_contabil,
    descricao,
    SUM(vl_saldo_final - vl_saldo_inicial) AS despesas_total
FROM 
    dados_financeiros
WHERE
    descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR %'
    AND data >= CURRENT_DATE - INTERVAL '1 year' 
GROUP BY
    reg_ans, cd_conta_contabil, descricao
ORDER BY
    despesas_total DESC
LIMIT 10;
