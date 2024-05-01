# 3 - Ordenando Valores na Leitura dos Dados

#1. Nessa aula vamos aprender a ordenar valores na leitura dos dados de um arquivo txt.

#2. Bem, imagine que o propósito do nosso arquivo txt que estamos escrevendo seja para armazenar os alunos que estão presentes em sala de aula.

#3. Uma boa funcionalidade que podemos ter é conseguir ordenar os valores do nosso arquivo, não é verdade?


names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
    
for name in sorted(names):
    print(f"Olá, {name}")

