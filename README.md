## Teste de nivelamento estágio


## Requisitos Gerais

- Python 3.x
- PostgreSQL (para teste_3)
- Node.js e npm (para teste_4)

### Instalação das Dependências Python
```bash
pip install -r requirements.txt
```

### Instalação das Dependências Frontend (teste_4)
```bash
cd teste_4_api/frontend/vue-project
npm install
```

## Projetos

### 1. Web Scraping (teste_1_web_scraping)
Download e compactação de PDFs do site da ANS.

```bash
cd teste_1_web_scraping
python src/main.py
```

Saída: 
- PDFs baixados em `data/`
- Arquivo ZIP em `data/anexos.zip`

### 2. Transformação de Dados (teste_2_transformacao_dados)
Extração de dados de PDF para CSV.

1. Coloque o PDF na pasta `data/`
2. Execute:
```bash
cd teste_2_transformacao_dados
python src/main.py
```

Saída:
- CSV em `data/tabela_rol.csv`
- ZIP em `data/vinicius_ribeiro.zip`

### 3. Banco de Dados (teste_3_banco_de_dados)
Sistema de processamento e análise de dados da ANS.

1. Configure o PostgreSQL
2. Execute:
```bash
cd teste_3_banco_de_dados
python src/main.py
```
3. Execute os scripts SQL em `src/scripts/`
Obs: Atente-se ao caminho para importar os dados

### 4. API  (teste_4_api)
Sistema de consulta de operadoras com interface web.

Terminal 1 (Backend):
```bash
cd teste_4_api/backend
python main.py
```

Terminal 2 (Frontend):
```bash
cd teste_4_api/frontend/vue-project
npm run dev
```

Acesse: http://localhost:XXXX
Obs: Acesse a porta que for mostrada

## Estrutura de Dados

### Pasta data/
Cada projeto cria sua própria pasta caso ela nao exista `data/` para armazenar:
- PDFs baixados
- Arquivos CSV gerados
- Arquivos ZIP
- Dados temporários

## Observações

- Certifique-se de ter todas as dependências instaladas
- Alguns testes dependem de arquivos gerados por outro teste então utilize sequencialmente
- Todos os dados são obtidos de fontes públicas da ANS
