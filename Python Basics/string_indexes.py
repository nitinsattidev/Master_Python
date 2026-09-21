selfish = "me me me"

print(selfish)
print(selfish[0])  # Output: m

# [start:stop:stepover]
selfish = "01234567"
print(selfish[0:2])  # Output: me

print(selfish[1:])

print(selfish[:5])

print(selfish[-1])

print(selfish[::-1])

print(selfish[::-2])


# strings are immutable

selfish += "8"
print(selfish)
