# Object Oriented Programming

'''

- OOP allows users to create their own objects
- Creates code that is repeatable and organized

'''

'''
class NameOfClass():
    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        # perform some action
        print(self.param1)
'''

'''
# class = user defined object; uses CamelCase

class Sample():
    pass
my_sample = Sample() #type(my_sample) = __main__.sample

'''

'''
class Dog():
    def __init__(self, breed): # self = instance of object
        - Attributes
        - Take in Argument
        - Assigns it using self.attribute_name
        self.breed = breed

#my_dog = Dog(breed = 'Lab')
'''

# Class Object Attributes and Methods
'''
class Dog():

    # Class Object Attribute
    # Same for any instance of class

    species = 'mammal'

    def __init__(self, breed, name): # self = instance of object
        - Attributes
        - Take in Argument
        - Assigns it using self.attribute_name
        self.breed = breed
        self.name = name

# my_dog = Dog(breed = 'Lab')

# Operations/Actions --> Methods
def bark(self):
    print('WOOF! my name is {}'.format(self.name))

my_dog.bark()
# "WOOF!"
'''

#Inheritance & Polymorphism

# Inheritance
'''
class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a dog!")

mydog = Dog
 # ANIMAL CREATED
 # Dog Created
mydog.eat()
 # I am eating
myanimal = Animal()
my.who_am_i()
 # I am a dog!
'''

# Polymorphism
'''
class Dog():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"

class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"

niko = Dog("Niko")
felix = Cat("Felix")

print(niko.speak())
# Niko says woof!
print(felix.speak())
# Felix says meow!

for pet in [niko,felix]:
    print(type(pet))
    print((pet.speak()))

def pet_speak(pet):
    print(pet.speak())
'''
