class PlayerCharacter:
    # Class Object Attribute
    memberhip = True

    def __init__(self, name="anonymous", age=0):

        if age > 18:
            self.age = age
            self.name = name

    def shout(self):
        print(f"my name is {self.name}")


Player1 = PlayerCharacter("Tom", 10)

print(Player1.shout())

# You will get error
