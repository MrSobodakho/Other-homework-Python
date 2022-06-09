'''Hometask_14_1
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Класс 
имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран. 
Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его  атрибуты. 

Hometask_14_2
Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет 
атрибут имени у объекта. Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя'''

class Dog:
    '''Создание описания и характеристик собаки'''
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self, m):
        print(f"{self.name} jumps {m} meters high.")

    def run(self, km_h):
        print(f"{self.name} runs at a speed of {km_h} km/h.")

    def bark(self, dB):
        print(f"{self.name} barking - {dB} dB")
    
    def change_name(self, new_name):
        self.name = new_name
        return self.name

if __name__ == "__main__":
    pooch = Dog(0.5, 9, "Tod", 1.5)
    print(f"Description of the dog: {pooch.__dict__}")
    pooch.run(10) 
    pooch.jump(1.5)
    pooch.bark(70) 

if __name__ == "__main__":
    hound = Dog(1.1, 23, "Avalon", 2.6)
    print(f"\nDescription of the dog: {hound.__dict__}")
    print(f"New dog name: {hound.change_name('Devil')}") 
