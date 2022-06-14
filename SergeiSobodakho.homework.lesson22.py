class Pet:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def run(self, km_h):
        print(f"{self.name} runs at a speed of {km_h} km/h.")

    def jump(self, m):
        print(f"{self.name} jumps {m} meters high.")
    
    def birthday(self):
        print (f"{self.name} {self.age + 1} years old")

    def sleep(self, h):
        print(f"{self.name} sleeps {h} hours a day.")

class Dog(Pet):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)

    def bark(self, dB):
        print(f"{self.name} barking - {dB} dB")

class Cat(Pet):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)

    def meow(self, MpM):
        print(f"{self.name} creates {MpM} meows per minute")

class Parrot(Pet):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)

    def fly(self, BpM):
        print(f"{self.name} {BpM} wing beats per minute.")

if __name__ == "__main__":
    pooch = Dog("Luna", 2.3, 6.5)
    print(f"Description of the dog: {pooch.__dict__}")
    pooch.run(10) 
    pooch.jump(1.5)
    pooch.birthday()
    pooch.sleep(8)
    pooch.bark(70)

    british = Cat("Stelsi", 3, 3.2)
    print(f"\nDescription of the cat: {british.__dict__}")
    british.run(5) 
    british.jump(0.8)
    british.birthday()
    british.sleep(24)
    british.meow(30)

    cockatoo = Parrot("Gosha", 1, 1.2)
    print(f"\nDescription of the parrot: {cockatoo.__dict__}")
    cockatoo.run(0.2) 
    cockatoo.birthday()
    cockatoo.sleep(18)
    cockatoo.fly(28)