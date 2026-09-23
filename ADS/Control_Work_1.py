import math

def f(x):
    return math.exp(x - 1) - x**3 - x

def fa(a, b, eps):
    if f(a) * f(b) > 0:
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
    if f(a) * f(b) > 0:
        return None
    while abs(b - a) > eps:
        x = a - f(a) * (a - b) / (f(a) - f(b))
        if f(x) == 0:
            return x
        elif f(x) * f(a) < 0:
            b = x
        else:
            a = x
    return x

#1
print(fa(0, 1, 0.00001))
#2
print(fb(0, 1, 0.00001))

#######################################

#1
def b(ll, val):
    rv = ll[-1]
    lv = ll[0]
    ll.sort()
    l = 0
    r = len(ll) - 1

    while l <= r:
        m = l + (r - l) // 2
        if ll[m] == val:
            return m if lv < rv else len(ll) - 1 - m
        elif ll[m] > val:
            r = m - 1
        elif ll[m] < val:
            l = m + 1

    indl = l
    indr = len(ll) - 1 - l
    if lv < rv:
        ll.insert(indl, val)
        return f'Новый массив: {ll}. Индекс: {indl}.'
    elif lv > rv:
        ll.insert(indl, val)
        ll.sort(reverse=True)
        return f'Новый массив: {ll}. Индекс: {indr + 1}.'

li = [1, 0, -1, -9]
print(b(li, 0.1))




#2
def f(x):
    if len(x) < 3:
        return None
    l = 0
    r = len(x) - 1
    while l < r:
        m = l + (r - l) // 2
        if x[m] < x[m + 1]:
            l = m + 1
        else:
            r = m
    if l == 0 or l == len(x) - 1:
        return None
    for i in range(1, l + 1):
        if x[i - 1] > x[i]:
            return None
    for i in range(l, len(x) - 1):
        if x[i] < x[i + 1]:
            return None
    return l
li = [0, 1, 2, 3, 2, -1]
print(f(li))






#3
def f(arr):
    if arr[0] * arr[-1] > 0:
        return len(arr)
    elif arr[0] == arr[-1] == 0:
        return 0

    negative = 0
    if arr[0] < 0:
        l, r = 0, len(arr) - 1
        while l + 1 < r:
            m = l + (r - l) // 2
            if arr[m] >= 0:
                r = m
            else:
                l = m
        negative = l + 1

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

    return max(negative, positive)
li = [-6, -3, -3, -1, 0, 0, 1, 6]
print(f(li))





#4
def f(arr):
    res = []

    for i in range(len(arr)):
        arr_2 = arr[i:]
        el = arr_2[0]
        if len(arr_2) > 1:
            arr_2.sort()
            l = 0
            r = len(arr_2) - 1

            while l <= r:
                m = l + (r - l) // 2
                if arr_2[m] >= el:
                    r = m - 1
                elif arr_2[m] < el:
                    l = m + 1
            res.append(l)

        else:
            res.append(0)
    return res

l = [5, 2, 6, 1, 1]
print(f(l))
