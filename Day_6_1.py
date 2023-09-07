email = input("Enter email to get username: ")
for i in email:
    if i != "@":
        print(i, end="")
    elif i == "@":
        break
