
print('\nЗадание №7 \n********** yield factorial ***********')


# генератор факториала
def fact(x):
    res_fact = 1
    for i in range(1, x + 1):
        res_fact = i * res_fact
        yield res_fact


for el in fact(4):
    print(el)
