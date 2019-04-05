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


