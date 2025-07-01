import math
print("Ingresa 5 números reales:")

def calcular_promedio(*numeros):
    return sum(numeros) / len(numeros)

def promedio_multiplicativo(*numeros):
    producto = 1
    for n in numeros:
        producto *= n
    return producto ** (1 / len(numeros))

def potencia_mayor_menor(*numeros):
    mayor = max(numeros)
    menor = min(numeros)
    return mayor ** menor

def raiz_cubica_menor(*numeros):
    menor = min(numeros)
    return menor ** (1 / 3)

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
n4 = float(input("Número 4: "))
n5 = float(input("Número 5: "))

numeros = [n1, n2, n3, n4, n5]

print("RESULTADOS")
print("Promedio:", calcular_promedio(*numeros))
print("Promedio multiplicativo:" ,promedio_multiplicativo(*numeros))
print("Potencia del mayor al menor:", potencia_mayor_menor(*numeros))
print("Raíz cúbica del menor:", raiz_cubica_menor(*numeros))