import os

def adicionar():
    name = input("Informe o Nome: \n")
    address = input("Informe o Endereço: \n")
    phone = input("Informe o Telefone: \n")
    
    contact = f"Nome: {name}\nEndereço: {address}\nTelefone: {phone}\n"
    
    with open("contacts.txt", "a", encoding="utf-8") as file:
        file.write(contact)
    
    print("Contato adicionado com sucesso!")

def visualizar():

    if not os.path.exists("contacts.txt"):
        print("Lista de contatos está vazia.")
        return
    
    with open("contacts.txt", "r", encoding="utf-8") as file:
        contacts = file.read()
    
    print("Address Book:")
    print(contacts)

def deletar():
    if not os.path.exists("contacts.txt"):
        print("Lista de Contatos está vazia.")
        return
    
    with open("contacts.txt", "w") as file:
        file.write("")
    
    print("Contatos excluídos com sucesso!")