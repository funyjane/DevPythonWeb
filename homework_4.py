
#сорри за обильное количество бесполезных комментариев в программе, это пока для себя, чтобы лучше визуализировать логику программы


#вводим переменные

var_1 = input('Введите первое значение: ')
var_2 = input('Введите второе значение: ')
var_3 = input('Введите третье значение: ')

#помещаем их в лист в форме int
list_of_vars = [int(var_1), int(var_2), int(var_3)]

#1. Вывести на экран 0, не если нет ни одного нуля - вывести: "Нет нулевых значений!!!" (без if)
result1 =  list_of_vars[0] and list_of_vars[1] and list_of_vars[2] and "Нет нулевых значений!!!"
print(result1)

#2. Вывести первое ненулевое значение,но если введены все нули - вывести "Введены все нули!" (без if)
result2 =  list_of_vars[0] or list_of_vars[1] or list_of_vars[2] or "Введены все нули!!!"
print(result2)

#3. Если первое значение больше чем сумма второго и третьего вывести a - b - c (п3 и п4 проверить одним условием(конструкцией)
if list_of_vars[0] > (list_of_vars[1] + list_of_vars[2]):
    x = list_of_vars[0] - list_of_vars[1] - list_of_vars[2]
    print(x)
elif list_of_vars[0] <= (list_of_vars[1] + list_of_vars[2]): #4. Если первое значение меньше или равно сумме второго и третьего вывести b + c - a   
    x_1 = list_of_vars[1] + list_of_vars[2] - list_of_vars[0]
    print(x_1)

#5. Если первое значение больше 50 и при этом одно из оставшихся значений больше первого вывести "Вася" (проверить одним условием)   
if list_of_vars[0] > 50 and list_of_vars[1] > list_of_vars[0] or list_of_vars[2] > list_of_vars[0]:
    print('Уася')    
elif list_of_vars[0] > 5 or (list_of_vars[1] == 7 and list_of_vars[2] == 7): #6. Если первое значение больше 5 или оба из оставшихся значений равны 7 вывести "Петя"
    print('Петя')