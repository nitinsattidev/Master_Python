# Users


class User:
    def sign_in(self):
        print("logged")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: arrows left - {self.num_arrows}")


wizard1 = Wizard("Nitin", "Crusher")

wizard1.sign_in()
print(wizard1.name)
wizard1.attack()

archer1 = Archer("Yamini", 100)
archer1.attack()
