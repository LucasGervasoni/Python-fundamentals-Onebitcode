class Animal:
    name = ''
    size = ''
    color = ''

    def eat(self):
        print("Animal se alimentando")

class Horse(Animal):
    race = ''

    def escape(self):
        print("Animal fugindo")

class Lion(Animal):
    mane = True

    def hunt(self):
        print("Animal caçando")


h = Horse()
h.name = 'Frederico'
h.color = 'branco'
h.escape()
h.eat()

l = Lion()
l.name = 'mufasa'
l.color = 'marrom'
l.hunt()
l.eat()