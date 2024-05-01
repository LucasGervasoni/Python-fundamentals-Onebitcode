class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"

class ContactBook(Contact):
    def __init__(self):
        self.contacts = []
    
    def add_contacts(self, contact):
        self.contacts.append(contact)
    
    def remove_contacts(self, contact):
        self.contacts.remove(contact)
    
    def display_contacts(self):
        if not self.contacts:
            print("Lista de Conatatos vazia.")
        else:
            for contact in self.contacts:
                print(contact)
                print("----------------------")
    
    def search_contacts(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return
            print("Contato não encontrado")