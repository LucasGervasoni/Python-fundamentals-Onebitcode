# 1 - Escrevendo em Arquivo Txt

#1. Nessa aula vamos aprender a escrever dados em um arquivo txt.

#2. Até aqui, você aprendeu a criar diversos programas em Python, porém, todas as informações eram salvas apenas em memória. Uma alternativa para persistir dados é utilizando arquivos.

#3. Para escrever em arquivos utilizamos a função open() e podemos utilizar algumas opções como parâmetro, como a opção **w** e a opção **a**.


name = input("Qual seu nome?\n")

# r - leitura
# w - escrita
# a - append
file = open("names.txt", "w")
file.write(name)
file.close()

name = input("Qual seu nome?\n")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()


#5. Como você pode ver, nos dois códigos acima, estamos trabalhando com o modo de escrita de dados (opção **a - append** e **w - write).** 

#6. Uma boa forma de refatorar esse código é utilizar o contexto com o with. Vamos utilizá-lo em boa parte dos próximos exemplos.


name = input("Qual seu nome?\n")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
