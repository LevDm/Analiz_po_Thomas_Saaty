# -*- coding: utf-8 -*-
def KOLVO_KRIT(): #запрос количества критериев с проверкой
    i = True
    while i == True:
        print('\n-----')
        N = input('* Введите количество критериев целым числом: ')
        
        if N == 'exit': break
    
        if  N.isdigit() == True:
            N = int(N)
            break
        else:
            print('\n** Необходимо целое число!')
            continue
    return N


def WHAT_VALUE(I,J): #запрос оценки критериев с проверкой
    i = True
    while i == True:
        print('\n-----')
        print('* В методе Саати для оценки относительной важности критериев рекомендуется специальная шкала от 1 до 9, где:\n** 1 - компонентs равной важности,\n** 3 - умеренное превосходство,\n** 5 - существенное превосходство,\n** 7 - значительное превосходство,\n** 9 - очень сильное превосходство.\n** !!Значения 2, 4, 6, 8 - используются как промежуточные между двумя соседними компонентами.')
        print('\n*** Относительная важность ритерия -№'+str(I)+' отностиельно -№'+str(J))
        VALUE = input('**** Введите оценку критериев ненулевым целым числом(от 1 до 9): ')
                
        if  VALUE.isdigit() == True and int(VALUE) > 0 and int(VALUE) <= 9:
            break
        else:
            print('\n***** Необходимо целое число от 1 до 9!')
            continue
    return VALUE


def MATRIX(N): #создание матрицы
    A = []
    N = N + 1
    for i in range(N):
        B = []
        for j in range(N): B.append(None)
        A.append(B)

    for i in range(N):
        for j in range(N):
            
            if A[i][j] != None: continue
        
            VALUE = 000
            
            if j == 0: VALUE = 'к№' + str(i) 
            if i == 0: VALUE = 'к№' + str(j)
            
            if i == j: 
                VALUE = 1
                if i == 0: VALUE = 'Кр '
                
            if VALUE == 000: VALUE = WHAT_VALUE(i,j)   
                
            VALUE = str(VALUE)
            
            if VALUE.isdigit() == True: 
                VALUE = round(float(VALUE),2)
                A[j][i] = round(1 / VALUE,2)
            
            A[i][j] = VALUE  
    return A


def isint(value): #определение целое ли число
    try:
        float(value)
        return True
    except ValueError:
        return False


def isfloat(value): #определение дробно ли число
    try:
        float(value)
        return True
    except ValueError:
        return False


def WHAT_KOEF(A): #расчет коэфициентов
    all_sum = 0
    W = []
    for i in range(len(A)):
        W.append(0)
        if i == 0: continue
        
        for j in range(len(A)):
            OZENKA = A[i][j] 

            if isfloat(OZENKA) == True or isint(OZENKA) == True:
                
                all_sum = all_sum + OZENKA
                
                W[i] = W[i] + OZENKA
                
    for i in range(len(A)):  
        W[i] = W[i] / all_sum
        W[i] = round(W[i],2)
    return W
  
      
def PRINT_KOEF(W): #вывод коэфициентов
    print('\n-----')
    print('Весовые коэффициенты критериев:')
    for i in range(len(W)):
        if i == 0: continue
        print('Критерий №' + str(i) + ' = ' + str(W[i]))


def PRINT_MATRIX(A): #вывод матрицы
    print('\n-----')
    for i in range(len(A)):
        LINE = ''
        for j in range(len(A)):    
            LINE = LINE + str(A[i][j]) + '     '
        print(LINE)


rabota = True
while  rabota == True:
    print('\n----------------')
    print('!!! Если необходимо завершить работу введите "exit" вместо количества критериев')
    
    n =  KOLVO_KRIT()    
    if n == 'exit': break
    a = MATRIX(n)
    PRINT_MATRIX(a)
    w = WHAT_KOEF(a)
    PRINT_KOEF(w)
