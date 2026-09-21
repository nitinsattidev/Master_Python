# Logical Operator

print(4 > 5)

print("a" > "A")

print("a" > "b")

print(0 != 0)

print(0 <= 1)

print(not (True))


####################################################

is_magician = False
is_expert = False

# Check if magician and expert: "You are master magician"

if is_magician and is_expert:
    print("You are master magician")

# Check if magician but not expert: "Atleast you're getting there"

if is_magician and not is_expert:
    print("Atleast you're getting there")


# If you're not magician "You need Magic Powers"

if not is_magician and not is_expert:
    print("You need Magic Powers")


# Complete Program
if is_magician:
    if is_expert:
        print("You are master magician")
    else:
        print("Atleast you're getting there")
else:
    print("You need Magic Powers")
