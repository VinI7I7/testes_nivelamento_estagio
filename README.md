# Teste de Nivelamento - Estágio

## Tecnologias Utilizadas

- **Linguagens**: Python 3, JavaScript (Node.js)
- **Banco de Dados**: PostgreSQL 17
- **Frameworks**: Flask (backend), Vue.js (frontend)

---

## Instalação das Dependências

### **Dependências Python**
```bash
pip install -r requirements.txt
```

### **Dependências do Frontend (Teste 4)**
```bash
cd teste_4_api/frontend/vue-project
npm install
```

---

## Estrutura do Projeto

Cada teste está contido em uma pasta separada e deve ser executado na ordem recomendada abaixo.

### **1. Web Scraping (teste_1_web_scraping)**
Este teste realiza o download de PDFs do site da ANS e os compacta em um arquivo ZIP.

#### **Execução**
```bash
cd teste_1_web_scraping
python src/main.py
```

#### **Saída**
- PDFs baixados na pasta `data/`
- Arquivo ZIP salvo em `data/anexos.zip`

---

### **2. Transformação de Dados (teste_2_transformacao_dados)**
Este teste extrai dados de PDFs e os converte para CSV.

#### **Passos**
1. Coloque o PDF na pasta `data/`  (não é necessário caso tenha executado o Teste 1).
2. Execute:
```bash
cd teste_2_transformacao_dados
python src/main.py
```

#### **Saída**
- Arquivo CSV gerado em `data/tabela_rol.csv`
- Arquivo ZIP salvo em `data/vinicius_ribeiro.zip`

---

### **3. Banco de Dados (teste_3_banco_de_dados)**
Este teste processa e analisa os dados extraídos no PostgreSQL.

#### **Passos**
1. Configure o PostgreSQL e crie o banco de dados.
2. Execute:
```bash
cd teste_3_banco_de_dados
python src/main.py
```
3. Serão baixados e processados os CSVs necessários.
4. Execute os scripts SQL em `src/scripts/`.
---

### **4. API e Interface Web (teste_4_api)**
Este teste implementa um sistema de consulta de operadoras com interface web.

#### **Execução**

##### **Backend**
```bash
cd teste_4_api/backend
python main.py
```

##### **Frontend**
```bash
cd teste_4_api/frontend/vue-project
npm run dev
```

Acesse a interface web em: [http://localhost:5173](http://localhost:5173) (ou a porta exibida no terminal).

---

## Estrutura de Dados

Cada projeto cria sua própria pasta `data/` para armazenar:
- PDFs baixados
- Arquivos CSV gerados
- Arquivos ZIP
- Dados temporários


## Observações
- Certifique-se de instalar todas as dependências antes de rodar os testes.
- Alguns testes dependem de arquivos gerados em etapas anteriores.
- Todos os dados processados são de fontes públicas da ANS.

---
