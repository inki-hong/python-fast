def cube(n):
    c = n * n * n
    return c


result = cube(5)
print(result)

for x in range(100, 110):
    result = cube(x)
    print(result)
