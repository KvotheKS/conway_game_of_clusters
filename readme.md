# Conway's Game Of "Life"

## Summary
## Novo Modelo
    O meu modelo antigo continha vários problemas, tanto em sua construção quanto na própria hipótese causal. Portanto os dois foram feitos dos zero, de que em seu estado atual, são duas simulações completamente diferentes, de forma que comparações com o antigo não são muito produtivas.
## Hipótese Causal
A hipótese causal consiste do pensamento de que pessoas são extremamente comunicativas, podem mudar de opinião, porém ainda assim serem fanáticas por algum grupo e/ou ideologia. E ainda por cima de tudo isso, a noção de que é muito mais fácil uma pessoa ser convencida por um amigo carismático a continuar num grupo do que ser levado a outra ideologia que é 'alien'. Com o pensamento em mente, supomos neste texto que quanto mais comunicativo e aberto a opinião as pessoas são, maior a chance delas mudarem de grupo, e quando as pessoas são líderes ou estão próximas de um líder dentro de um grupo, menor a variação dentro do grupo. E por fim, como situação emergente, analisa-se que grupos tendem a se fundir e a diferença entre cada situação é a velocidade com o qual isso ocorre.
## Mudanças
    Como o meu desejo era analisar a clusterização, modifiquei todo o código de que a simulação consiste em realmente todas as celulas focarem em agrupamentos. O antigo não fazia muito sentido dado sua hipótese. Antes tentei utilizar o Game of Life como base lógica, o que foi extremamente contraditório e não atingiu minha expectativa. As mudanças feitas, portanto, foram variadas, mas agora o código nem sequer se assemelha ao que antes era sua base, o Game of Life.

## Descrição das variáveis
As variáveis do csv são as seguintes:

* initial_chance - que dita a chance de alguem iniciar com grupo.
* ambition_ceil - que dita a chance de alguem virar um lider do grupo
* opinion_ceil - que dita a chance de alguem mudar de grupo
* polarization - que dita a influencia dentro do grupo que um lider tem
* Group Size index - dita a disparidade de tamanho entre os grupos da simulação
* Local Variety index - dita q disparidade de opiniões diferentes vizinhas entre as células
* Ideology Index - dita a quantidade de diferentes grupos presentes na simulação

## How to Run

To run the model interactively, run ``mesa runserver`` in this directory. e.g.

```
    $ mesa runserver
```

Then open your browser to [http://127.0.0.1:8521/](http://127.0.0.1:8521/) and press ``run``.

or

Just run ``python run.py`` in this directory. e.g.

```
    $ python run.py
```

## Dependencies

mesa
matplotlib