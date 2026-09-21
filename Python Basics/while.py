# Here else statement won't run if there will be break statement, so this is the purpose of else statement with while --> to determine that loop fnishes completely wthout any break
i = 0


while i < 50:
    print(i)
    i += 1
else:
    print("Done with all the work")


while True:
    response = input("say something or exit: ")
    if response == "exit":
        break
