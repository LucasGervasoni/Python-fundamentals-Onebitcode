# Dicionário

#> Os dicionários são usados para armazenar valores de dados em pares chave: valor. Além disso, é importante ressaltar que no dicionário, utilizamos as chaves. A sintaxe lembra muito à linguagem de formatação de dados Json.


gameFifa = {
    "price": 90.55,
    "yearLaunch": 2022,
    "version": 2023,
    "classification": 8.5,
    "genre": ["esporte", "família"]
}
print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Recuperando um elemento do dicionário
print(gameFifa['genre'])
print(gameFifa.get('classification'))

# 2 - Buscando apenas as chaves
print(gameFifa.keys())

# 3 - Buscando apenas os valores
print(gameFifa.values())

# 4 - Retorna itens do dicionário como tupla de uma lista 
print(gameFifa.items())

# 5 - Adicionando itens no dicionário
gameFifa["players"] = 2
print(gameFifa)

# 6 - Atualizando itens no dicionário
gameFifa.update({"players": 1})
print(gameFifa)

# 7 - Removendo item no dicionário
gameFifa.pop("players")
print(gameFifa)


# Dicionários Aninhados



import pprint 
gamesDict = {
  "fifa 23" : {
    "yearLaunch" : 2022,
    "classification" : 8.5,
    "genre": ["esporte", "família"]
  },
  "mario odyssey" : {
    "yearLaunch" : 2017,
    "classification" : 10.0,
    "genre": ["aventura", "3d"]
  },
  "donkey kong country" : {
    "yearLaunch" : 1996,
    "classification" : 9.5,
    "genre": ["aventura", "plataforma"]
  }
}
#print(dictJogos)
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Buscando informação dentro de um dicionário
print(gamesDict["mario odyssey"]["genre"])

# 2 - Adicionando novo item
gamesDict["mario odyssey"]["players"] = 1
print(gamesDict['mario odyssey'])

# 3 - Excluindo um dicionário
del gamesDict["fifa 23"]
pp.pprint(gamesDict)


