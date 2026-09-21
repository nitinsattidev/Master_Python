name = input("Enter your name: ")
password = input("Enter your password: ")
length = len(password)
hidden_password = "*" * length

print(f"Hi {name}, your password is {hidden_password} is {length} letters long")
