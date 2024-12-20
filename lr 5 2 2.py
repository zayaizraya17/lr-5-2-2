#инициализация для переменной
symbol =0 
#ввод с калвиатуры первой строки 
string_one=str(input("Введите  первую строку для проверки на анограмму "))
#убрать все пробелы
string_replace=string_one.replace(" ","")
#длина первой строки 
len_string_one=len(string_replace)
#ввод второй строки 
string_two=str(input("Введите вторую строку для проверки на анограмму "))
#цикл перебора символов второй строки 
for i in string_two:
#циклы проверки
 if i in string_replace:
  symbol +=1
if symbol==len_string_one:
#вывод ответов 
  print("Ваша строка анограмма")
else:
  print("Ваша строка не анограмма")