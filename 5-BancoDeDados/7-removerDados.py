import sqlite3

#conectando o BD
connection = sqlite3.connect("title.bd")

#criando um cursor para interagir com o BD
cursor = connection.cursor()

# solicitando dados pro usuário
id = int(input("Informe o id do filme\n"))

#removendo dados
cursor.execute("""
    DELETE FROM movies 
    WHERE id = ?
            """,(id,))

connection.commit()
print('Filme removido com sucesso.')

#fechando conexão
connection.close()