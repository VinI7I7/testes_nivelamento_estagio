# Web Scraping de PDFs da ANS

Este projeto realiza web scraping de PDFs do site da ANS (Agência Nacional de Saúde Suplementar) e os compacta para armazenamento.

## Estrutura do Projeto


```
teste_1_web_scraping/
├── src/
│   ├── utils/         # Utilitários para download e compressão
│   └── main.py        # Arquivo principal do programa
└── .gitignore
└── requirements
```

## Funcionalidades

- Download automático de PDFs de uma fonte web
- Compactção dos PDFs baixados
- Tratamento de erros 


## Requisitos

- Python 3
- Dependências listadas em requirements.txt 

## Como Executar

1. Clone o repositório
2. Navegue até o diretório do projeto
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o arquivo principal:
   ```bash
   python src/main.py
   ```

## Observações

Este projeto foi desenvolvido como parte de um teste de nivelamento para estágio.
