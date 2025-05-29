#     -5 -4 -3 -2 -1
# lista=[1, 5, 7, 10,16]
# #      0 1 2 3 4 5
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

notas=[55,67,34,70,13]
cnot=0
suma=0
ifnotas>=40:
    print("usted tiene buena nota")
else:
    print("usted tiene un rojo")
for num in notas:
    suma+=num
    cnot+=1
prom=suma/cnot

print("el promerdio es ",round (prom))
# if notas>=40:
#     print("usted tiene buena nota")
# else:
#     print("usted tiene un rojo")

