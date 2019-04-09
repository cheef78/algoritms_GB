#Суслов Олег Александрович
from pympler import asizeof
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
print ("\nКоличество байт памяти, занятое переменными = ", str(asizeof.asizeof(massiv)))
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
print ("\nКоличество байт памяти, занятое переменными = ", str(asizeof.asizeof(massiv)+asizeof.asizeof(numbs)))
            
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

print ("\nКоличество байт памяти, занятое переменными = ", str(asizeof.asizeof(massiv)+asizeof.asizeof(minel)+asizeof.asizeof(maxel)))

print ('*'*80)



print ('*'*80)
print ('4. Определить, какое число в массиве встречается чаще всего.\n\n')
massiv = []
eqmassiv = []
import random
for el in range (0,50):
    massiv.append(random.randint(1,10))
for el in range (0,50):
    numbs = massiv[el]
    num = 0
    for el1 in range (0,50):
        if numbs == massiv[el1]:
            num = num+1
    eqmassiv.append(num)
maxel = eqmassiv[0]
posmaxel = 0
for el1 in range (0,50):
        if eqmassiv[el1] >= maxel:
            maxel = el1
print ('Исхоный массив чисел:')
for el2 in range(0, (int(len(massiv))//10)):
    for el1 in range (0,10):
        print (massiv[10*el2+el1],';',sep='', end = '')
        if (10*el2+el1)+1>= int(len(massiv)):
            break
    print ('\n')
print ('Массив числа повторений:')
for el2 in range(0, (int(len(massiv))//10)):
    for el1 in range (0,10):
        print (eqmassiv[10*el2+el1],';',sep='', end = '')
        if (10*el2+el1)+1>= int(len(eqmassiv)):
            break
    print ('\n')


print ("В исходном массиве чисел максимально повторяющееся число =  ", massiv[maxel])
print ("\nКоличество байт памяти, занятое переменными = ", str(asizeof.asizeof(massiv)+asizeof.asizeof(eqmassiv)))
print ('*'*80)
    






print('Пользователь вводит данные о количестве предприятий, их наименования и прибыль')
print('за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..')
print('Программа должна определить среднюю прибыль (за год для всех предприятий)')
print('и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести')
print('наименования предприятий, чья прибыль ниже среднего.')
print('Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections')

numb = int(input ('\nВвелите число учитываемых предприятий '))
names = []
kvartal1=[]
kvartal2 = []
kvartal3 = []
kvartal4 = []
kvartal = []
Summ  = 0
Avrg = 0
for i in range (0, numb):
    names.append((input ('\nВвелите наименования предприятия № ' + str(i+1) + ' ')))
    kvartal1.append(int(input ('\nВвелите прибыль предприятия ' + names[i] + ' за ПЕРВЫЙ квартал ')))
    kvartal2.append(int(input ('\nВвелите прибыль предприятия ' + names[i] + ' за ВТОРОЙ квартал ')))
    kvartal3.append(int(input ('\nВвелите прибыль предприятия ' + names[i] + ' за ТРЕТИЙ квартал ')))
    kvartal4.append(int(input ('\nВвелите прибыль предприятия ' + names[i] + ' за ЧЕТВЕРТЫЙ квартал ')))
    kvartal.append((kvartal1[i]+kvartal2[i]+kvartal3[i]+kvartal4[i])/4)
    Summ = Summ + kvartal[i]
Avrg = Summ/numb
for i in range (0, numb):
    print (f"\nНаименование предприятия -{names[i]} Среднегодовая прибыль предприятия =  {kvartal[i]}")
print ('\nСреднегодовая прибыль по всем предприятиям = ', Avrg)
print ('\nСписок предприятий с годовой прибылью выше или равной среднегодовой:')
for i in range (0, numb):
    if kvartal[i] >= Avrg:
        print (names[i])
print ('\nСписок предприятий с годовой прибылью ниже среднегодовой:')
for i in range (0, numb):
    if kvartal[i] < Avrg:
        print (names[i])

Itogo = [asizeof.asizeof(numb), asizeof.asizeof(names),asizeof.asizeof(kvartal1),asizeof.asizeof(kvartal2),asizeof.asizeof(kvartal3),asizeof.asizeof(kvartal4),asizeof.asizeof(kvartal),asizeof.asizeof(Avrg),asizeof.asizeof(Summ)] 
S=0
for el in range(0,int(len(Itogo))):
    S=S+Itogo[el]
print ("\nДанные об использовании программой объема оперативной памяти: ")
print ("\nОбщее количество байт памяти, занятое используемыми переменными = ", str(S+asizeof.asizeof(S)+asizeof.asizeof(Itogo)))
print ("\nв т.ч. количество байт памяти, занятое основными переменными = ", str(S))
print ("\nв т.ч. количество байт памяти, занятое служебными переменными = ", str(asizeof.asizeof(S)+asizeof.asizeof(Itogo)))


