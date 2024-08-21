def summ(*args):
    total = 0

    for i in args:
        if type(i) == int:
            total += i
        if type(i) == str:
            total += len(i)
        if type(i) == dict:
            for key, value in i.items():
                if type(key) == int:
                    total += key
                elif type(key) == str:
                    total += len(key)
                if type(value) == int:
                    total += value
                elif type(value) == str:
                    total += len(value)
        if type(i) == tuple:
            for j in i:
                total += summ(j)
        if type(i) == set:
            for j in i:
                total += summ(j)
        if type(i) == list:
            for j in i:
                total += summ(j)

    return total  # Добавляем возврат суммы


# Пример данных
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = summ(*data_structure)
print(result)  # Ожидаемый результат: 101
