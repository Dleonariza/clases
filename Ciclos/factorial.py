
n = int(input("Digite el numero: "))

if n == 0:
    print(1)
elif n > 0:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"{n}! = {factorial}")
