#crear un menu de carrito con las siguentes opciones 
#1.- ingresa el nombre del usuario 
#sera mostrado em la boleta con un saludo 
#2.-comprar poner productos para poder comprar 
#con su precio correspondiente 
#3.-sacar boleta calcular el precio neto 
#y el precio mas iva, mostrar totale 
#4.- salir 
#consideraciones:
#por lo menos 3 productos 
#no hya limite de compra 
#se puede salir en cualquier momento 
# los montos de los productos son
total=0
carrito=0
def new_func():
    op=int(input)
    return op

while True:
        print('''
        1. ingrese su nombre 
        2.comprar productos 
        3.mostrar boleta
        4. salir 
        ''')
     
        op =int(input())
        match op:
            case 1:
                nombre=input("ingrese su nombre:")
                        
            case 2:
                while True:
                    print('''
                            1.- manzana $ 500
                            2.-  pera $ 700
                            3.- platano $1.000
                            4.- volver al menu principal
                            ''')
                    productos=int(input())
                    if productos==1:
                        total+=500
                        carrito+=1
                    elif productos==2:
                        total+=700
                        carrito+=1
                    elif productos==3:
                        total+=1.000
                        carrito+=1
                    elif productos==4:
                    
                        break
                    else:
                        print("opcion invalida")
            case 3: 
                print(f'''
                 hola {nombre}
                 la cantidad de productos que lleva es {carrito}
                 el total neto es {total}
                 el total con iva es {total*1.19}
                 ''')
            case 4:
                break

            case _:
             print("opcion invalida")
                                    
        
                
    

# pedir cantidad de alumnos 
#pedir notas por cada alumno 
#promedia a cada alumno 
#y muestra si aprieba o reprueba
# bonus mostrar promedio de todos los alumnos 
# ingresad
print

# ingrese cant de alumnos: 5
# ingrese cantidad de notas del alimno 1:3 
#ingrese nota 1 del alumno 1 
# #ingrese nota 2 del alumno 1 
#ingrese nota 3 del alumno 1 
# el promedio del alumno es: 5,6
# alumno 1 aprobo 
#ingrese la nota 1 del alumno 2 



