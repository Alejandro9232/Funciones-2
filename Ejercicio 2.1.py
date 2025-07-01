import time

def imprimir_numeros(*args):
    for arg in args:
        if arg == "impares":
            for i in range(1, 1000, 2):
                print(f"Los números impares son: {i}")
                time.sleep(0.02)
        elif arg == "pares":
            for j in range(2, 1001, 2):
                print(f"Los números pares son: {j}")
                time.sleep(0.02)

imprimir_numeros("impares", "pares")