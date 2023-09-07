def count_dots(string1):
    count = 0
    for i in string1:
        if i == ".":
            count += 1
    return count


print(count_dots("h.e.t.v.i"))
