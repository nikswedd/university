
import math

def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def task1():
    nums = [int(input(f"Введите число {i+1}: ")) for i in range(4)]

    res = nums[0]
    for num in nums[1:]:
        res = gcd(res, num)

    print(f"Наибольший общий делитель четырех чисел: {res}")


def factorize(n):
    factors = {}
    d = 2

    while d * d <= n:
        if n % d == 0:
            count = 0
            while n % d == 0:
                count += 1
                n //= d
            factors[d] = count

        d += 1 if d == 2 else 2

    if n > 1:
        factors[n] = 1

    return factors


def task2():
    n = int(input("Введите целое положительное число для факторизации: "))
    original_n = n

    factors = factorize(n)

    print(f"Каноническое разложение числа {original_n}:")
    factors_str = " * ".join(
        [f"{p}^{c}" if c > 1 else str(p) for p, c in factors.items()]
    )
    print(f"{original_n} = {factors_str}\n")


def fermat(n):
    if n % 2 == 0:
        return 2, n // 2

    m = math.isqrt(n)
    if m * m < n:
        m += 1

    x = 0
    while True:
        q = (m + x) ** 2 - n
        root = math.isqrt(q)

        if root * root == q:
            return m + x - root, m + x + root

        x += 1


def task3():
    n = int(input("Введите нечетное число для факторизации: "))

    p1, p2 = fermat(n)
    print(f"Результат разложения Ферма: {n} = {p1} * {p2}")


def lucas_lehmer(p):
    m = (1 << p) - 1
    s = 4

    for _ in range(p - 2):
        s = (s * s - 2) % m

    return s == 0


def task4():
    p = int(input("Введите показатель p для числа Мерсенна (M_p = 2^p - 1): "))

    m = (1 << p) - 1

    if lucas_lehmer(p):
        print(f"Число Мерсенна M_{p} ({m}) является ПРОСТЫМ.")
    else:
        print(f"Число Мерсенна M_{p} ({m}) является СОСТАВНЫМ.")


def von_neumann(seed, count=10):
    sequence = []
    current = seed

    for _ in range(count):
        squared_str = str(current ** 2).zfill(10)
        current = int(squared_str[2:7])
        sequence.append(current)

    return sequence


def task5():
    seed = int(input("Введите начальное пятизначное число: "))

    seq = von_neumann(seed, 10)
    print("Сгенерированная последовательность:", *seq)


def sundaram(n):
    k = (n - 1) // 2
    marked = [False] * (k + 1)

    for i in range(1, k + 1):
        j = i
        while i + j + 2 * i * j <= k:
            marked[i + j + 2 * i * j] = True
            j += 1

    primes = []
    if n >= 2:
        primes.append(2)

    for idx in range(1, k + 1):
        if not marked[idx]:
            primes.append(2 * idx + 1)

    return primes


def task6():
    n = int(input("Введите верхнюю границу N: "))

    primes = sundaram(n)
    print(f"Простые числа до {n}: {primes}")


task1()
task2()
task3()
task4()
task5()
task6()
