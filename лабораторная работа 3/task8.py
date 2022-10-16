money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0
up = 1.05
difference = salary - spend
while money_capital + difference >= spend :
    money_capital += difference
    spend = spend * up
    month += 1
print (month)



