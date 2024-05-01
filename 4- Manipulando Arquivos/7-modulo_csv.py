# 11 - Utilizando o Módulo CSV

#1. Nessa aula vamos aprender a lê valores lidos de um arquivo csv utilizando o módulo built in csv.
#2. Até então estávamos usando o arquivo csv sem título nas colunas. Com a utilização deste módulo conseguiremos trabalhar com esse exemplo.


import csv 

courses = []
with open("languagens.csv", encoding="utf-8") as file:
   reader = csv.DictReader(file)
   for row in reader:
       courses.append({"name": row["name"], "category": row["category"]})

for course in sorted(courses, key=lambda course: course["name"], reverse=True):
    print(f"{course['name']} -{course['category']}")
