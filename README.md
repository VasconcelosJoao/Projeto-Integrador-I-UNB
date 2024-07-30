# Projeto Integrador 1 - Carrinho Seguidor de Linha

## Descrição

Este projeto foi desenvolvido para a disciplina de Projeto Integrador 1 da Universidade de Brasília (UnB). O objetivo foi construir um carrinho seguidor de linha utilizando dois Arduinos: um para controlar a movimentação do carrinho e outro para coletar dados de desempenho. Após a construção, foram realizadas análises dos dados coletados para avaliar o desempenho do carrinho.

## Tabela de Conteúdos

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Componentes](#componentes)
- [Montagem do Carrinho](#montagem-do-carrinho)
- [Análise de Dados](#análise-de-dados)
- [Resultados](#resultados)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Tecnologias Utilizadas

- Arduino IDE
- Python
- Pandas
- Matplotlib

## Componentes

- 2 Arduinos (Uno)
- 2 Motores DC
- 3 Sensores de Linha
- 1 Bateria de 9V
- Jumpers
- Protoboard
- Chassi de Carro

## Montagem do Carrinho

1. **Conexões**:
   - Conecte os motores DC aos pinos digitais do Arduino responsável pela movimentação.
   - Conecte os sensores de linha aos pinos digitais do Arduino controlador.
   - Conecte a bateria de 9V ao Arduino.

2. **Programação**:
   - O Arduino de movimentação é responsável por controlar a velocidade e direção dos motores, utilizando os sensores para seguir a linha.
   - O segundo Arduino coleta dados como velocidade e corrente, registrando-os em um cartão SD.

## Análise de Dados

Os dados coletados pelo Arduino de monitoramento são armazenados em um arquivo CSV. Utilizando Python e bibliotecas como Pandas e Matplotlib, foram realizadas análises para calcular a velocidade média, aceleração e consumo energético do carrinho. Os scripts de análise incluem:

- **Plotagem do percurso**: Visualização do caminho percorrido pelo carrinho.
- **Cálculo do consumo energético**: Avaliação do consumo de energia ao longo do tempo.
- **Análise de velocidade e aceleração**: Estudo do desempenho do carrinho em diferentes condições.

## Resultados

O carrinho seguidor de linha demonstrou um bom desempenho ao seguir trajetos pré-definidos. As análises dos dados permitiram identificar padrões de consumo energético e otimizar o controle da velocidade e direção do carrinho.

## Contribuição

Contribuições são bem-vindas! Para contribuir, siga os passos abaixo:

1. Fork o repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça suas alterações e commit (`git commit -m 'Adicionando nova funcionalidade'`).
4. Envie para o repositório remoto (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
