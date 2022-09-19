# Math Visualization

Repositório para organizar o código-fonte do projeto da Feira de Ciências do CTISM 2022.

## Resumo

O software desenvolvido aqui é um visualizador de funções matemáticas lineares e função do círculo, desenvolvido usando a biblioteca plotly, escrita em Python. O software é majoritariamente escrito em Python, com as projeções sendo geradas em HTML.

## Instalação

1. Clone este repositório na sua máquina
2. Crie um ambiente virtual e instale as dependências:

`conda create --name math --file requirements.txt --yes`
(mais sobre ambientes virtuais [aqui](https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/venvs.md#criando-pela-linha-de-comando))

3. Instale a biblioteca dash usando pip: `pip install dash==2.6.*`
4. Ative o ambiente virtual com `conda activate math`
5. Rode os scripts de teste pela linha de comando para verificar se tudo foi instalado corretamente, e.g. `python teste_plotly.py`

## Checklist de atividades

**Dica:** Para marcar um dos _checkboxes_ abaixo, edite o arquivo em Markdown
e troque de `[ ]` para `[x]`.

* [ ] Em 
* [ ] breve.

## Bibliografia

* [Documentação Dash (em inglês)](https://dash.plotly.com/)
* [Documentação plotly (em inglês)](https://plotly.com/python/)
   * A página de documentação contém códigos-fonte de exemplo para diversos tipos de projeção
* [API reference plotly (em inglês)](https://plotly.com/python-api-reference/)
   * A documentação da API contém a documentação de diversas funções da biblioteca plotly
* [Galeria de exemplo dash (em inglês)](https://dash-example-index.herokuapp.com/)