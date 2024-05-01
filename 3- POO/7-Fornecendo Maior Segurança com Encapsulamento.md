# Fornecendo Maior Segurança com Encapsulamento

A analogia mais simples de entender o encapsulamento, é um remédio de cápsula. O essencial do remédio é o que está protegido dentro da cápsula, para que aquele conteúdo não seja alterado.

E trazendo para a orientação a objetos, o nosso objetivo é proteger o acesso aos atributos, possibilitando o acesso a leitura ou escrita destes atributos, somente via métodos.

'''python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    # Aplicando o Encapsulamento    
        #self.__salary = salary
    def show(self):
        # accessing public data member
        print(f"Nome: {self.name} Salário: {self.salary}")
        
fulano = Employee("Fulano", 4000)
sicrano = Employee("Sicrano", 10000)
fulano.name = "Fulano 2"
fulano.salary = 40000
fulano.show()
sicrano.show()
'''

Note que no nosso projeto, nós estamos conseguindo modificar tranquilamente todos os atributos, inclusive o atributo salário. Só que isso, não seria uma boa escolha, não é verdade? 

Para resolver essa questão, podemos tornar esse atributo como privado.

'''python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def show(self):
        # accessing public data member
        print(f"Nome: {self.name} Salário: {self.__salary}")
        
fulano = Employee("Fulano", 4000)
sicrano = Employee("Sicrano", 10000)
fulano.name = "Fulano 2"
fulano.__salary = 40000
fulano.show()
sicrano.show()
'''