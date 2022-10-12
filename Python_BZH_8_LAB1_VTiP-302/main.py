import math

try:  # Защищенный блок 1
    a = float(input("Введите A="))
    b = float(input("Введите B="))
    x = float(input("Введите x="))
    y = ''

    try:  # Защищенный блок 2
        if x >=6:
            y = 4 * (math.pow(a, 2) + 2*x + math.pow(b, 2))/(a*b)
        else:
            y = math.pow(x, 3) * (math.pow(a-b, 2))
        print("y=", y)

    except ZeroDivisionError:  # Обработчик ошибок для защищенного блока 1
        print("Нет решения!")
except:  # Обработчик ошибок для защищенного блока 2
        print("Неверные входные данные!")


