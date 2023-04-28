from tkinter import Menu


def Facturacion():
    nombre=str(input("Didite su nombre:    "))
    Cedula=int(input("Digite su ID:    "))
    Reserv=str(input("Cual es su numero de reserva?:   "))

    if (Reserv == "1") or (Reserv == "01"):
        print("Factura  Agencia de autos power point"
                , nombre,
                Cedula,
                "Su cita ha sido agendada de 9:00 a 11:00  ",  )
    elif (Reserv == "2") or (Reserv == "02"):
        print("Factura Agencia de autos power point"
                , nombre ,
                Cedula,
                "Su cita ha sido agendada de 12:00 a 2:00  ")
    elif  (Reserv == "3") or (Reserv == "03"):
        print("Factura Agencia de autos power point"
                , nombre
                ,Cedula,
                "Su cita ha sido agendada de 3:00 a 5:00  ")
        menu()
    else:
        print("Hubo algun error en los datos ingresados, intente nuevamente")
        Facturacion()
        
def logIn ():

# Email address: cyber@gmail.com
# pwd = Final

    email = str(input("Ingerse su email address: "))
    pwd = str(input("Ingrese su password:"))
    
    if (email == "cyber@gmail.com") and (pwd == "Final"):
        print ("Bienvenido")
        print(welcome())

    elif (email != "cyber@gmail.com"):
     print("Email address incorrecto intente otra vez")
     logIn()
    
    elif (pwd != "Final"):
        print("Password address incorrecto intente otra vez")
        logIn()
    else:
         print("Opcion no valida intente otra vez")
         logIn()
            
def welcome():
     ask3 = int(input("Ingrese (#1) para ir a menu o (#2)para ir a reservas. "))
     if (ask3 == 1):
             print(menu())
     elif (ask3 == 2):
             print(Reservas())
     else:
          print("Opcion no valida intente otra vez")
          print(welcome())



def Reservas (): 

    print(days())

def days():
    dia = int(input("Estos son los dias para sacar la cita del test: \n (#1)- Lunes \n (#2)- Martes \n (#3)- Miercoles \n (#4)- Jueves \n (#5)- Viernes \n (#6)- Sabado \n (#0)- (Ingrese 0 para devolverse) \n Por favor degite el numero del dia que deseas escoger: "))

    if dia == 1:
        print("Has escogido el dia Lunes")
        print(hora())

    elif dia == 2:
        print("Has escogido el dia Martes")
        print(hora())

    elif dia == 3:
        print("Has escogido el dia Miercoles")
        print(hora())

    elif dia == 4:
        print("Has escogido el dia Jueves")
        print(hora())

    elif dia == 5:
        print("Has escogido el dia Viernes")
        print(hora())

    elif dia == 6:
        print("Has escogido el dia Sabado")
        print(hora())

    elif dia == 0:
        print(menu())


        
def hora ():
    print("Estos son los horario: \n #1-(09:00am a 11:00am) \n #2-(12:00pm a 02:00pm) \n #3-(03:00pm a 05:00pm) \n #0-(Ingrese 0 para devolverse)" )
    horas =int(input(" Por favor degite el numero del horario que deseas escoger: "))
        
    if horas == 1:
                print("Has escogido el horario de 09:00am a 11:00am")

                people = int(input("Ingrese la cantidad de personas que asitiran al test:"))
                if (people >= 1) :
                    print("Su cita a sido agendada el dia Lunes a las 09:00am a 11:00am. Numero de reservacion es #01 " )
                else:
                    if people==2:
                         print("Lo sentimos no hay espacio, elige otro horario")
                         print(hora())


    elif horas == 2:
                print("Has escogido el horario de 12:00am a 02:00am")

                people = str(input("Ingrese la cantidad de personas que asitiran al test:"))
                if (people > "2") and (people < "3") :
                    print("Su cita a sido agendada el dia Lunes a las 12:00am a 2:00am. Numero de reservacion es #02 " )
                else:
                    print("Lo sentimos no hay espacio, elige otro horario")
                    print(hora())


    elif horas == 3:
                print("Has escogido el horario de 03:00am a 5:00am")

                people = str(input("Ingrese la cantidad de personas que asitiran al test:"))
                if (people > "3") or (people < "5") :
                    print("Su cita a sido agendada el dia  a las 09:00am a 11:00am. Numero de reservacion es #03 " )
                else:
                    print("Lo sentimos no hay espacio, elige otro horario")
                    print(hora())


    elif horas == 0:
        print(days())
    else:
        print("El opcion ingresada no se encuentra") 
        print(hora())  


def moduloInformes():
    print("Las opciones disponibles para la vista de *Admin* son las siguientes","\n",
           "Cantidad de personas, Digite 1 para ver esta opcion""\n", "Cantidad de Dinero generado , Digite 2 para ver esta opcion"
           "\n", "Cantidad de Afluencia, Digite 3 para ver esta opcion"
           "\n", "Horario con menor cantidad de personas, Digite 4 para ver esta opcion"
           "\n", "Horario con mayor cantidad de personas, Digite 5 para ver esta opcion")
    cantidadPersonas=("#.txt, que guarde por condicion e imprima cada uno")
    cantidadDinero=("#.txt que guarde el dinero generado por dia")
    cantidadAfluencia=("#.txt que guarde la cantidad de afluencia por dia")
    horarioMenor=("#.txt que guarde la cantidad de horas con menor cantidad de personas  por dia")
    horarioMayor=("#.txt que guarde la cantidad de horas con mayop cantidad de personas  por dia")
     

#print(menu())
#Da error por la concatenacion mal

def menu ():
     ask1 = str(input("Main menu: \n 1- Login. \n 2- Reservas. \n 3- Facturacion. \n 4- Informes. \n Por favor digite el numero de la opcion que deseas escoger: "))
     while ask1 != "0":
        if (ask1 == "1"):

            print("Has selecionado la opcion login")
            print(logIn())

        elif (ask1 == "2"):

            print("Has selecionado la option reservas")

            print(Reservas())

        elif (ask1 == "3"): 

            print("Has selecionado la opcion facturacion")
            print(Facturacion()) 

        elif (ask1 == "4"):

            print("Has selecionado la option informes")
            print(Informes())

        else:
            print("Lo sentimos la opcion ingresada no se encuentra, por favor intente otra vez:")  
            b= menu()         




menu()