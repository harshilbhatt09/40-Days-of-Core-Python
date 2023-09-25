def same_in_reverse(name):
    if list(name) == list(name[::-1]):
        return True
    else:
        return False


print(same_in_reverse(input("Enter Name: ")))
