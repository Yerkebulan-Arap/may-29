user_input = input("Введите год: ")

try:
    leap_year = int(user_input)
except ValueError:
    print("Вы ввели не число!")
    
else:
    if leap_year % 400 == 0:
        print(leap_year, "Високосный год")
    elif leap_year % 4 == 0 and leap_year != 0:
        print(leap_year, "Високосный год")
    else:
        print(leap_year, "Не високосный год")