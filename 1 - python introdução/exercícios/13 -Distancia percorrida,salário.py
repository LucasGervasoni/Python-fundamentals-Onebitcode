distancia = float(input('Qual a distância que você deseja percorrer? '))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.35
  
print(f"Você irá percorrer {distancia}Km e gastará R${preco:.2f}")

salario = float(input("Digite o valor do seu salário: "))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
  
total = salario + aumento

print(f"O seu salário de R${salario:.2f} teve um aumento de {aumento:.2f} e passou a ser R${total}")