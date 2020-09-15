

text = 'Не знаю, как там в Лондоне, я не была. Может, там собака - это друг человека. А у нас управдом - друг человека!'

#count the number of digits
ltrnum = str(len(text))
print ('1. Количество символов ', ltrnum)

#reverse the string
rvrsdtext = text[::-1]
print ('2. Развернутая строка: ', rvrsdtext)

#capitalise every word
print('3. Сделать каждое слово с большой буквы: ', text.title())

#capitalise the whole string
print('4. Сделать весь текст просисными буквами: ',text.upper())

#find a quantity of "нд", "ам", "о" in the string
ndnum = 'Количество нд: ', text.count("нд")
amnum = 'Количество ам: ', text.count("ам")
onum = 'Количество о: ', text.count("о")
print('5. Найти число вхождений "нд", "ам", "о" в строку: ',ndnum, amnum, onum)

#my own exercises
char = input('Вставьте любое слово: ')
print(text.replace('друг', char))

lowercasetxt = text.casefold() 
print('Is the text string in lower case? ', lowercasetxt.islower())