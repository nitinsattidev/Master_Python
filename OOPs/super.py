class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)  #  or we can use super().__init__(email)
        self.name = name
        self.power = power

    def profile(self):
        print(
            f"My name is {self.name}, power is {self.power} and email address is {self.email} "
        )


wizard1 = Wizard("Nitin", "Fire", "nitin@gmail.com")
wizard1.profile()
