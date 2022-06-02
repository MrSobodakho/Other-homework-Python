'''Hometask_13_1
Из полученного списка чисел создайте список с суммами этих чисел, отсортированными по возрастанию.

user_in = [i for i in input("Please enter numbers: ").split()]

def sum_digits(add_list):
    sum_list = []
    for i in add_list:
        sum_list.append(sum(map(int, i)))
    return sorted(sum_list)

print(f"Result: {sum_digits(user_in)}")'''

'''Hometask_13_2
Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:

while True: #для отсечения ошибок с символами без перезапуска программы
    try:
        user_in = float(input("Enter one number: "))
    except ValueError:
        print("You entered an invalid character! Please re-enter.")
    else:
        break

def calc_function (x):
    if x <= -2:
        return 1 - (x + 2)**2
    elif x > -2 and x <= 2:
        return - (x / 2)
    else:
        return (x - 2)**2 + 1

print(f"Answer: {calc_function(user_in)}")'''

'''Hometask_13_3
Напишите функцию которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а 
чётные нацело делит на два.

while True: #для отсечения ошибок с символами без перезапуска программы
    try:
        user_in = [int(i) for i in input("Please enter numbers: ").split()]
    except ValueError:
        print("You entered an invalid character! Please re-enter.")
    else:
        break

def list_editor (inc_list):
    return [int(i / 2) for i in user_in if not i % 2]

print(f"Result: {list_editor(user_in)}")'''