print('\nЗадание №4 \n****** элементы без повторений *******')

digits_list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_digits_list_1 = [el for el in digits_list_1 if digits_list_1.count(el) == 1]
print(new_digits_list_1)
