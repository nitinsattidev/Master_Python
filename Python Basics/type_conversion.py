from datetime import date

birth_year = input("What is your birther year?")

current_year = date.today().year

print(f"current year is: {current_year}")
print(f"Your age is:{current_year - int(birth_year)}")
