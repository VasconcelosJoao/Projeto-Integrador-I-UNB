import pandas as pd

# Passo 1: Ler o arquivo CSV
df = pd.read_csv('Pistas-MS/Pista-I.csv')

# Passo 2: Converter a coluna `tempo` para segundos, arredondando para o segundo mais próximo
df['tempo_s'] = (df['tempo'] / 1000).round().astype(int)

df['corrente'] = df['corrente'] + 348

# Passo 3: Agrupar os dados por segundo
# Agrupar por 'tempo_s', somar os valores de 'coluna1' e calcular a média de 'coluna2'
df_agrupado = df.groupby('tempo_s').agg({
    'rpmEsquerdo': 'mean',  # Soma os valores na 'coluna1'
    'rpmDireito': 'mean',  # Soma os valores na 'coluna1'
    'corrente': 'mean' # Calcula a média dos valores na 'coluna2'
}).reset_index().round(2)

# Renomear a coluna 'tempo_s' para 'tempo'
df_agrupado.rename(columns={'tempo_s': 'tempo'}, inplace=True)

# Passo 5: Salvar o resultado em um novo arquivo CSV
df_agrupado.to_csv('Pistas-S/Pista-I.csv', index=False)