# def suma_ret():
#     n1=int(input("ingrese un numero" ))
#     n2=int(input("ingrese un numero" ))
#     return n1+n2
# '''realizar una funcion que calcule el IVA
# realizar otra funcion que al pasarle el precio y un numero 
# como porcentaje (eje 20)
# calcule el descuento y muestre el valor final 

# '''argumento=dato que va dentro del parentesis

def IVA(num):
    print(num*1.19)
n=int(input("ingrese un numero "))
IVA(n)


def descuento(desc):
    descuento=desc*0.2
    print(desc-descuento)

descuento(6000)