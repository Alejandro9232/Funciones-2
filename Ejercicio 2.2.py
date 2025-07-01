print("Ingresar longitudes positivas para saber si se puede construir un triangulo")

def Es_un_triangulo (*lados):

    a, b, c = lados

    if a + b > c and a + c > b and b + c > a:
        print("Si se puede formar el triangulo")
    else:
        print("No se puede formar el triangulo")

        
a = float(input("Ingresar longitud a: "))
b = float(input("Ingresar longitud b: "))
c = float(input("Ingresar longitud c: "))
    
Es_un_triangulo(a ,b ,c )
 