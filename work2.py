user_input = input("Введите трехзначное число: ")

try:
    three_dig = int(user_input)
except ValueError:
    print("Ошибка! Вы ввели не число")
 
else:
    if three_dig % 10 == three_dig // 10 % 10 or three_dig % 10 == three_dig // 100 or three_dig // 10 % 10 == three_dig // 10:
        print("В числе есть одинаковые цифры")
    else:
        print("В числе нет одинаковых цифров")