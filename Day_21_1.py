def make_tuples(a, b):
    result = [(a[i], b[j]) for i in range(len(a)) for j in range(len(b)) if j == i]
    return result


print(make_tuples([1, 2, 3, 4], [5, 6, 7, 8]))
