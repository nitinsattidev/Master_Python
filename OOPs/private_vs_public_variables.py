# Nothing actually provate in python but we can use _ in front of variable to let the programmer know that this private variable and don't change it


class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print("run")

    def speak(self):
        print(f"My name is {self._name} and I'm {self._age} years old!")


player1 = PlayerCharacter("Nitin", 32)
player1.speak()

######### Below lines of code can change the variables value after instantiating the class, this we don't do

player2 = PlayerCharacter("Yamini", 30)
player2.name = "Sati"
player2.speak = "!!!"

print(player2.name)
print(player2.speak)
