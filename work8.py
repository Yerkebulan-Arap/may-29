user_input_1 = input("Столица Англии? A. Париж B. Берлин C. Лондон: ")
user_input_2 = input("Сколько полос на флаге США? A. 12 B. 13 C. 15: ")
user_input_3 = input("Какая валюта Дании? A. Евро B. Крон C. Франк: ")

try:
    question_1 = str(user_input_1)
    question_2 = int(user_input_2)
    question_3 = str(user_input_3)
except:
    print("Ошибка! Ответьте на вопрос")
else:
    if question_1 == "Лондон":
        right_1 = 2
    else:
        right_1 = 0
    if question_2 == 13:
        right_2 = 2
    else:
        right_2 = 0
    if question_3 == "Крон":
        right_3 = 2
    else:
        right_3 = 0
    total = right_1+right_2+right_3  
    
print("Вы набрали: ", total, "баллов")