salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
count = 0
money_capital = 0
spend_all = 0
salary_all = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
while count < months:
    salary_all += salary
    spend_all += spend
    spend = spend * (1 + increase)
    count += 1
money_capital = spend_all - salary_all
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
