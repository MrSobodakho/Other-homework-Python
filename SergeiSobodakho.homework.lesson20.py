'''Hometask_13_4
Напишите функцию, которая создает список случайных элементов. На фход функция принимает кол-во элементов, 
минимальное и максимальное значение

from random import randint
user_in = tuple(map(int, input("Enter the number of items and their minimum and maximum values: ").split()))
            # т.к. по задаче входные данные вносятся кортежем?
def new_list(amount_elem, min_value, max_value):
    return list(map(lambda my_list: randint(min_value, max_value), range(amount_elem)))
print(new_list(*user_in))'''

'''Hometask_13_6
Напишите функцию, вычисляющую значение факториала числа N. Используйте рекурсию.

user_in = int(input("Enter the number: "))

def factorial(n):
    if n <= 1:
        return 1
    else:
        return (n * factorial(n-1))

print(f"The factorial of a number is: {factorial(user_in)}")'''

'''Hometask_13_11
Напишите декоратор к функции деления, который меняет местами делимое и делитель.
user_in = list(map(int, input("Enter two numbers: ").split()))

def new_decorator(division_function):
    def my_revers(num1, num2):
        return num2 / num1
    return my_revers

@new_decorator
def div(num1, num2):
    return num1 / num2

print(div(*user_in))'''


