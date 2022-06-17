class Building:

    def __init__(self, name, windows, doors):
        self.name = name
        self.windows = windows
        self.doors = doors

class BeautySalonMixin:
    min_price = 10

    def manicure(self):
        pass

    def haircut(self, hair_length):
        pass

class BeautySalonRoom(Building, BeautySalonMixin):

    def __init__(self, floor, windows, doors):
        super().__init__(floor, windows, doors)
    
    def manicure(self):
        print(f"Manicure cost: {self.min_price + (self.min_price/100*20)} rubles.")

    def haircut(self, hair_length):
        if hair_length < 30:
            print(f"Haircut cost: {self.min_price + (self.min_price/100*20)} rubles.")
        elif 30 < hair_length < 50:
            print(f"Haircut cost: {self.min_price + (self.min_price/100*50)} rubles.")
        else:
            print(f"Haircut cost: {self.min_price + (self.min_price/100*80)} rubles.")

if __name__ == "__main__":
    bsr = BeautySalonRoom("Bane", 4, 6)
    print(bsr.__dict__)
    bsr.manicure()
    bsr.haircut(15)
    bsr.haircut(41)
    bsr.haircut(80)
