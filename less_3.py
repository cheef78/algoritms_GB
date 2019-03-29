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
    
