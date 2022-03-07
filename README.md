### Sumário

Conway Game of Clusters é um modelo que busca transformar a simulação do famoso Game of Life em uma análise de clusterização, deixando os parametros de morte mais favoráveis para clusters sobreviverem e as celulas dentro de pequenos grupos continuarem vivas.

As mudanças feitas no Game of Life foram para tornar o jogo mais aleatório e mais voltado para agrupamento de células. Para isso, foi determinado que grupos de 3 a 5 agentes continuam vivos, além de que células mortas tem uma chance de voltarem a vida. Essas mudanças tem como efeito esperado uma entropia maior, e também uma "densidade" que alterna entre iterações que existem vários clusters e outras que são primariamente compostas por células que renasceram e estão relativamente longes umas das outras.

Essa simulação funciona de maneira que o estado inicial acaba importando bem menos que no Game of Life, dado o fato de que células podem renascer aleatóriamente.

### Instalação dos requisitos e execução do programa

Para a utilização do programa, foram utilizados:

* Python3 3.8.10
* Python Mesa

Para instalar a biblioteca Mesa, basta utilizar o seguinte comando:

* pip install mesa

Para usar o programa, basta executar o script run.py, para isso foi utilizado o seguinte comando no terminal:

* python3 /conways_game_of_life/run.py

## Controle da Simulação

Na simulação foram disponibilizadas duas variáveis controláveis por usuário, uma que determina a chance inicial das células estarem vivas, e outra que determina a chance de células mortas renascerem.

### Resultados do programa

Para fins de análise do programa, logo abaixo da simulação em questão, há um gráfico que mostra qual é a média de clusterização do programa.

A cada 15 passos da simulação são gravados dois arquivos em disco: agent.csv e model.csv, que guardam informações de agente e modelo respectivamente. As variáveis de agente estão relacionadas a posição e quantidade de vizinhos (caso a célula esteja viva), e as variáveis de modelo estão relacionadas a média de clusterização da simulação.

Esses arquivos se encontram na pasta "conways_game_of_life". Os arquivos .csv que já se encontram na pasta foram resultados de simulações feitas no dia 06/03/2022