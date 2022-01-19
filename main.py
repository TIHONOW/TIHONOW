while True:
    what=input("Что делаем? (+, -, /, *):")
    if what not in('+', '-', '/', '*'):
        exit('Неверная операция')
    input_value1 = float(input("Введите первое число = "));
    input_value2 = float(input("Введите второе число = "));
    if what == "+":
        solution = input_value1 + input_value2
    elif what == "-":
        solution = input_value1 - input_value2
    elif what == "/":
        if input_value2 == 0:
            print("Ошибка - деление на 0!")
        else:
            print(input_value1/input_value2)
    elif what == "*":
        solution = input_value1 * input_value2
        print(solution)