'''
import random

def gen():
    a = int(input('n = '))
    list = [random.randint(0, 10) for _ in range(a)]
    return list

result = gen()


b = result[::-1]
result_2 = []
i = 0
while i < len(result):
    c = result[i] * b[i]
    result_2.append(c)
    result.pop()
    b.pop()
    i += 1
print(result_2)

n = int(input('n = '))
print(gen(n))
'''


a = 0
b = 1
c = 0
v = 1

for i in range(n):
    a, b = b, a + b
    result.append(a)

