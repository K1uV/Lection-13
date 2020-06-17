class Animal():
    def talk(self):
        print('Talkkkkkkkkkkkkkkkkkkkkkkkk')

class Dog(Animal):
    def talk(self):
        print('Wooof wooof')

class Cat(Animal):
    def talk(self):
        print('Meow meow')

animals = Animal()
animals.talk()

dogs = Dog()
dogs.talk()

cats = Cat()
cats.talk()