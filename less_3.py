#Суслов Олег Александрович

print ('*'*80)
print ('В диапазоне натуральных чисел от 2 до 99 определить,\nсколько из них кратны каждому из чисел\nв диапазоне от 2 до 9\n\n')
massiv = []
for el in range (2,10):
    num = 0
    for el1 in range (2,100):
        if el1%el==0:
            num = num+1
    massiv.append(num)
for i  in range (0,8):
    print ("В диапазоне чисел, от 2 до 99, числу - " + str(i+2) + " кратно " + str(massiv[i]) + " чисел")
print ('*'*80)
    
print ('*'*80)
print ('Во втором массиве сохранить индексы четных элементов первого массива.\nНапример, если дан массив со значениями 8, 3, 15, 6, 4, 2,\nто во второй массив надо заполнить значениями 1, 4, 5, 6 \n(или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.\n\n')
massiv = []
numbs = []
import random
for el in range (0,100):
    massiv.append(random.randint(1,100))
for el1 in range (0,100):
    if massiv[el1]%2==0:
        numbs.append(el1)
print (massiv)
print (numbs)
print ('*'*80)


