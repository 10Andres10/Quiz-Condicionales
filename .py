print("--------- TIPOS ------")
print("---------- DE --------")
print("------ TRIANGULOS ----")

#input
x = input("Digite un lado del triangulo: ")
x= int(x)
y = input("Digite un segundo lado del triangulo: ")
y = int(y)
z = input("Digite un tercer lado del triangulo: ")
z = int(z)

#procesing
if (x + y) > z or (z + y) > x or (z + x) > y:
    print(" Si es un tipo de triangulo ")
    if (x == y) and (y == z):
        print(" y es un triangulo equilatero. ")
    if (x == y) or (y == z) or (z == x):
        print(" y es un triangulo isoceles. ")
    else:
        print(" y es un triangulo escaleno. ")

else:
    print(" No es un triangulo ")

