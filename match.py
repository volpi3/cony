def suma2(n1,n2):
    print(f"el resultado de la suma es {n1}+{n2}")
def suma():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print(f"el resultado de la suma es, {n1}+{n2}")
def resta():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print(f"el resultado de la resta es, {n1}-{n2}")
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
     op=int(input("""sleccione una opcion
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
                resta("el resultado de la suma es" )
            
            case 3:
                multiplicacion()
            case 4:
                divicion()
            case 5:
                break
            case _:
                print("opcion no valida")
                



            
     

      


            
    


