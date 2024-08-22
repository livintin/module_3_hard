def summ(*args):
    total = 0
    for i in args:
        if isinstance(i, int):
            total += i
        if isinstance(i, str):
            total += len(i)
        if isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, int):
                    total += key
                elif isinstance(key, str):
                    total += len(key)
                if isinstance(value, int):
                    total += value
                elif isinstance(value, str):
                    total += len(value)
        if isinstance(i, tuple):
            for j in i:
                total += summ(j)
        if isinstance(i, set):
            for j in i:
                total += summ(j)
        if isinstance(i, list):
            for j in i:
                total += summ(j)

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
