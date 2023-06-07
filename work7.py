user_input = input("Введите радиус окружности: ")
user_input_per = input("Введите периметр квадрата: ")

try:
    radius_circ = int(user_input)
    perimeter_sq = int(user_input_per)
except:
    print("Ошибка! Введите число")
    
else:
    circum_fer = 2 * 3.14 * radius_circ  #C = 2*pi*r
    if circum_fer <= perimeter_sq:
        print("Такая окружность поместиться в указанный квадрат")
    else:
        print("Такая окружность не поместиться в указанный квадрат")