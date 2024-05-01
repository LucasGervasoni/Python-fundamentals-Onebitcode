from agendaDeContatos import adicionar, visualizar, deletar

def main():
    while True:
        print("\nMenu:")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Delete all contacts")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            adicionar()
        elif choice == "2":
            visualizar()
        elif choice == "3":
            deletar()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

main()