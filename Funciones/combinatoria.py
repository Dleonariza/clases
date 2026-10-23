def factorial(num):
    if num < 0:
        return None
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for n in range(2, num+1):
            fact *= n # es lo mismo fact = fact * n
        return fact

def combinatoria(n, k):
    if n < 0 or k < 0 or (n - k) < 0:
        return None
    else:
        combi = factorial(n) / (factorial(k) * factorial(n - k))
        return combi
    
n = int(input("Ingrese un numero mayor igual que 0: "))
k = int(input("Ingrese un numero mayor igual que 0 para k:"))

print("C(", n, ",", k, ")= ", combinatoria(n, k))