def add_hash(string):
    list1 = [i for i in string]
    result = "#".join(list1)
    return result


def add_underscore(string):
    result = string.replace("#", "_")
    return result


def remove_underscore(string):
    result = string.replace("_", "")
    return result


print(remove_underscore(add_underscore(add_hash("harshil"))))