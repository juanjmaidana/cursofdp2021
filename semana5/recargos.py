edad = int(input("Ingrese su edad: "))
decJurIng = int(input("Ingrese su Declaración Jur. de Ingresos: "))
bien = 3500
if (edad >= 18 and decJurIng >= 20000):
    extra = bien + (bien * 0.15)
    totalCompras = bien + extra
    print("Debe pagar tributo")
    print("Adicional: $",extra)
    print("Total a pagar: $",totalCompras)
else:
    print("No debe pagar Tributo extra")