import sqlite3

#conectando o BD
connection = sqlite3.connect("title.bd")

#criando um cursor para interagir com o BD
cursor = connection.cursor()

#criar a tabela
cursor.execute('''
    CREATE TABLE movies(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        score REAL NOT NULL               
    );
    ''')

#fechando a conexão
print("Table criada com sucesso!")
connection.close()
