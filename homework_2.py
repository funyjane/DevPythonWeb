
print("Калькулятор массы тела by Danila Stasiuk ver 0.111 \n")

#вводим переменные 
weight = int(input('Пожалуйста, введите ваш вес (В кг): '))
height = float(input('Теперь введите ваш рост (в метрах) : '))

#высчитываем индекс массы тела
bmi = round(weight/(height**2), 2)
print("\nВаш индекс массы тела: ", bmi)

#создаем шкалу
a = int((int(bmi) - 20)/2)
b = int((60 - int(bmi))/2)
scale = '20' + ('='* int(a)) + 'I' + ('=' * int(b)) + '60'

#выводим шкалу
print(scale)

