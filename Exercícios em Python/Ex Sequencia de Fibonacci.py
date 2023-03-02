def verifica_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    if b == n:
        return True
    else:
        return False

def calcula_fibonacci(n):
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if fibonacci[-1] == n:
        print(f"O número {n} pertence à sequência de Fibonacci!")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")
    return fibonacci

numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
fibonacci = calcula_fibonacci(numero)
print(fibonacci)
