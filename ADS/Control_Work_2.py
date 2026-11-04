import math

def gcd_subtraction(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def task_1():
    nums = [int(input(f"Введите число {i+1}: ")) for i in range(4)]
    
    # Поочередно находим НОД всех четырех чисел
    res = nums[0]
    for num in nums[1:]:
        res = gcd_subtraction(res, num)
    print(f"Наибольший общий делитель четырех чисел: {res}")


def optimized_trial_factorization(n):
    factors = {}
    d = 2
    while d * d <= n:
        if n % d == 0:
            count = 0
            while n % d == 0:
                count += 1
                n //= d
            factors[d] = count
        # Оптимизация шага: после 2 проверяем только нечетные числа
        d += 1 if d == 2 else 2
    if n > 1:
        factors[n] = 1
    return factors

def task_2():
    n = int(input("Введите целое положительное число для факторизации: "))
    original_n = n
    
    factors = optimized_trial_factorization(n)
    
    print(f"Каноническое разложение числа {original_n}:")
    factors_str = " * ".join([f"{p}^{c}" if c > 1 else str(p) for p, c in factors.items()])
    print(f"{original_n} = {factors_str}\n")


def fermat_factorization(n):
    if n % 2 == 0:
        return 2, n // 2
    m = math.isqrt(n)
    if m * m < n:
        m += 1
    
    x = 0
    while True:
        q = (m + x) * (m + x) - n
        root = math.isqrt(q)
        # Проверяем, является ли q точным квадратом
        if root * root == q:
            a = m + x
            b = root
            return a - b, a + b
        x += 1

def task_3():
    n = int(input("Введите нечетное число для факторизации: "))
    
    p1, p2 = fermat_factorization(n)
    print(f"Результат разложения Ферма: {n} = {p1} * {p2}")


def lucas_lehmer_test(p):
    m = (1 << p) - 1  # Вычисление M_p = 2^p - 1 через битовый сдвиг
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % m  # Остаток берется сразу, чтобы избежать переполнения
    return s == 0

def task_4():
    p = int(input("Введите показатель p для числа Мерсенна (M_p = 2^p - 1): "))
    
    m = (1 << p) - 1
    if lucas_lehmer_test(p):
        print(f"Число Мерсенна M_{p} ({m}) является ПРОСТЫМ.")
    else:
        print(f"Число Мерсенна M_{p} ({m}) является СОСТАВНЫМ.")


def von_neumann_generator(seed, count=10):
    sequence = []
    current = seed
    for _ in range(count):
        # Возводим в квадрат, дополняем нулями до 10 символов и берем центральные 5 цифр
        squared_str = str(current ** 2).zfill(10)
        current = int(squared_str[2:7])
        sequence.append(current)
    return sequence

def task_5():
    seed = int(input("Введите начальное пятизначное число: "))
    
    seq = von_neumann_generator(seed, 10)
    print("Сгенерированная последовательность:", *seq)


def sieve_sundaram(n):
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

def task_6():
    n = int(input("Введите верхнюю границу N: "))
    
    primes = sieve_sundaram(n)
    print(f"Простые числа до {n}: {primes}")



task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
