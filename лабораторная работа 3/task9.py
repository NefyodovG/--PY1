salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
month = 10
up = 1.03
difference = salary - spend
need_money = 0
for money in range(1, months +1):
    money = spend +- salary
    spend = spend * up
    need_money += money

print(round(need_money))
