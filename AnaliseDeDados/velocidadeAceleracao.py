import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Passo 1: Calcular o raio de cada roda
diametro_roda = 6.8 / 100  # Convertendo para metros
raio_roda = diametro_roda / 2

# Ler os dados
df = pd.read_csv('Pista-I.csv')

# Passo 2: Converter rpmEsquerdo e rpmDireito para velocidade linear (m/s)
df['velocidadeEsquerda'] = df['rpmEsquerdo'] * raio_roda
df['velocidadeDireita'] = df['rpmDireito'] * raio_roda

# Passo 3: Calcular a velocidade média do veículo
df['velocidadeMedia'] = (df['velocidadeEsquerda'] + df['velocidadeDireita']) / 2

# Passo 5: Calcular a aceleração ao longo do tempo
df['aceleracao'] = np.gradient(df['velocidadeMedia'], df['tempo'])

# Plotar a velocidade média e a aceleração ao longo do tempo
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(df['tempo'], df['velocidadeMedia'], label='Velocidade Média (m/s)')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade Média (m/s)')
plt.title('Velocidade Média ao Longo do Tempo')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(df['tempo'], df['aceleracao'], label='Aceleração (m/s²)', color='orange')
plt.xlabel('Tempo (s)')
plt.ylabel('Aceleração (m/s²)')
plt.title('Aceleração ao Longo do Tempo')
plt.legend()

plt.tight_layout()

# Salvar a figura
plt.savefig('velocidade_aceleracaoms.png')