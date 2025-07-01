import time

def fibonacci_iterativo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

n = int(input("Ingrese un número para calcular Fibonacci: "))

start_time = time.time()
resultado_iterativo = fibonacci_iterativo(n)
end_time = time.time()
tiempo_iterativo = end_time - start_time

start_time = time.time()
resultado_recursivo = fibonacci_recursivo(n)
end_time = time.time()
tiempo_recursivo = end_time - start_time

print(f"Fibonacci({n}) con iteración: {resultado_iterativo}")
print(f"Tiempo iterativo: {tiempo_iterativo:.6f} segundos")

print(f"Fibonacci({n}) con recursión: {resultado_recursivo}")
print(f"Tiempo recursivo: {tiempo_recursivo:.6f} segundos")