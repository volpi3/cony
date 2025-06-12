#        -5-4 -3  -2 -1
# lista=[1, 5, 7, 10,16]
# #      0  1  2   3  4  
# print(lista[4]) #acceso a valor por indice  positivo
# print(lista[-5]) #acceso a valor por indice  positivo

# notas=[55,67,34,70,13]
# cnot=0
# suma=0
# for num in notas:
#     suma+=num
#     cnot+=1
# prom=suma/cnot
# print("el promerdio es ",round (prom))

# nombre=["cony","franco",""]
# apellido=["volpi", "troncoso"]
# print(len(nombre) )#

# for i in range (len(nombre)):
#     print(f"su nombre es {nombre[i]} {apellido[i]}")

# frutas=["granada","piña","sandia"]
# for fruta in frutas:
#     print(f"la {fruta} tiene {len(frutas)} caracterer")
# autos=["audi","toyota","BWM","KIA","mercedes"]
# for auto in autos:
#     print(auto)
#     if "a" in auto.lower():
#         print("la marca tiene una a")
#     else:
#         print("ni una a encontada")

# notas=[55,67,34,70,13]
# cnot=0
# suma=0
# if notas>=40:
#     print("usted tiene buena nota")
# else:
#     print("usted tiene un rojo")
# for num in notas:
#     suma+=num
#     cnot+=1
# prom=suma/cnot

# print("el promerdio es ",round (prom))
# if notas>=40:
#     print("usted tiene buena nota")
# else:
#     print("usted tiene un rojo")

# frutas={"manzana","frambueza","durazno"}

# for frutas in frutas:
#     print(frutas)

# numero=[1, 5, 7, 10,16]

# print(len(numero))
# print(numero)
# numero.append(20)#append agrega un numero a la lista 
# print(numero)#muestra el numero agregado 

# nombre=[]
# while True:
#     print('''
#           1.- Ingrese Nombre
#           2.- Salir
#           ''')
#     op=int(input(" seleccione una opcion "))
#     match op:
#         case 1:
#             nom=input(" ingrese un nombre ")
#             nombre.append(nom)   
#             print(nombre)
#         case 2:
#             print(" saliendo... ")
#             break
#         case _:
#             print(" opcion invalida ")
# nombre=["Diego"]
# apellido=["Robles"]
# while True:
#     print('''
#           1.- Ingrese Nombre y apellido 
#           2.- buscar nombre
#           3.- mostrar nombre
#           4.-salir
#           ''')
#     op=int(input(" seleccione una opcion "))
#     match op:
#         case 1:
#             nom=input(" ingrese su nombre ")
#             ape=input(" ingrese su apellido ")
#             nombre.append(nom)  
#             apellido.append(ape) 
#         case 2:
#             buscar=input("ingrese el nombre que busca")
#             if buscar in nombre:
#                 print(f"el nombre {buscar} se encuentra en la lista")
#             else:
#                 print(f"el nombre {buscar } no se encuentra en la lista")
          
#         case 3:
#             for i in range(len(nombre)):
#                 print( nombre[i], apellido[i])
        
#         case 4:
#             print ("saliendo del programa")
#             break
#         case _:
#             print("opcion invalida")

# productos=["mojito", "tequila margarita", "piña colada"]
# precios=["6000","7500","6500"]
# carro=[]
# while True:
#     print('''
#           1.- Ingrese productos
#           2.- comprar
#           3.- crear boleta
#           4.-salir
#           ''')
#     op=int(input(" seleccione una opcion "))
#     match op:
#         case 1:
#               nom=input(" ingrese un producto ")
#               productos.append(nom)
#               pre=int(input("ingrese el precio"))
#               precios.append(pre)   
#         case 2:    
#                 for i in range(len(productos)):
#                     print(f"{i+1} .- {productos[i]} $ {precios[i]}")
#         case 3:
#               print()
              
#         case 4:
#               print("salir del super")
#               break
#         case _:
#               print("opcion invalida")

notas=[5.4, 1.0 ,7.0]
while True:
    print(''' programa de notas 
          1.-Ingrese sus notas
          2.-Borrar nota
          3.-Mostrar notas
          4.-sacar promedio, nota mayor y nota menor 
          5.-limpiar todas las notas 
          6.-salir
          ''')
    op=int(input("selecione una opcion "))
    match op:
        case 1:
            nota=float(input("ingrese su nota "))
            notas.append(nota)
        case 2:
             for i in range(len(notas)):
                     print(f"{i+1} .- {notas[i]} ")
             elim=int(input("ingrese la nota que quiere eliminar"))
             notas.pop(elim-1)
        case 3:
              print(notas)
        case 4:
              print(f"su promedio es:{sum(notas)/len(notas)}\n su nota mayor es {max(notas)} y su nota menor es {min(notas)}")
             
        case 5:
              notas.clear()
              print("las notas fueron eliminadas")
              
        case 6:
            print("salir del programa ")
            break
        case _:
            print("opcion invalida ")
        

                       
                    
                        

              
            
          
    
