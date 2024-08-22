def summ(*args):
    total = 0
    for i in args:
        if isinstance(i, int):
            total += i
        if isinstance(i, str):
            total += len(i)
        if isinstance(i, dict):
            total += summ(*i.items())
        if isinstance(i, tuple):
            total += summ(*i)
        if isinstance(i, set):
            total += summ(*i)
        if isinstance(i, list):
            total += summ(*i)

    return total


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = summ(*data_structure)
print(result)
