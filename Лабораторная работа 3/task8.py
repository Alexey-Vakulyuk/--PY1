money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
budget = money_capital  # общий бюджет

while budget >= spend:
    month += 1  # прожили еще 1 месяц
    budget += salary  # получили зарплату
    budget -= ((1+increase)**month) * spend  # потратились

print(month)
