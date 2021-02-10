from sys import argv

print('\nЗадание №1 \n************* Расчет зарплаты *************')


def salary_calc(working_hours, hour_cost, add_bonus):
    """Salary calculation

    :param working_hours: float
    :param hour_cost: float
    :param add_bonus: float
    :return: float
    """
    return working_hours * hour_cost + add_bonus


# если были переданы параметры - выполнить функцию расчет зарплаты
if len(argv) > 1:
    hours, cost, bonus = argv[1:4]
    print(salary_calc(float(hours), float(cost), float(bonus)))
