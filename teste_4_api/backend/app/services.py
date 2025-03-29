import pandas as pd

def search_operadoras(query, df):
    query = query.lower()
    results = []
    primary_columns = ['Razão Social', 'Nome Fantasia', 'Registro ANS', 'CNPJ']

    for _, row in df.iterrows():
        score = 0
        row_data = {}

        for col in df.columns:
            if pd.notna(row[col]):
                value = str(row[col]).lower()

                if query in value:
                    score += 10 if col in primary_columns else 5
                    if value == query:
                        score += 15
                row_data[col] = row[col]

        if score > 0:
            results.append({'score': score, 'data': row_data})

    results.sort(key=lambda x: x['score'], reverse=True)
    return [item['data'] for item in results]
