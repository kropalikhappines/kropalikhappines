from random import randint
import sys
import platform

lst_num = [randint(1, 99) for i in range(100)]
print(lst_num)


def func_min_num(lst):
    min_num = lst[0]

    for i in lst:
        if i < min_num:
            min_num = i
    return lst.index(min_num)


num_1 = lst_num.pop(func_min_num(lst_num))
num_2 = lst_num.pop(func_min_num(lst_num))
print(f'Минимальные числа {num_1, num_2}')

print(sys.getsizeof((lst_num)))
print(sys.getsizeof(lst_num[0]))
print(sys.getsizeof(tuple(lst_num)))

sum_size = 0
sum_size += sys.getsizeof(lst_num)
sum_size += sys.getsizeof(func_min_num)
sum_size += sys.getsizeof(num_1)
sum_size += sys.getsizeof(num_2)

print(f'Переменные на {sum_size}')
sum = 0
for i in lst_num:
    sum += sys.getsizeof(i)
print(f'Размер каждого элемента в листе в сумме {sum}')

print(sys.version)
print(sys.platform) # Почему-то определяет как win32, возможно он показывает разрядность питона
print(platform.architecture())
