'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
'''

n = int(input('введите число = '))
a = 0
b = 1
c = 0
v = 1
result = []
result_1 = []
for i in range(n):
    a, b = b, a + b
    result.append(a)
for i in range(n):
    c, v = v, c - v
    result_1.append(c)
result_3 = result_1 + result
print(result_3)




