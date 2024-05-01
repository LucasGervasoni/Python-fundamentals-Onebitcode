# 8 - Escrevendo Dados em CSV

#1. Nessa aula vamos aprender a escrever dados csv em Python.
#2. Utilizando o módulo csv, essa tarefa ficará bem mais tranquila. E o melhor é que assim, podemos tornar o programa mais interativo com o usuário.


import csv

name = input("Informe o nome da linguagem que deseja aprender?\n")
category = input("Qual categoria que a linguagem se encaixa?\n")

with open("languagens.csv", "a", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow([name,category])
