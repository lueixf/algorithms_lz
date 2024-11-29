import random 

print ('Первый список')
list_1 = random.sample(range(1000001), 100)    #выбор случайных элементов из диапазона без повторений
list_1.sort()
print(list_1)

a = int(input('искомый элемент:'))

score = 0       # считаем количество сравнений, начиная с 0
if a in list_1:      # если элемент есть в list_1
    for i in range(0, len(list_1)):
        score = score + 1    #прибавляем каждый цикл 1
        if list_1[i] == a:  
            break
    print(f'индекс искомого в линейном поиске :{i}')
    print(f'колтчество сравнений в линейном поиске: {score}')
else :
    print('элемент не найден в первом списке')

# бинарный поиск
print(list_1)    # сортированный первый список
if  a in list_1:
    first = 0
    last = len(list_1)
    score_2 = 0
    index = 1
    while (first <= last) and index == 1:
        mid = (first + last)//2 #   индекс элемента в середине списка
        score_2 = score_2 + 1  #    прибавляем каждый цикл + 1
        if list_1[mid] == a:
            index = mid
        else :
            if a < list_1[mid]:
                last = mid - 1
            else:
                first = mid + 1
    print(f'количество сравнений в бинарном поиске :{score_2}')
    print(f'индекс искомого элемента в бинарном поиске :{score_2}')
else:
    print('элемент не найден во втором списке')
    