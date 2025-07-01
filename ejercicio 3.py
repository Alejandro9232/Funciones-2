print("Agrega un número y la potencia")

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        resultado = base * potencia(base, exponente - 1)
        print(f"Calculando: {base}^{exponente} = {base} * {base}^{exponente - 1} = {resultado}")
        return resultado

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese la potencia: "))

print(f"Resultado final: {base}^{exponente} = {potencia(base, exponente)}")