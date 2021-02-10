"""
Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
    1. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
       Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
       Внимание: использовать только арифметические операции! (грусть печаль)
    2. К каждому элементу списка добавить 17 и
       заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
    3* Решить задачу под пунктом 2, не создавая новый список.
"""
numbers = []    # объявляем рабочий список
summ1 = 0       # объявляем переменную для ответа на задание 1
summ2 = 0       # объявляем переменную для ответа на задание 2

for num in range(1, 1001, 2):   # генерим список кубов нечётных чисел 1-1000 включительно
    numbers.append(num ** 3)

print('\nПолученный список: ', numbers)

# решение задания 1
for num in numbers:     # проходим по числам из списка
    _num = num          # оставляем элемент списка в буфере, присваивая его значение временной переменной
    _sum_of_num = 0     # обнуляем сумму цифр в числе
    while _num > 0:                 # проходим по цифрам в числе накапливая их сумму
        _sum_of_num += _num % 10    # прибавляем последнюю цифру к сумме цифр
        _num //= 10                 # отбрасываем последнюю цифру от числа
    if _sum_of_num % 7 == 0:    # если сумма цифр числа делится на 7 без остатка
        summ1 += num            # то прибавляем число к ответу на задание 1

print('Ответ на задание 1:', summ1)


# решение задания 2 без изменения исходного списка
for num in numbers:     # проходим по числам из списка
    _num = num + 17     # оставляем элемент списка +17 в буфере, присваивая его значение временной переменной
    _sum_of_num = 0     # обнуляем сумму цифр в числе
    while _num > 0:                 # проходим по цифрам в числе накапливая их сумму
        _sum_of_num += _num % 10    # прибавляем последнюю цифру к сумме цифр
        _num //= 10                 # отбрасываем последнюю цифру от числа
    if _sum_of_num % 7 == 0:    # если сумма цифр числа делится на 7 без остатка
        summ2 += num + 17           # то прибавляем число к ответу на задание 1

print('\n\nОтвет на задание 2 без изменения исходного списка:', summ2)


# решение задания 2 с изменением исходного списка
summ2 = 0
for i, num in enumerate(numbers):   # прибавляем к каждому элементу списка 17
    numbers[i] = num + 17

for num in numbers:     # проходим по числам из списка
    _num = num          # оставляем элемент списка в буфере, присваивая его значение временной переменной
    _sum_of_num = 0     # обнуляем сумму цифр в числе
    while _num > 0:                 # проходим по цифрам в числе накапливая их сумму
        _sum_of_num += _num % 10    # прибавляем последнюю цифру к сумме цифр
        _num //= 10                 # отбрасываем последнюю цифру от числа
    if _sum_of_num % 7 == 0:    # если сумма цифр числа делится на 7 без остатка
        summ2 += num            # то прибавляем число к ответу на задание 1

print('\nИзменённый исходный список: ', numbers, '\nОтвет на задание 2 с изменением исходного списка:', summ2)
