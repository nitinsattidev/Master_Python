# polymorphism means many forms


class User:
    def sign_in(self):
        print("logged")

    def attack(self):
        print("Do Nothing!")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        User.attack(self)
        print(f"Attacking with arrows: arrows left - {self.num_arrows}")


def player_attack(char):
    char.attack()


wizard1 = Wizard("Nitin", "Fighter")
archer1 = Archer("Yamini", 200)

player_attack(wizard1)
player_attack(archer1)
