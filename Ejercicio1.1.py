verificar_coordenadas = lambda h, k, x, y:(x-h)**2 + (y-k)**2

verificacion = lambda d,r: (
"dentro" if d < r**2 else
"en el borde" if d == r**2 else
"fuera"
)

h = int(input("Ingresar coordenada h: "))
k = int(input("Ingresar coordenada k: "))
r = int(input("Ingresar radio r: "))
x = int(input("Ingresar coordenada x: "))
y = int(input("Ingresar coordenada y: "))

d2 = verificar_coordenadas (h, k, x, y)
resultado = verificacion (d2, r)
print(f"El punto esta {resultado} del radio")