import time
import math
from collections import deque
from random import randint


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
    nums = [int(input(f'Введите число {i + 1}: ')) for i in range(4)]

    # Последовательно находим НОД всех четырех чисел
    res = nums[0]
    for num in nums[1:]:
        res = gcd(res, num)

    print(f'Наибольший общий делитель четырех чисел: {res}')


# Вероятностный тест Ферма для проверки на простоту
def is_ferma_prime(n, k=10):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    for i in range(k):
        a = randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True


# Задание 2. Факторизация числа

# наивный метод
def factorize(n, split=False):
    factors = []
    if n < 2:
        return factors

    # Проверяем делимость на 2
    while n % 2 == 0:
        if split:
            return [2, n // 2]
        factors.append(2)
        n //= 2

    # Ищем нечетные делители
    d = 3
    while d * d <= n:
        while n % d == 0:
            if split:
                return [d, n // d]
            factors.append(d)
            n //= d
        d += 2

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

        
        res = factorize(num, True)
        if len(res) == 1:
            factors.append(res[0])
        else:
            queue.extend(res)

    return sorted(factors)





# Проверка множителей на простоту
def check(factors):
    for p in sorted(set(factors)):
        print(f'{p} — {"простое" if is_ferma_prime(p) else "непростое"}')


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


    print('\nНаивная факторизация:')
    print('Множители:', f1)
    print(f'Время выполнения: {time1:.8f} секунд')

    print('Факторизация с помощью очереди:')
    print('Множители:', f2)
    print(f'Время выполнения: {time2:.8f} секунд')

    print('\nПроверка множителей на простоту:')
    check(f1)


# Задание 3. Факторизация методом Ферма

def fermat(n):
    # Если число простое или меньше 2
    if n < 2 or is_ferma_prime(n):
        return [n]

    # Для четного числа выносим множитель 2
    if n % 2 == 0:
        return fermat(2) + fermat(n // 2)

    m = math.isqrt(n)
    if m * m < n:
        m += 1

    x = 0

    # Ищем представление n как разность квадратов
    while True:
        q = (m + x) ** 2 - n
        root = math.isqrt(q)

        # является ли q полным квадратом
        if root * root == q:
            p1 = m + x - root
            p2 = m + x + root
            # рекурсивно проверяем и доразкладываем полученные множители
            return fermat(p1) + fermat(p2)

        x += 1


def task3():
    n = int(input('\nВведите число для факторизации: '))

    factors = sorted(fermat(n))
    print(factors)
    print(f'Результат разложения Ферма для {n}: {factors}')



# Задание 4. Тест Люка-Лемера
def lucas(p):
    # Вычисляем число Мерсенна
    m = (2 ** p) - 1
    s = 4

    # Строим последовательность с вычислением остатка
    for i in range(p - 2):
        s = (s * s - 2) % m

    return s == 0


def task4():
    p = int(input('\nВведите показатель p для числа Мерсенна (M_p = 2^p - 1): '))

    m = (2 ** p) - 1

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


# запуск
task1()
task2()
task3()
task4()
task5()
task6()

