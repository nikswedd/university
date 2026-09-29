import math

def f(x):
    return math.exp(x - 1) - x**3 - x

def fa(a, b, eps):
    if f(a) * f(b) > 0: #проверка на наличие корня
        return None
    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def fb(a, b, eps):
    if f(a) * f(b) > 0: #проверка на наличие корня
        return None
    while abs(b - a) > eps:
      #вычисление примерного "х" с помощью уравнения прямой
        x = a - f(a) * (a - b) / (f(a) - f(b))
        if f(x) == 0:
            return x
        elif f(x) * f(a) < 0:
            b = x
        else:
            a = x
    return x

#1
print(fa(0, 1, 0.00001)) #0.48357391357421875
#2
print(fb(0, 1, 0.00001)) #0.48356891139951785



######################################

#1
def b(ll, val):
    rv = ll[-1]
    lv = ll[0]
    l = 0
    r = len(ll)
    while l < r:
        m = l + (r - l) // 2
        if ll[m] == val:
            return f'Индекс: {m}.'
        elif (ll[m] > val and rv > lv) or (ll[m] < val and rv < lv):
            r = m
        elif (ll[m] < val and rv > lv) or (ll[m] > val and rv < lv):
            l = m + 1
    ll.insert(r, val)
    return f'Новый массив: {ll}. Индекс: {r}.'

li = [1, 0, -1, -9]
print(b(li, 0.1)) #Новый массив: [1, 0.1, 0, -1, -9]. Индекс: 1.
li = [-6, -1, 2, 4, 5]
print(b(li, 3)) #Новый массив: [-6, -1, 2, 3, 4, 5]. Индекс: 3.
li = [9, 5, 0, -1, -6]
print(b(li, 5)) #Индекс: 1.





#2
def f(x):
    if len(x) < 3:
        return None
    l = 0
    r = len(x) - 1
    while l < r:
        m = l + (r - l) // 2
        if x[m] < x[m + 1]: #возрастание
            l = m + 1
        else: #убывание
            r = m
    if l == 0 or l == len(x) - 1: #Если пик находится на границе
        return None
    for i in range(1, l + 1):
        if x[i - 1] > x[i]:
            return None
    for i in range(l, len(x) - 1):
        if x[i] < x[i + 1]:
            return None
    return l
li = [0, 1, 2, 3, 2, -1]
print(f'Индекс пика: {f(li)}.') #Индекс пика: 3.
li = [99, 0, 1, 2, 3, 2, 0]
print(f'Индекс пика: {f(li)}.') #Индекс пика: None.



#3
def f(arr):
    if arr[0] * arr[-1] > 0:
        return f'Положительных: {len(arr)}.' if arr[0] > 0 else f'Отрицательных: {len(arr)}.'
    elif arr[0] == arr[-1] == 0:
        return 'Только нули.'

    #Нахождение всех отрицительных
    negative = 0
    if arr[0] < 0:
        l, r = 0, len(arr) - 1
        while l < r:
            m = l + (r - l) // 2
            if arr[m] >= 0:
                r = m
            else:
                l = m + 1
        negative = l

    #Нахождение всех пложительных
    positive = 0
    if arr[-1] > 0:
        l, r = 0, len(arr) - 1
        while l < r:
            m = l + (r - l) // 2
            if arr[m] > 0:
                r = m
            else:
                l = m + 1
        positive = len(arr) - l

    return f'Положительных: {positive}. Отрицательных: {negative}. Наибольшее: {max(negative, positive)}.'
li = [-1, 0, 2, 2]
#Положительных: 2. Отрицательных: 1. Наибольшее: 2. [-1, 0, 2, 2]
print(f(li), li)
li = [0, 0, 0]
#Только нули. [0, 0, 0]
print(f(li), li)
li = [1]
#Положительных: 1. [1]
print(f(li), li)
li = [-9, -5, -1, 0, 0]
#Положительных: 0. Отрицательных: 3. Наибольшее: 3. [-9, -5, -1, 0, 0]
print(f(li), li)






#4
def ff(x):
    arr1, arr2 = [], [0] * len(x)
    for i in range(len(x) - 1, -1, -1):
        l = 0
        r = len(arr1)
        while l < r:
            m = l + (r - l) // 2
            if arr1[m] >= x[i]:
                r = m
            elif arr1[m] < x[i]:
                l = m + 1
        arr2[i] = r
        arr1.insert(r, x[i])
    return arr2


l = [5, 2, 6, 1, 1]
print(f'{l}->{ff(l)}')
