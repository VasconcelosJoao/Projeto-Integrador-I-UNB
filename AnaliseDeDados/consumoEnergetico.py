import pandas as pd
import matplotlib.pyplot as plt

# Ler os dados do arquivo CSV
df = pd.read_csv('Pistas-MS/Pista-III.csv')

# Ajuste para evitar corrente negativa devido a ruído
df['Corrente_Convertida'] = abs((df['corrente'])*(5.000)/(1023.000*0.185) * 12)




# Calcular o consumo energético em Watt-hora (Wh), assumindo tensão constante de 5V
df['Consumo_Energetico'] = (df['Corrente_Convertida'])/1000

# Converter o consumo energético para kWh
df['Consumo_Energetico_kWh'] = df['Consumo_Energetico'] / 3600

# Calcular o consumo total de energia ao longo do tempo
df['Consumo_Total_kWh'] = df['Consumo_Energetico_kWh'].cumsum()

# Criar uma figura com dois subplots (gráficos)
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
# Plotar o gráfico de consumo energético em kWh ao longo do tempo
plt.plot(df['tempo'], df['Consumo_Energetico_kWh'], label='Consumo Energético (kWh)')
plt.xlabel('Tempo (s)')
plt.ylabel('Consumo Energético (kWh)')
plt.title('Consumo Energético ao Longo do Tempo')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
# Plotar o gráfico do consumo total de energia em kWh ao longo do tempo
plt.plot(df['tempo'], df['Consumo_Total_kWh'], color='red', label='Consumo Total de Energia (kWh)')
plt.xlabel('Tempo (ms)')
plt.ylabel('Consumo Total de Energia (kWh)')
plt.title('Consumo Total de Energia ao Longo do Tempo')
plt.grid(True)
plt.legend()

# Ajustar o layout e salvar a imagem do gráfico
plt.tight_layout()
plt.savefig('grafico_consumo_energetico_e_total_kWh.png')