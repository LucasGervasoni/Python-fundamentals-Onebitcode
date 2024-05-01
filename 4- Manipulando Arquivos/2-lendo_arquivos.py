# 2 - Lendo Dados de um Arquivo

#1. Nessa aula vamos aprender a ler dados de um arquivo txt.
#2. Bem, se você executou o arquivo da aula anterior, você já deve ter um arquivo em txt criado. 
#3. Nessa aula vamos aprender a ler dados de um arquivo txt. Utilizamos a propriedade **r** no método open, que significa **read**.


with open("names.txt", "r") as file:
    for line in file:
        print(f"Olá {line}")

with open("names.txt", "r") as file:
    for line in file:
        #print(f"Olá {line}")
        print(f"Olá {line.rstrip()}") #retira o espaço das palavras
