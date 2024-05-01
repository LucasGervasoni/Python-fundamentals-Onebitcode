import sqlite3

#conectando o BD
connection = sqlite3.connect("title.bd")

#criando um cursor para interagir com o BD
cursor = connection.cursor()

#lendo dados da tabela
data = cursor.execute("""
    SELECT name, year, score FROM movies
                    """)

print(data.fetchall())

#iterando os dados
for row in cursor.execute("SELECT * FROM movies"):
    print(f"{row}")

#ordenando os dados pelo score
for row in cursor.execute("SELECT * FROM movies ORDER BY score desc"):
    print(f"{row}")

#fechando conexão
connection.close()