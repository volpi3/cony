# #declaracion de variables
# nombre="cony"
# edad=20
# # ejemplo de contatenacion 
# print("hola", nombre,"y su edad es", edad )
# print ("ingrese su nombre")
# nombre=input()

# n1=int(input("ingrese un numero"))
# n2=int(input("ingrese un numero"))
# print("el resultado de la suma es",  n1+n2)

def suma2(n1,n2):
    print("el resultado de la suma es ",n1+n2)
def suma():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print(f"el resultado de la suma es, {n1}+{n2}")
def resta():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print(f"el resultado de la suma es, {n1}-{n2}")
def multiplicacion():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print(f"el resultado de la suma es, {n1}*{n2}")
def divicion():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print(f"el resultado de la suma es, {n1}/{n2}")

def calculadora():
   while True:
     op=int(input("""sleccione unaopcion
             1.- suma
             2.- resta 
             3.- multipicacion 
             4.-division
             5.- salir
              """))
     match op:
            case 1:
                suma()
            case 2:
                resta()
            case 3:
                multiplicacion()
            case 4:
                divicion()
            case 5:
                print("salir")
                break
            case _:
                print("opcion no valida")