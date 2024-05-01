# Strings

#> A técnica de slice ou fatiamento, é muito utilizada em Python, pois por meio dela, podemos extrair substrings dentro de uma string.


gameName = 'Fifa23'
gameDescription = '''
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar 
localmente ou online.


# string[início:fim] - índice começa com 0 | índice final -1

# Busque toda string a partir da primeira posição
print(gameName[0:])

# Busque toda string até a última posição
print(gameName[:6])

# Busque toda string da primeira até a última posição
print(gameName[0:6])

"""
string[início:fim:passo] - índice começa com 0 | índice final -1 | 
passo - determina o incremento. Por padrão esse número é o 1
"""

#Busque toda a string de 2 em 2 caracteres.
print(gameName[::2])

# Inverta uma string de trás pra frente
print(gameName[::-1])

# Imprime os caracteres nos índices ímpares
print(gameName[1::2])

# saida
Fifa23
Fifa23
Fifa23
Ff2
32afif
ia3
'''

#> Trabalhar com métodos que poderão deixar uma string em minúsculo, maiúsculo, apenas a primeira letra maiúscula, vamos aprender também a contar caracteres dentro de uma string, etc.


gameName = 'Fifa23'
gameDescription = '''
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports,
e que possibilita jogar 
localmente ou online.
'''

print(gameName.upper()) #Maiúsculo
print(gameName.lower()) # Minúsculo
print(gameName.capitalize()) #Apenas primeira letra maiúscula
print(gameName.title()) #Apenas primeira letra maiúscula
print(gameName.center(10, '-')) #Retorna a string centralizada
print(gameName.find("f"))
print(gameDescription.count('a')) #Conta quantos caracteres 
print(gameDescription.count('A')) #Conta quantos caracteres 
print(gameDescription.replace("Fifa", "Pes")) #Altera elementos
print(gameDescription.split(','))
