
from itertools import cycle, count

print('\nЗадание №6 \n************ итераторы *************')
end_of_cycle = 10
for el in count(3):
    print(el)
    if el == end_of_cycle:
        break

counter = 1
rh_list = ["раз", "два", "три", "четыре", "пять"]
for el in cycle(rh_list):
    print(el)
    # закончим вывод элементов после трёх проходов
    if counter == len(rh_list) * 3:
        break
    counter += 1
