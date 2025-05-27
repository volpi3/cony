# Crear un programa con un menú que permita al usuario:
# Comprar un café (3 tipos: espresso $3.000, latte $4.000, capuccino $4.500)
# Ver ventas del día (número de cafés vendidos, total recaudado, bebida más cara vendida)
# Salir
# expreso=0
# latte=0
# capuchino=0
# venta=0
# cafe_vendidos=0
# def menu_cafe ():
#     global expreso, latte, capuchino, venta, cafe_vendidos
#     while True:
#         op=int(input('''hola buenas que cafe va a querer
#                  1.-capuchino $4.500
#                  2.-latte $4.000
#                  3.-expreso $3.000
#                  4.-ninguno
#                  '''))
#         match op:
#             case 1:
#                  venta+=4500
#                  cafe_vendidos+=1
#                  capuchino+=1
#                  print("usted compro  un capuchino")
#             case 2:
#                 venta+=4.000
#                 cafe_vendidos+=1
#                 latte+=1
#                 print("usted compro  un latte")
#             case 3:
#                 venta+=3.000
#                 cafe_vendidos+=1
#                 expreso+=1
#                 print("usted compro  un expreso")
#             case 4:
#                 break
                
#             case _:
#                 print("opcion invalida")
                
# def ventas_diarias():
#       print(f'''ventas totales ${venta}
#             Num de cafes {cafe_vendidos}
#             ''')
#       if capuchino>=1:
#         print("el monto mas alto fue de $4500")
#       elif latte>=1:
#          print("el monto mas alto fue de $4000")
#       elif expreso>=1:
#          print("el monto mas alto fue de $3000")

# Hay 3 tipos de entradas:
# VIP: $12.000
# Normal: $8.000
# Niño: $5.000
# El resumen de ventas debe mostrar:
# Total de entradas vendidas
# Total recaudado
# Tipo de entrada más vendida


vip=0
normal=0
niño=0
ventas=0
entradas_vendidas=0
def venta_entradas():
    global vip , normal, niño, ventas, entradas_vendidas
    while True:
        op=int(input('''que entrada va a querer 
                     1.- vip $12000
                     2.- normal $8000
                     3.- niño $5000
                     4.- salir
                     '''))
        match op:
            case 1: 
                ventas+=12000
                entradas_vendidas+=1
                vip+=1
                print("usted compro la etrada vip")
            case 2: 
                ventas+=8000
                entradas_vendidas+=1
                normal+=1
                print("usted compro la etrada normal")
            case 3: 
                ventas+=5000
                entradas_vendidas+=1
                niño+=1
                print("usted compro la etrada niño")
            case 4:
                break
            case _:
                print("opcion invalida")
def ventas_diarias():
    print(f'''ventas del dia 
          1.- total recaudado, {ventas}
          2.-total entradas vendidas {entradas_vendidas}  
          3.- vip  vendidas {vip}  
          4.- normal vendidas {normal}
          5.- niño vendidas {niño}  
          ''')
    if vip > 0:
        print("el monto mas alto pagado fue de $12000")
    elif normal > 0:
        print("el monto mas alto pagado fue de $8000")
    elif niño > 0:
        print("el monto mas alto paado fue de $5000")
    else:
        print("no se ha vendido ninguna entrada")
while True:
    op=int(input('''elia una opcion 
1.- comp entradas 
2.- ventas del dia 
3.-salir
opcion: '''))
    match op:
        case 1:
            venta_entradas()
        case 2:
            ventas_diarias()
        case 3:
            print("Gracias por usar el sistema de venta de entradas.")
            break
    





    



            
            




