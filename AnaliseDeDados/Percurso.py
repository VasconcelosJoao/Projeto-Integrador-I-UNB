import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Função para plotar o percurso de um carrinho com base em um arquivo CSV
def plot_path(filename, d=10):
    # Ler o arquivo CSV em um DataFrame
    df = pd.read_csv(filename)

    # Calcular a velocidade média das rodas
    df['v_avg'] = (df['r1'] + df['r2']) / 2

    # Calcular a diferença de velocidade entre as rodas
    df['v_diff'] = df['r1'] - df['r2']

    # Calcular o ângulo de rotação com base na diferença de velocidade
    df['theta'] = np.cumsum(df['v_diff'] / d)  

    # Calcular a posição x com base na velocidade média e no ângulo de rotação
    df['x'] = np.cumsum(df['v_avg'] * np.cos(df['theta']))

    # Calcular a posição y com base na velocidade média e no ângulo de rotação
    df['y'] = np.cumsum(df['v_avg'] * np.sin(df['theta']))

    # Criar uma nova figura
    plt.figure(figsize=(10,5))

    # Plotar o percurso do carrinho
    plt.plot(df['x'], df['y'])

    # Definir a mesma escala para os eixos x e y
    plt.axis('equal') 

    # Adicionar uma grade ao gráfico
    plt.grid(True) 

    # Definir o rótulo do eixo x
    plt.xlabel('Posição X (cm)')

    # Definir o rótulo do eixo y
    plt.ylabel('Posição Y (cm)')

    # Definir o título do gráfico
    plt.title('Esboço do Percurso')

    # Salvar o gráfico em um arquivo PNG
    plt.savefig('percurso.png')

plot_path('random_path.csv')

## rpm -> m/s = rpm*2*pi*r/60