import sqlite3

#conectando o BD
connection = sqlite3.connect("title.bd")

#criando um cursor para interagir com o BD
cursor = connection.cursor()

#inserir os dados
cursor.execute("""
    INSERT INTO movies(name,year,score)
    VALUES('Super Mario Bros', 2023, 10)
                """)

cursor.execute("""
    INSERT INTO movies(name,year,score)
    VALUES('Avatar', 2023, 9.5)
                """)

cursor.execute("""
    INSERT INTO movies(name,year,score)
    VALUES('Velozes e Furiosos 10', 2023, 8.6)
                """)

#gravando os dados no BD
connection.commit()
print("Dados inseridos com sucesso!")

#fechando conexão
connection.close()