user_input = input("Введите сумму покупку: ")

try:
    sum = int(user_input)
except ValueError:
    print("Ошибка! Введите сумму")

else:
    if 200 <= sum < 300:
        print("Скидка 3%", sum*3/100)
    elif 300 <= sum < 500:
        print("Скидка 5%", sum*5/100)
    elif 500 <= sum:
        print("Скидка 7%", sum*7/100)
    else:
        print("Скидки нет")
    