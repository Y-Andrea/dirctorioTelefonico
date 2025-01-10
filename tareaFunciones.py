#hacer una funcion que me permita por las horas que fue a clases esta semana
#al final el programa me de la suma de las horas que estudio esa semana
#mi funcion, saludo.
def grate_people() :
    print("what is your name?")
    name = input ()
    print ("hello, how are you?" , name)
#Mi funcion, calculadora de Horas.
def calculo_horas() :
    print("cuantas horas estudiaste el lunes?")
    lunes = int(input ())
    print ("cuantas horas estudiaste el martes?")
    martes = int(input ())
    print ("cuntas horas estudiaste el miercole?")
    Miercoles = int(input ())
    #nombre de variable, total horas estudiadas
    totalHoras= lunes + martes + Miercoles
    print ("Horas estudiadas" , totalHoras)

    




#calculo_horas()

#mi funcion datos de mi mascota
def datos_de_mi_mascota () :
    print ("nombre de su mascota?")
    nombre= input ()
    print ("que edad tiene su mascota?")
    edad= input ()
    print ("tipo de mascota/raza")
    raza= input ()
    print ("tu nombre completo")
    tuNombre= input ()

    #llamo a mi funcion
    datos_de_mi_mascota= nombre + edad + raza + tuNombre
    print ("datos de mi mascota", datos_de_mi_mascota)
    
    print (nombre, "es una", raza, "el cual tiene", edad, "años de edad y", tuNombre, "es actualmente el dueño")

datos_de_mi_mascota ()

