a = [1, 1, 2, 3, 5, 8, 9, 2, 4, 6, 8, 0, 18, 20, 25, 30, 36]
# 1
print(list(filter(lambda x: x < 5, a)))

# 2
print(list(map(lambda x: x / 2, a)))

# 3
print(list(map(lambda x: x / 2, filter(lambda x: x > 17, a))))

# 4
print(sum(map(lambda x: x ** 2, filter(lambda x: x % 9 == 0, a))))
