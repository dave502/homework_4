
print('\nЗадание №2 \n****** Список с бОльшими элементами *******')

digits_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for i, el in enumerate(digits_list) if (i > 0) & (digits_list[i] > digits_list[i - 1])]
print(new_list)
