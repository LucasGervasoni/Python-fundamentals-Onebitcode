# 4 - Transformando em Dicionário

#1. Nessa aula vamos aprender a transformar os dados lidos de um arquivo csv em um dicionário.
#2. Podemos utilizar um dicionário para armazenar as informações baseadas em chave e valor. E aí podemos utilizar uma lista e adicionar cada um dos dicionários dentro dela.


courses = []
with open("languagens.csv", encoding="utf-8") as file:
    for line in file:
        name, category = line.rstrip().split(",")
        course = {}
        course["name"] = name
        course["category"] = category
        courses.append(course)
print(courses)

for course in courses:
    print(f"{course['name']} -{course['category']}")
