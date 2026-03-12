import secrets
alf = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@#$_&-+()/*:;!?,.~`"
try:
    L = int(input("Длина (4-150):"))
    if L < 4 or L > 150:
        print("Ошибка: длина должна быть от 4 до 150!")
    else:
        password = "".join(secrets.choice(alf) for _ in range(L))
        print(f"Пароль: {password}")
except ValueError:
    print("Ошибка: введите целое число!")
except KeyboardInterrupt:
    print("\nОстановлено!")
