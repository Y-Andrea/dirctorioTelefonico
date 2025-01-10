#verificacion para saber si una persona si es, o no, mayor de edad

print ("año actual de solicitud")
añoActual= int(input())
print("digite su nombre completo")
nombreCompleto = input ()
print ("año de nacimiento segun su documento de identidad")
añoDeNacimiento = int (input())
if añoActual - añoDeNacimiento >18:

    print("añoActual - añoDeNacimiento es mayor a 18, si puede votar")
else:
    print("añoActual - añoDeNacimiento es menor a 18, no puede votar")











