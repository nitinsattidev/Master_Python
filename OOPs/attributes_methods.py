class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        if self.membership:  # or PlayerCharacter.membership
            self.name = name  # Attributes
            self.age = age

    def shout(self):
        print(f"my name is {self.name}")


player1 = PlayerCharacter("Nitin", 32)
player2 = PlayerCharacter("Yamini", 30)
player2.attack = 50

print(player1.membership)
print(player2.membership)

print(player1.shout())
