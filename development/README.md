# Desenvolvimento

Arquivo contendo o conteúdo do repositório em sua etapa de desenvolvimento.

## Checklist de atividades

**Dica 1:** Para marcar um dos _checkboxes_ abaixo, edite o arquivo em Markdown
e troque de `[ ]` para `[x]`.

**Dica 2:** Escreva o seu nome entre parênteses para informar que vai fazer
aquela atividade.

### Primeira rodada

1. [x] (Henry) Organizar tudo.
2. [x] (Bruno) Implementar função para converter da equação reduzida da reta para a equação geral.
      * Dica: pesquise a função `eval` para validar expressões matemáticas
3. [x] (aline) Implementar função para converter da equação geral da reta para a equação reduzida.
      * Dica: pesquise a função `eval` para validar expressões matemáticas
4. [x] (Tales) Implementar função que, dada uma equação reduzida da reta, informa os coeficientes angular e linear.
5. [x] (Liza) Implementar função que, dada uma equação geral da reta, informa os coeficientes a, b e c.
6. [x] (Henry) Implementar função que, dada uma equação de reta (geral ou reduzida), informa o ângulo formado com o eixo x.
7. [x] (Nicole) Implementar uma função que, dada uma equação da circunferência, informa o centro, e o raio da mesma.
8. [x] (Gui) Implementar função que, dadas duas equações, uma de reta e uma de circunferência, informa se ambas são
       secantes, tangentes ou não se interceptam. Caso sejam secantes e tangentes, informar em qual(quais) ponto(s)
       isto ocorre.
9. [x] (Luize) Implementar layout da página HTML utilizando dash.
      * Dica: https://dash.plotly.com/dash-core-components
10. [x] (Henry) implementar gráfico da reta e da circunferência.

### Segunda rodada

1. [x] (Tales) Descobrir porque, para certas equações gerais da reta, a função [funcoes/coeficientes_geral/main.py]() 
       não está gerando os coeficientes a, b, e c.
2. [x] (Guilherme) Descobrir porque, para certas equações reduzidas da circunferência, a função [funcoes/calculo_raio_e_centro/main.py]() 
       não está gerando as coordenadas do centro e o raio.
3. [x] (Bruno) Fazer com que o gráfico fique estilizado da mesma maneira que o site (linhas e pontos em azul, background
       em rosa). 
       Remover também a grade de background. Em outras palavras, deixar o gráfico esteticamente bonito
   * Dica 1: consultar [documentação](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scatter.html) 
            da função que gera o gráfico, e procurar por **color** ou **background color**
   * Dica 2: Pode ser que seja preciso consultar a documentação do 
               [layout](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html) ou da 
               [Figure](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html)
4. [x] (Luize) Capturar o movimento do mouse que o usuário fizer enquanto mexer na ferramenta, e salvar em um arquivo.
       Usar o exemplo que está na pasta [tracking](tracking)
   * (**ainda não feito**) Bônus: capturar a entrada de texto dos inputs também
5. [x] (Suzi) Escrever o texto de introdução da ferramenta.
6. [x] (Luize) Colocar o texto da introdução da ferramenta em um modal, logo que o usuário abrir a página. O modal é 
       importante porque ele define em que momento a ferramenta vai começar a capturar os dados do mouse e entradas de 
       texto. A captura deve se encerrar depois de x minutos (por exemplo, 5 minutos)
7. [x] (Aline) Para cada um dos arquivos dentro da pasta [funcoes](app/funcoes), colocar exemplos de caso de uso na função
       main, para testar se a função está funcionando corretamente (usar o arquivo [angulo_eixo_x](app/funcoes/angulo_eixo_x.py)
       como exemplo). Caso, para algum tipo de entrada de texto, a função não funcione, avisar os colegas responsáveis 
       para que eles façam a correção.
8. [x] (Liza, Nicole) Fazer o banner para a JAI no Canva.
9. [x] Apresentar a ferramenta na feira de Ciências. 
   * Sexta-feira de manhã: Tales, Guilherme
   * Sexta-feira de tarde: Liza, Aline
   * Sábado: Luize, Liza
10. [x] (Henry) Resolver referências cíclicas das callbacks do dash e revisão final da ferramenta.

## API

Esta seção detalha, de acordo com os itens descritos no [Checklist de atividades](#checklist-de-atividades), qual 
deve ser a entrada e a saída esperada de cada uma das funções implementadas.

Por exemplo, para o primeiro item da lista, devemos implementar uma função que recebe uma string, e retorna uma string
também. Em Python, essa função teria essa forma:

```python
def reta_reduzida_para_geral(reduzida: str) -> str:
   return 'ax + by + c = 0'
```

Perceba que esta função recebe uma variável como parâmetro (`reduzida`, do tipo `str`), e retorna uma variável do tipo
`str` também. Por isso, a **Entrada** na tabela abaixo é uma `str`, e a **saída** é uma `str` também.

É importante atentar-se esta tabela pois alguns colegas precisarão do retorno de uma função que você irá implementar,
para implementar as suas próprias funções. O tipo de retorno influenciará na maneira como os colegas farão o trabalho
deles.

| Item da checklist |       Entrada |                                         Saída |
|:------------------|--------------:|----------------------------------------------:|
| 2                 |           str |                                           str |
| 3                 |           str |                                           str |
| 4                 |           str |                                  float, float |
| 5                 |           str |                           float, float, float |
| 6                 |           str |                                         float |
| 7                 |           str |                    tuple(float, float), float |
| 8                 |           str | str, tuple(float, float), tuple(float, float) |
| 9                 | não se aplica |                                 não se aplica |
| 10                | não se aplica |                                 não se aplica |


## Link da reunião 

[link](https://drive.google.com/file/d/1jte5aDalkYnU4661NR-E6pZAd0d8ITp8/view?usp=sharing)

## Bibliografia

* [Documentação Dash (em inglês)](https://dash.plotly.com/)
* [Documentação plotly (em inglês)](https://plotly.com/python/)
   * A página de documentação contém códigos-fonte de exemplo para diversos tipos de projeção
* [API reference plotly (em inglês)](https://plotly.com/python-api-reference/)
   * A documentação da API contém a documentação de diversas funções da biblioteca plotly
* [Galeria de exemplo dash (em inglês)](https://dash-example-index.herokuapp.com/)

## Desenho da interface gráfica

![](croqui.png)