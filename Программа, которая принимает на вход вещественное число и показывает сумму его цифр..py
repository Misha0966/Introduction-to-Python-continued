#6782 -> 23
#0,56 -> 11

print('Вы ввели не число, если сумма окажется = 0') # выводим на экран предупреждение о "Защите от дурака"
number = input("Введите число : ") # создаём перменную для числа = значению, которое вводит с клавиатуры пользователь.
result = 0 # создаём переменную для резулата и присваем ей значение 0, для последущего счётчика 
for i in number: # пока переменная i находится в числом диапозоне, делаем следующее условие:
    if i.isdigit(): # если в переменной i все символы в строке являются цифрами, то  
        result = result+int(i) # результат = предыдующему результату + целочисленное значение переменной i, так как результат сложения из условий задачи всегда целочисленное значение,
print(f"Сумма цифр введенного числа {number} равняется: {result}") # Выводим сообщение о результате решения задачи