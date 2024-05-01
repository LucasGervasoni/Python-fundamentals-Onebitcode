#Criando o Banco de Dados SQLite

import sqlite3

#criando o BD
connection = sqlite3.connect("title.bd")

#verifica se houve alterações na base de dados
print(connection.total_changes)