print('Вы ввели не целочисленное значение для числа, если программа выдаст ошибку') # выводим на экран предупреждение о "Защите от дурака"
N = int(input("Ввведите число: ")) # создаём переменную N и присваем ей целочисленные значения в соответствии с вводимым через клавиатуру пользователя числом. 
def factorial(N): # задаём функцию факториала переменной N
    a = 1 # создаём переменную a и присваем ей значение 1, исходя из условий задачи
    numbers = [] # cоздаём числовую переменную, где полученные значения будут отображаться в квадратных скобках
    for i in range (1, N+1): # пока переменная i находится в диапозоне от 1 до N+1, то
     a = a * i # создаём переменную а и присваем ей произведение предыдущей переменной а * на переменную i
    numbers.append(a) # к числовой переменной добавляем переменную а
    return numbers # делаем повтор числовой переменной
print(f'набор произведений чисел от 1 до N {factorial(N)}') # Выводим результат решения задачи