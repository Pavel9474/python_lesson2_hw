#  Напишите программу, которая принимает на вход число
#   N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
number=int(input('Введите число: '))
factorials=[]
for element in range(1, number+1):
    factorial=1
    for a in range(1,element+1):
        factorial*=a
    factorials.append(factorial, )
print(factorials)
# Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
print('x| y|¬(x∧y)∨z')
for x in range(2):
  for y in range(2):
    for z in range(2):
      print(f'{x}| {y}| {int (not(x and y))or z}')
# # Даны две строки. Посчитайте сколько раз 
# # каждый символ первой строки встречается во второй
# # «one» «onetwonine» - o – 2, n – 3, e – 2

string1=str(input('Введите первую строку '))
string2=str(input('Введите вторую строку '))
string1_unique=[]
for i in string1:
    if i not in string1_unique:
        string1_unique.append(i)
for i in range(len(string1_unique)):
    count=0
    for j in range(len(string2)):
        if string1_unique[i]==string2[j]:
            count+=1
    print(f'{string1_unique[i]} - {count}', end=', ')             

#  Задайте список из N элементов, заполненных числами из 
#  промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]
numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
step=int(input('Введите количество элементов на которое нужно сдвинуть список '))
shiftlist=numbers[-1*step:]+numbers[:-1*step]
print(numbers)
print(shiftlist)