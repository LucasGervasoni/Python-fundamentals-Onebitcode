# def

#> É uma maneira de se criar função.


def wellcome():
    print("Hello World")

def create_game():
    name = input("Digite o nome do jogo \n")
    yearLaunch = int(input("Digite o ano de lançamento\n"))
    gamePrice = float(input("Digite o preço do jogo\n"))
    noteRating = float(input("Digite a nota de avaliação do jogo\n"))
    print(name)
    print(yearLaunch)
    print(gamePrice)
    print(noteRating)

wellcome()
create_game()


#> Utilizar funções pode ser uma boa opção a fim de reaproveitar a execução de blocos sem a necessidade de duplicação de código. E utilizar funções com argumentos, torna ainda mais dinâmica a sua utilização.


def full_name(fname, lname):
    print(f"{fname} {lname}")

def sum(a, b):
    print(a + b)

def address(country="Brasil"):
    print(f"Eu moro no {country}")

full_name("Rodrigo", "Macedo")
sum(20, 10)
address()
address("Canadá")

def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo \n"))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum/qtdRating}")

rating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))
rating_game(rating)
