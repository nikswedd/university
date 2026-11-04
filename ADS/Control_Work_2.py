import time
import math
from collections import deque


# Задание 1. НОД методом вычитания

def gcd(a, b):
    # Вычитаем меньшее число из большего до их равенства
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def task1():
    nums = [int(input(f'Введите число {i+1}: ')) for i in range(4)]

    # Последовательно находим НОД всех четырех чисел
    res = nums[0]
    for num in nums[1:]:
        res = gcd(res, num)

    print(f'Наибольший общий делитель четырех чисел: {res}')


# Задание 2. Факторизация числа
def sieve(n):

    marked = [True] * (n + 1)
    marked[0] = marked[1] = False

    # Вычеркиваем составные числа, начиная с квадрата простого
    for i in range(2, math.isqrt(n) + 1):
        if marked[i]:
            for j in range(i * i, n + 1, i):
                marked[j] = False

    return marked



# Наивный перебор делителей
def factorize(n):
    factors = []
    d = 2

    # Делим число на найденный делитель до тех пор, пока это возможно
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1

    if n > 1:
        factors.append(n)

    return factors




# Факторизация с помощью очереди
def factor_queue(n):
    factors = []
    queue = deque([n])
    while queue:
        num = queue.popleft()

        if num < 2:
            continue

        # Проверяем делимость на 2
        if num % 2 == 0:
            factors.append(2)
            queue.append(num // 2)
            continue

        # Ищем нечётный делитель
        d = 3
        limit = math.isqrt(num)

        while d <= limit:
            if num % d == 0:
                break
            d += 2

        if d <= limit:
            queue.append(d)
            queue.append(num // d)
        else:
            # Делителей нет — число простое
            factors.append(num)

    return sorted(factors)

# Подсчет кратности множителей

def counts(factors):
    result = {}

    # Считаем количество повторений каждого множителя
    for p in factors:
        result[p] = result.get(p, 0) + 1

    return result


# Проверка множителей на простоту

def check(factors, primes):
    for p in sorted(set(factors)):
        print(f'{p} — {"простое" if primes[p] else "составное"}')


def task2():
    n = int(input('Введите целое положительное число: '))

    if n < 2:
        print('Число должно быть не меньше 2.')
        return

    # Замеряем время наивной факторизации
    start = time.perf_counter()
    f1 = factorize(n)
    time1 = time.perf_counter() - start

    # Замеряем время факторизации с помощью очереди
    start = time.perf_counter()
    f2 = factor_queue(n)
    time2 = time.perf_counter() - start

    # Подсчитываем кратность множителей
    c1 = counts(f1)
    c2 = counts(f2)

    print('\nНаивная факторизация:')
    print('Множители:', f1)
    print('Каноническое разложение:', c1)
    print(f'Время выполнения: {time1:.8f} секунд')

    print('\nФакторизация с помощью очереди:')
    print('Множители:', f2)
    print('Каноническое разложение:', c2)
    print(f'Время выполнения: {time2:.8f} секунд')

    # Создаём решето для проверки простоты множителей
    primes = sieve(n)

    print('\nПроверка множителей на простоту:')
    check(f1, primes)



# Задание 3. Факторизация методом Ферма

def fermat(n):
    # Для четного числа сразу выделяем множитель 2
    if n % 2 == 0:
        return 2, n // 2

    # Находим ближайшее целое число сверху от корня n
    m = math.isqrt(n)
    if m * m < n:
        m += 1

    x = 0

    # Ищем представление n как разность квадратов
    while True:
        q = (m + x) ** 2 - n
        root = math.isqrt(q)

        # Проверяем, является ли q полным квадратом
        if root * root == q:
            return m + x - root, m + x + root

        x += 1


def task3():
    n = int(input('\nВведите нечетное число для факторизации: '))

    p1, p2 = fermat(n)
    print(f'Результат разложения Ферма: {n} = {p1} * {p2}')




# Задание 4. Тест Люка-Лемера
def lucas(p):
    # Вычисляем число Мерсенна
    m = (2**p) - 1
    s = 4

    # Строим последовательность с вычислением остатка
    for i in range(p - 2):
        s = (s * s - 2) % m

    return s == 0


def task4():
    p = int(input('\nВведите показатель p для числа Мерсенна (M_p = 2^p - 1): '))

    m = (2**p) - 1

    if p < 2:
        print('Показатель p должен быть не меньше 2.')
        return

    if lucas(p):
        print(f'Число Мерсенна M_{p} ({m}) является ПРОСТЫМ.')
    else:
        print(f'Число Мерсенна M_{p} ({m}) является СОСТАВНЫМ.')



# Задание 5. Генератор фон Неймана
def neumann(seed):
    seq = []
    count = 10
    current = seed

    for jj in range(count):
        # Возводим число в квадрат и дополняем до 10 цифр
        squared = str(current ** 2).zfill(10)

        # Берем пять центральных цифр
        current = int(squared[2:7])
        seq.append(current)

    return seq


def task5():
    seed = int(input('\nВведите начальное пятизначное число: '))

    if seed < 10000 or seed > 99999:
        print('Число должно быть пятизначным.')
        return

    seq = neumann(seed)
    print('Сгенерированная последовательность:', *seq)



# Задание 6. Решето Сундарама
def sundaram(n):
    # Определяем размер массива
    k = (n - 1) // 2
    marked = [False] * (k + 1)

    # Отмечаем составные числа по формуле Сундарама
    for i in range(1, k + 1):
        j = i

        while i + j + 2 * i * j <= k:
            marked[i + j + 2 * i * j] = True
            j += 1

    primes = []

    # Число 2 добавляется отдельно
    if n >= 2:
        primes.append(2)

    # Получаем неотмеченные простые числа
    for i in range(1, k + 1):
        if not marked[i]:
            primes.append(2 * i + 1)

    return primes


def task6():
    n = int(input('\nВведите верхнюю границу N: '))

    primes = sundaram(n)
    print(f'Простые числа до {n}: {primes}')




task1()
task2()
task3()
task4()
task5()
task6()
