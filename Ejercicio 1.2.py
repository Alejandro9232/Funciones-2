import math

pi = math.pi

volumen_total_figura = lambda r1, r2, h : (4/3)*(pi)*(r1**3) + (1/3)*(pi)*(r2**2)*(h)
area_total_figura = lambda r1, r2, g : (4)*(pi)*(r1**2) + (pi)*(r2)*(g) + (pi)*(r2**2)

r1 = int(input("Ingresar el radio del circulo: "))
r2 = int(input("Ingresar el radio del cono: "))
h = int(input("Ingresar la altura del cono: "))

g = ((r2**2)+(h**2))**(1/2)
vt = volumen_total_figura (r1, r2, h)
at = area_total_figura (r1, r2, g)

print(f"El volumen de la figura es {vt} unidades")
print(f"El area de la figura es {at} unidades ")