
try:
    word = str(input("Введите слово: "))
except Exception:
    print("Ошибка!")
    
else:
    if len(word) !=5:
        print("Слово должно состоять из пяти букв")
    elif word == word[::-1]:
        print("Да, это слово палиндром")
    else:
        print("Нет, это слово не палиндром")
    