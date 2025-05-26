
#iterar una lista de elementos f


# for numero in range (5):
#     print(numero+1)
# buscar =10
# for numero in range (10):#iterable
#     print(numero)
#     if numero==buscar:
#         print("encontrado",buscar)
#         break # detiene la iteracion del scrip se queda hasta el 
# # else:
#     print("no encontre el  numeor buscado")
# for char in "elizabeth troncoso":
#     print(char)
####
# numero = 1 
# while numero < 100:
#     print(numero)
#     numero *= 2
# comando = ""
# while comando!="salir":
#     comando = input("$")
#     print(comando)
# lop infinitos 
# while True:
    # comando= input("$")
    # print(comando)
    # if comando== "salir":
    #     break
# loop anidados 

# for j in range (3):
#     for k in range (3):
#         print(F"{j+1} , {k+1}")
#########
# print("bienbenido a la calculadora ")
# print("para salir escribe salir")
# print(" la opciones son suma, reta,multi y div ")
# num1=int(input( "ingrese un numero "))
# opcion=input("ingrese que operacion quiere (suma,resta,multi,div): ")
# num2=int(input( "ingrese otro numero "))
# print("bienbenido a la calculadora ")
# print("para salir escribe salir")
# print("la opciones son suma, reta,multi y div ")
resultado=""
def calcu():
    while True:
        if not resultado:
            resultado=input("ingrese un numeor ")
            if resultado =="salir":
                break
            resultado=int(resultado)
        opcion=input("ingrese una operacion: ")
        if opcion=="salir":
            break
        n2 = input("ingrese el segundo numero")
        if n2=="salir":
            break
        n2 =int(n2)
        if opcion=="suma":
            resultado+=n2
        elif opcion=="resta":
            resultado-=n2
        elif opcion=="multi":
            resultado*=n2
        elif opcion=="div":
            resultado/=n2
        else:
            print("operacion incorrecta")
            break
        print(f"el resultado es {resultado}")
        

# resultado=""
# while True:
#     if not resultado:
#         resultado=input("ingrese un numeor ")
#         if resultado =="salir":
#             break
#         resultado=int(resultado)
#     opcion=input("ingrese una operacion: ")
#     if opcion=="salir":
#         break
#     n2 = input("ingrese el segundo numero")
#     if n2=="salir":
#         break
#     n2 =int(n2)
#     if opcion=="suma":
#         resultado+=n2
#     elif opcion=="resta":
#         resultado-=n2
#     elif opcion=="multi":
#         resultado*=n2
#     elif opcion=="div":
#         resultado/=n2
#     else:
#         print("operacion incorrecta")
#         break
#     print(f"el resultado es {resultado}")
        









