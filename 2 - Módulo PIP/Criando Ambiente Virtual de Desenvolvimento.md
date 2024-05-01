1. Nessa aula vamos aprender a criar um ambiente virtual de desenvolvimento na linguagem Python.

2. A principal vantagem de ter um ambiente virtual de desenvolvimento, é que **isolamos** as bibliotecas que serão utilizadas em um projeto, o que vai facilitar bastante quando se quiser fazer o deploy de um projeto.

3. Em nosso caso, o deploy do aplicativo será a geração do arquivo instalador da aplicação do Tkinter. Por isso, vamos nos certificar de que apenas as bibliotecas necessárias sejam utilizadas no projeto.

4. Para criar o ambiente virtual de desenvolvimento, pode-se executar o comando no terminal: **python -m venv .venv** 

    1. Estamos indicando que vamos criar um diretório .venv, que vai ser o diretório que armazenará as bibliotecas que instalarmos nesse ambiente de desenvolvimento.

    2. Para ativar o ambiente virtual de desenvolvimento, pode ser executado o comando: **./.venv/Scripts/activate**
    
    3. Como pode ser visto na imagem abaixo, já estamos dentro do ambiente virtual de desenvolvimento.