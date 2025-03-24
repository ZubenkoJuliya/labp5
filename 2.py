def factorials(n):
    factorial = 1
    factorials_list = []
    for i in range(1, n + 1):
        if i == 0:
            factorials_list.append(factorial)
        else:
            factorial *= i
            factorials_list.append(factorial)
    return factorials_list


# Пример использования
n = 7
print(f"Факториалы от 1 до {n}:")
print(factorials(n))
