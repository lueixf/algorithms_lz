from random import randint
N = 100 # N = len(a)
a = []
for i in range(1, N+1): # цикл для присваивания значения элементам
    a.append(randint(1, 1_000_000)) #рандом
g=0 #счетчик
for i in range(0, len(a)-1): #цикл для проверки по всей длине
    f = False # флаг для проверки наличия изменений
    for j in range(0,len(a)- 1 - i):# цикл для проверки каждого элемента
        if a[j] > a[j+1]:# условие
            a[j], a[j+1]=a[j+1], a[j] # обмен значений при выполнении условия
            f = True # смена флага при наличии изменений
            print(a) #названия переменных, выход из цикла
        g +=1 
    if not f: # возможность выхода из цикла при отсутствии изменений 
        break
print('Счетчик =', g) # вывод 
N = 100 # N = len(a)
a = [] 
for i in range(N): # цикл для присваивания значения элементам
    a.append(randint(1, 1_000_000)) #рандом
g1=0 # счётчик
i=0
while i < N - 1: # цикл для проверки по всей длине
    m=i # присвоение минимального значения
    j = i # поиск следующего минимального через переменную j
    while j < N: # поиск через проверку каждого элемента 
        if a[j] < a[m]: # условие
            m = j # присвоение нового минимального значения
        g1 += 1 #счётчик
        j += 1 # переход к следующему элементу 
    a[i], a[m] = a[m], a[i] # обмен значений
    print(a) 
    
    i += 1 
print(a)
print('кол-во сравнений при сортировке пузырьком =', g)
print('кол-во сравнений при сортировке выбором =', g1)





