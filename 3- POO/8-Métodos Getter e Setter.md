# Métodos Getter e Setter

Bem, na última aula nós vimos que conseguimos controlar a privacidade do atributo salário. Mas será que não existe nenhuma forma para acessar e modificar esse atributo?

Sim, existe. Não diretamente, como vimos. Mas podemos alterar por meio de métodos. Lembra da premissa do encapsulamento: **proteja os atributos e controle o acesso e valores deles por meio de atributos.**

Pensando nisso, temos os métodos getter e setter. O método getter é utilizado para retornar valores de atributos e o método setter é utilizado para modificar valores de atributos.

'''python
class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def show(self):
        # accessing public data member
        print(f"Nome: {self.name} Salário: {self.__salary}")
  
       # getter method
    def get_salary(self):
        return self.__salary

    # setter method
    def set_salary(self, salary):
        self.__salary = salary
        
fulano = Employee("Fulano", 4000)
sicrano = Employee("Sicrano", 10000)
fulano.name = "Fulano 2"
fulano.set_salary(40000)
fulano.show()
sicrano.show()
'''