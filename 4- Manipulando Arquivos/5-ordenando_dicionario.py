# 5 - Ordenando Valores no Dicionário

#1. Nessa aula vamos aprender a ordenar valores lidos de um arquivo csv em um dicionário.
#2. Diferentemente do que fizemos em aulas anteriores, para ordenar valores em um dicionário, é necessário um pouco mais de trabalho, então mãos a obra.


courses = []
with open("languagens.csv", encoding="utf-8") as file:
    for line in file:
        name, category = line.rstrip().split(",")
        course = {}
        course["name"] = name
        course["category"] = category
        courses.append(course)
print(courses)

def get_name(course):
    return course["name"]

def get_category(course):
    return course["category"]

for course in sorted(courses, key=get_category, reverse=True):
    print(f"{course['name']} -{course['category']}")
