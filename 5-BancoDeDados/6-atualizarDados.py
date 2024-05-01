import sqlite3

#conectando o BD
connection = sqlite3.connect("title.bd")

#criando um cursor para interagir com o BD
cursor = connection.cursor()

#solicitando dados do usuário
id = int(input("Informe o id do filme\n"))
name = input("Informe o nome do filme\n")

#atualizando os dados
cursor.execute("""
    UPDATE movies set name = ?
    WHERE id = ?
                """,(name,id))
connection.commit()
print('Dados atualizados com sucesso.')

#fechando conexão
connection.close()