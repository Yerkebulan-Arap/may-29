user_input = input("Вводите количество сумму USD: ")
currency = input("Выберите валюту: ")

try:
    sum = int(user_input)
except ValueError:
    print("Ошибка! Введите сумму")

else:
    if currency == "EUR":
        print(sum*0.93519, "евро")
    elif currency == "UAH":
        print(sum*36.92, "гривен")
    elif currency == "AZN":
        print(sum*1.7, "манат")
    else:
        print("Такая валюта недоступна")