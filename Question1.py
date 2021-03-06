"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
    1. до минуты: <s> сек;
    2. до часа: <m> мин <s> сек;
    3. до суток: <h> час <m> мин <s> сек;
    4. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""
_duration = ''                                  # объявляем переменную времени для нормального запуска цикла
max_duration_list = [60, 60, 24]                # описываем макс количества сек мин ч
duration_list = []                              # объявляем список для получения в него количеств сек мин ч д
duration_str = [' сек.', ' мин ', ' час ', ' дн ']  # подписи для единиц измерения
output_duration = ''                            # переменная для вывода полученного отрезка времени

while not _duration.isdigit():   # проверяем чтобы переменная была числовой
    _duration = input('Введите время в секундах: ')  # просим ввод переменной, пока она не станет числовой
else:
    duration = int(_duration)    # после получения числовой переменной преобразовываем ее в число

for i in range(3):  # пробегаем по списку единиц времени
    duration_list.append(duration % max_duration_list[i])   # забираем остаток от деления на макс количество единиц
    duration = duration // max_duration_list[i]             # переводим время в следующую единицу измерения

duration_list.append(duration)  # добавляем к списку дни

for i, t in enumerate(duration_list):   # проходим по спискам подписей и полученного списка собирая данные в кучу
    output_duration = str(t) + duration_str[i] + output_duration if t > 0 else output_duration  # если t = 0 пропускаем

print(output_duration)
