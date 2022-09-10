'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

list_a = [1.1, 1.2, 3.1, 5, 10.01, 2]
list_b = []
for i in list_a:
    if type(i) != int:
        c = i % int(i)
        list_b.append(c)
num_max = max(list_b)
num_min = min(list_b)
n = num_max - num_min
print(round(n, 2))



'''
num_max = max(list_a)
num_min = min(list_a)
n = num_max % int(num_max) - num_min % int(num_min)
print(round(n, 2))
'''