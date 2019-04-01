#Суслов Олег Александрович
import timeit

def numbs1():
    
    #print ('*'*80)
    #print ('В диапазоне натуральных чисел от 2 до 99 определить,\nсколько из них кратны каждому из чисел\nв диапазоне от 2 до 9\n\n')
    #print ('АЛГОРИТМ 1 (через 2 цикла)\n')
    massiv = []
    for el in range (2,10):
        num = 0
        for el1 in range (2,100):
            if el1%el==0:
                num = num+1
        massiv.append(num)
    #for i  in range (0,8):
        #print ("В диапазоне чисел, от 2 до 99, числу - " + str(i+2) + " кратно " + str(massiv[i]) + " чисел")
    #print ('*'*80)
    
    
def numbs2():
    
    #print ('*'*80)
    #print ('В диапазоне натуральных чисел от 2 до 99 определить,\nсколько из них кратны каждому из чисел\nв диапазоне от 2 до 9\n\n')
    #print ('АЛГОРИТМ 2 (через множественные условия)\n')
    massiv = []
    m2=0
    m3=0
    m4=0
    m5=0
    m6=0
    m7=0
    m8=0
    m9=0
    for el in range (2,100):
        if el%2 == 0:
            m2=m2+1
        if el%3 == 0:
            m3=m3+1
        if el%4 == 0:
            m4=m4+1
        if el%5 == 0:
            m5=m5+1
        if el%6 == 0:
            m6=m6+1
        if el%7 == 0:
            m7=m7+1
        if el%8 == 0:
            m8=m8+1
        if el%9 == 0:
            m9=m9+1
    massiv = [m2,m3,m4,m5,m6,m7,m8,m9]
    #for i  in range (0,8):
         #print ("В диапазоне чисел, от 2 до 99, числу - " + str(i+2) + " кратно " + str(massiv[i]) + " чисел")
    #print ('*'*80)
    
#numbs1()
#numbs2()
print ('*'*80)
print ('В диапазоне натуральных чисел от 2 до 99 определить,\nсколько из них кратны каждому из чисел\nв диапазоне от 2 до 9\n')

print ('\nАЛГОРИТМ 1 (через 2 цикла), 1 повтор\n')
print(timeit.timeit("numbs1()", setup="from __main__ import numbs1", number = 1))
print ('\nАЛГОРИТМ 2 (через множественные условия), 1 повтор\n')
print(timeit.timeit("numbs2()", setup="from __main__ import numbs2", number = 1))


print ('\nАЛГОРИТМ 1 (через 2 цикла), 1 тыс повторов\n')
print(timeit.timeit("numbs1()", setup="from __main__ import numbs1", number = 1000))
print ('\nАЛГОРИТМ 2 (через множественные условия), 1 тыс повторов\n')
print(timeit.timeit("numbs2()", setup="from __main__ import numbs2", number = 1000))

print ('\nАЛГОРИТМ 1 (через 2 цикла), 10 тыс повторов\n')
print(timeit.timeit("numbs1()", setup="from __main__ import numbs1", number = 10000))
print ('\nАЛГОРИТМ 2 (через множественные условия), 10 тыс повторов\n')
print(timeit.timeit("numbs2()", setup="from __main__ import numbs2", number = 10000))

print ('\nАЛГОРИТМ 1 (через 2 цикла), 100 тыс повторов\n')
print(timeit.timeit("numbs1()", setup="from __main__ import numbs1", number = 100000))
print ('\nАЛГОРИТМ 2 (через множественные условия), 100 тыс повторов\n')
print(timeit.timeit("numbs2()", setup="from __main__ import numbs2", number = 100000))


