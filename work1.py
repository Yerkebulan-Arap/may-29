user_input = input("Введите число от 0 до 9: ")

try:
    letter = int(user_input)
except ValueError:
    print("Ошибка вы ввели не число!")
    
else:
    if letter == 1:
        print("!")
    elif letter == 2:
        print("@")
    elif letter == 3:
        print("#")
    elif letter == 4:
        print("$")
    elif letter == 5:
        print("%")
    elif letter == 6:
        print("^")
    elif letter == 7:
        print("&")
    elif letter == 8:
        print("*")
    elif letter == 9:
        print("(")
    elif letter == 0:
        print(")")
    else:
        print("Вы ввели другое число")

finally:
    print("Попробуйте еще раз!")
