def equal_strings(a, b):
    if "".join(sorted(a)) == "".join(sorted(b)):
        return True
    else:
        return False


print(equal_strings("love", "evol"))
