# if / else


name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Informe o ano de lançamento do jogo\n"))
classification = float(input("Informe a nota de classificação do jogo\n"))

if classification > 8.0:
    print(f"O jogo {name} é bom. Recomendo jogá-lo.")
else:
    print(f"O jogo {name} ainda não atingiu uma boa nota, por isso não recomendo.")

a = 20
b = 30

if a != b:
    print("Os números são diferentes.")
else:
    print("Os números são iguais.")


# if / else / elif


# Calculadora Python
num1 = float(input("Digite o número 1\n"))
num2 = float(input("Digite o número 2\n"))
operation = input("Digite a operação a realizar (+ - * /)\n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Operação inválida")
    result = 0
print(f"Resultado: {result}")


