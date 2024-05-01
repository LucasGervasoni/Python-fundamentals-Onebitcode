import sqlite3

#conectando o BD
connection = sqlite3.connect("title.bd")

#criando um cursor para interagir com o BD
cursor = connection.cursor()

#solicitando dados pro usuário
name = input("Nome do filme\n")
year = int(input("Ano do filme\n"))
score = float(input("Nota do filme\n"))

#inserindo dados
cursor.execute("""
    INSERT INTO movies(name,year,score)
    VALUES(?, ?, ?)
                """,(name,year,score))

#gravando os dados no BD
connection.commit()
print("Dados inseridos com sucesso!")

#fechando conexão
connection.close()