# Lista

#> As listas são usadas para armazenar vários itens em uma única variável, além disso, é importante ressaltar que na lista, utilizamos os colchetes.


gameData = ["Fifa23", 2022, 90.50, 8.5]
print(gameData)

gamesList = ["Fifa23", "Star Wars", "The Legend of Zelda", "Red Dead 2"]
print(gamesList)

# 1 - Busque os dois primeiros itens da lista
print(gamesList[0:2])

# 2 - Busque o último item da lista
print(gamesList[-1])

# 3 - Busca jogos até uma posição
print(gamesList[:2])

# 4 - Busca jogos de uma posição em diante
print(gamesList[2:])


#> Aprenderemos a recuperar um item da lista pelo seu índice, a adicionar e remover itens da lista, ordenar os valores de uma lista, etc.


gamesList = ["Fifa23", "Star Wars", "The Legend of Zelda", "Red Dead 2"]

# 1 - Tamanho da lista
print(len(gamesList))

# 2 - Recupera um item da lista pelo índice
print(gamesList.index("Star Wars"))

# 3 - Adiciona item ao final da lista
gamesList.append("Gta V")
print(gamesList)

# 4 - Ordena lista
gamesList.sort()
#listaJogos.reverse()
print(gamesList)

# 5 - Copia os itens de uma lista para outra
gamesReset = gamesList.copy()
gamesReset.remove('Fifa23')
gamesReset.remove('Star Wars')
print(gamesReset)

# 6 - Remove todos os itens da lista
gamesList.clear()
print(gamesList)
