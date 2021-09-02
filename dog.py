class Dog:
    '''创建DOG类'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(f'{self.name} sits down.')
    def roll_over(self):
        print(f'{self.name} rolls over.')


my_dog = Dog('leeyu', 2)
print(f'my dog\'s name is {my_dog.name}')
print(f'my dog\'s age is {my_dog.age} years old.')
my_dog.sit()
my_dog.roll_over()


your_dog = Dog('yuli',6)
print(f'\nyour dog\'s name is {your_dog.name}, and it\'s {your_dog.age} years old.')
your_dog.roll_over()