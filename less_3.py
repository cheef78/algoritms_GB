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
    
print ('Во втором массиве сохранить индексы четных элементов первого массива.\nНапример, если дан массив со значениями 8, 3, 15, 6, 4, 2,\nто во второй массив надо заполнить значениями 1, 4, 5, 6 \n(или 0, 3, 4, 5 - если индексация начинается с нуля),\n т.к. именно в этих позициях первого массива стоят четные числа.\n\n')
massiv = []
numbs = []
import random
for el in range (0,50):
    massiv.append(random.randint(1,100))
for el1 in range (0,50):
    if massiv[el1]%2==0:
        numbs.append(el1)
print ('Исхоный массив чисел:')
for el2 in range(0, (int(len(massiv))//10)):
    for el1 in range (0,10):
        print (massiv[10*el2+el1],';',sep='', end = '')
        if (10*el2+el1)+1>= int(len(massiv)):
            break
    print ('\n')

print ('массив индексов четных элементов исходного массива:')
for el3 in range(0, (int(len(numbs))//10)+1):
    for el4 in range (0,10):
        
        print (numbs[10*el3+el4],';',sep='', end = '')
        if (10*el3+el4)+1>= int(len(numbs)):
            break
    print ('\n')
            
print ('*'*80)

print ('В массиве случайных целых чисел поменять местами\n минимальный и максимальный элементы.\n\n')
massiv = []
import random
for el in range (0,50):
    massiv.append(random.randint(1,100))
minel = massiv[0]
posminel = 0
maxel = massiv[0]
posmaxel = 0
for el1 in range (0,50):
        if massiv[el1]<= minel:
            minel = massiv[el1]
            posminel = el1
for el1 in range (0,50):
        if massiv[el1] >= maxel:
            maxel = massiv[el1]
            posmaxel = el1


       
print ('Исхоный массив чисел:')
for el2 in range(0, (int(len(massiv))//10)):
    for el1 in range (0,10):
        print (massiv[10*el2+el1],';',sep='', end = '')
        if (10*el2+el1)+1>= int(len(massiv)):
            break
    print ('\n')

print ('Максимальный элемент =  {}, позиция максимального элемента = {}\n'.format(maxel,posmaxel))
print ('Минимальный элемент =  {}, позиция минимального элемента = {}\n'.format(minel,posminel))
            
massiv[posmaxel] = minel
massiv[posminel] = maxel

print ('Массив чисел с замененными элементами:')
for el2 in range(0, (int(len(massiv))//10)):
    for el1 in range (0,10):
        print (massiv[10*el2+el1],';',sep='', end = '')
        if (10*el2+el1)+1>= int(len(massiv)):
            break
    print ('\n')




print ('*'*80)


