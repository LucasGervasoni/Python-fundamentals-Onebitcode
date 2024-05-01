from agendaDeContatos import Contact
from agendaDeContatos import ContactBook

contact_book = ContactBook()

while True:
    print("\n--- Opções Agenda de Contatos ---")
    print("1. Adicionar Contato")
    print("2. Remover Contato")
    print("3. Listar Contatos")
    print("4. Buscar Contato")
    print("5. Sair")

    choice = input("Escolha a opção: ")

    if choice == "1":
        name = input("Informe o nome: ")
        phone = input("Informe o telefone: ")
        email = input("Informe o e-mail: ")
        contact = Contact(name, phone, email)
        contact_book.add_contacts(contact)
        print("Contato adicionado com sucesso.")
    elif choice == "2":
        name = input("Informe o nome para remover: ")
        contact = contact_book.search_contacts(name)
        if contact:
            contact_book.remove_contacts(contact)
            print("Contato removido com sucesso.")
    elif choice == "3":
        contact_book.display_contacts()
    elif choice == "4":
        name = input("Procure por um nome: ")
        contact_book.search_contacts(name)
    elif choice == "5":
        print("Saindo do programa.")
        break
    else:
        print("Opção Inválida. Utilize uma opção de 1 a 5")