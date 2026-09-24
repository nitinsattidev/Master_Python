class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f"Hello there, {self.name}")

    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter("Ram", 14)

print(player1.adding_things(5, 7).name)

# We can call this decorator function with instancating

print(PlayerCharacter.adding_things(7, 9).age)

player3 = PlayerCharacter.adding_things2(9, 8)

print(player3)

################################################################################
