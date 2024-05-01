1. Nessa aula vamos aprender alguns comandos utilitários do Pip.

2. Bem, o primeiro comando que temos de importante do pip, é o **pip list.** Esse comando vai nos ajudar a listar as bibliotecas que estão instaladas no projeto.

![Img1.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e9f6303d-8415-4ca7-a75e-577c442c5603/Img1.png)

3. Note que foram listadas apenas duas bibliotecas, que são bibliotecas utilitárias para o funcionamento do ambiente virtual de desenvolvimento.

4. Um comando muito útil é o pip install. Ele serve para instalar bibliotecas. Vamos experimentar instalando a biblioteca pyinstaller, com o comando: **pip install pyinstaller**

![Img2.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/32f4475c-92f9-4f05-a7eb-a00d3d988466/Img2.png)

5. Outro comando bem útil também, é o **pip freeze**. Esse comando retorna o resultado com um formato pronto para que possamos copiar as bibliotecas e versões e instalar com o pip. 

![Img3.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/edbb9268-010a-43b4-aa8c-b88ea787e496/Img3.png)

6. Por último, poderíamos adicionar o resultado anterior para um arquivo .txt, que vai ficar responsável pela listagem das bibliotecas, bem como de suas versões. Podemos usar esse comando: **pip freeze -l > requirements.txt.** 

7. Agora que temos a informação pronta no arquivo requirements.txt, é só executar o comando **pip install -r requirements.txt** e todas as bibliotecas serão instaladas.