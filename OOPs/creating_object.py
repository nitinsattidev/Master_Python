class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def run(self):
        return "run"


player1 = PlayerCharacter("Nitin", 32)
player2 = PlayerCharacter("Yamini", 30)

print(player1.name, player1.age)
print(player1.run())
print(player2.name, player2.age)
print(player2.run())
