#estructura de control que valida un numero ingresado.
def funcion_numero ():   #se hizo el def para dejar la estructura dentro de una funcion
    print ("digita un numero")
    numero = int (input ())
    if numero > 5:
        print ("numero es mayor que 5")
    else:
        print ("numero no es mayor que 5")



#programa para verificar si puede votar o no.
print ("digita tu edad")
numero = int(input())
if numero >=18:
    print ("numero mayor a 18 si puede votar")
else:
    print ("numero no es mayor a 18 no puede votar")











