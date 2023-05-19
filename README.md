# Math Visualization

Repositório para organizar o código-fonte do projeto da Feira de Ciências do CTISM 2022.

## Resumo

O Software desenvolvido aqui é um visualizador de funções matemáticas lineares e função do círculo, desenvolvido usando 
a biblioteca dash, escrita em Python. O Software é majoritariamente escrito em Python, com as projeções sendo geradas 
em HTML.

## Instalação

1. Clone este repositório na sua máquina.
2. Crie um ambiente virtual e instale as dependências do conda:

   ```bash
   conda create --name math --file requirements.txt --yes
   ```

   (mais sobre ambientes virtuais [aqui](
   https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/venvs.md#criando-pela-linha-de-comando))

3. Ative o ambiente virtual com `conda activate math`
4. Instale as dependências do pip (dash e dash-boostrap-components):
   
   ```bash
   pip install --requirement pip_requirements.txt
   ```

5. Rode o script `main.py`. **Nota:** o dash informa um link na linha de comando (por exemplo, `http://127.0.0.1:8050/`) 
   que você precisará copiar-e-colar no seu navegador para abrir a página. Não se esqueça de, depois de rodar o código, 
   pressionar `CTRL + C` para parar a execução do script.


