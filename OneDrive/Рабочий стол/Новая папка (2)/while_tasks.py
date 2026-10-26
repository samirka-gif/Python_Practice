i=1
while i<=10:
    print(i)
    i+=1

total = 0
n = int(input("Введите число: "))
while n != 0:
    total += n
    n = int(input("Введите число: "))
print("Сумма:", total)

n = int(input("Введите натуральное число: "))
c = 0
while n > 0:
    c += 1
    n = n // 10
print("Количество цифр:", c)

n = int(input("Введите натуральное число: "))
total = 0
while n > 0:
    digit = n % 10
    total += digit
    n = n // 10
print("Сумма цифр:", total)

n = int(input("Введите натуральное число: "))
result = 0
while n > 0:
    digit = n % 10
    result = result * 10 + digit
    n = n // 10
print(result)

n = int(input("Введите число n: "))
power = 1
while power <= n:
    print(power)
    power *= 2

passw="123qwerty"
input_passw=input("введите пароль")
while input_passw !=passw:
    print("неверный пароль")
    input_passw=input("введите пароль")
print("доступ разрешен")


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
while b != 0:
    remainder = a % b
    a = b
    b = remainder
print("НОД:", a)

n = int(input("Введите число n: "))
a = 0
b = 1
while a <= n:
    print(a)
    a, b = b, a + b


num = 57
count = 0
n = int(input("Угадайте число от 1 до 100: "))
count += 1
while n != num:
    if n < num:
        print("Больше")
    else:
        print("Меньше")
    n = int(input("Попробуйте ещё раз: "))
    count += 1
print("Правильно! Попыток:", count)