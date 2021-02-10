from functools import reduce

print('\nЗадание №5 \n************ reduce *************')
# получаем список четных чисел от 100 до 1000
list_100_1000 = [el for el in range(100, 1001) if el % 2 == 0]
# выводим произведение всех чисел списка
print(reduce(lambda x, y: x * y, list_100_1000))
