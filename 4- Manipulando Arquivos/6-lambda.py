# 10 - Utilizando Expressão Lambda

#1. Nessa aula vamos aprender a ordenar valores lidos de um arquivo csv em um dicionário.
#2. Uma outra forma e mais fácil de ordenar valores em um dicionário é utilizando uma expressão lambda.


courses = []
with open("languagens.csv", encoding="utf-8") as file:
    for line in file:
        name, category = line.rstrip().split(",")
        course = {}
        course["name"] = name
        course["category"] = category
        courses.append(course)
print(courses)

for course in sorted(courses, key=lambda course: course["name"], reverse=True):
    print(f"{course['name']} -{course['category']}")
