# #dicionario es un conjunto de pares de datos
# dic={"nombre ": "elizabeth", "numero ":961383599, "casado ":True }
# print(dic)
# dic["nombre "]="elizabeth troncoso "
# print(dic)
# dic["ciudad"]="Italia"
# print(dic)
# frutas={"naranja":500, "manzana": 900, "granada":1500}
# print(frutas)
# frutas["mandarinas"]=1200
# print(frutas)
# for kay,value in frutas.items():
#     print(kay, "$ ",value)

# productos={{"nombre":"lapiz"},{"nombre":"goma"}}
# print(productos[1]["nombre"])

# '''
# 1.-Agregar articulo
# 2.-borar articulo
# 3.- actualizar articulo
# 4.-mostrar lista de articulos
# 5.-salir
# '''
def agregar(lista):
     agre=input("agrege articulo")
     precio=int(input("ingrese el precio"))
     lista.append({"nombre":agre,"precio":precio})
def muestra_lista(lista):
     for i,articulo in enumerate(lista):
                 print(i+1,articulo["nombre"],articulo["precio"])
def borar_art(lista):
        muestra_lista(lista)
        elim=int(input("ingrese articulo que quiere eliminar"))
        lista.pop(elim-1)
art=[{"nombre":"cuaderno","precio":2200},{"nombre":"estuche","precio":2500},{"nombre":"lapiz gel","precio":3000}]
while True:
    print('''
          1.-Agregar articulo
          2.-borar articulo
          3.- actualizar articulo
          4.-mostrar lista de articulos
          5.-salir
          ''')
    op=int(input("ingrese una opcion"))
    match op:
        case 1:
            agregar(art)
        case 2:
            borar_art(art)
        case 3:
              for i,articulo in enumerate(art):
                print(i+1,articulo["nombre"],articulo["precio"])

        case 4:
            muestra_lista(art)
                
        case 5:
            print("saliendo..")
            break
        case _:
            print("opcion invalida ")
# ######## terminar programa #####
personas={
     1:{"nombre":"elizabeth troncoso",
        "telefono":6587468,
        "estado civil":"soltero",
        "ciudadano":False}
        }
#########
personas={{ }}
while True:
     try:
          print('''
                1.-ingresar persona
                2.-mostrar listado
                3.-actualizar persona
                4.-borrar persona
                5.- salir
                ''')
          op=int(input("ingrese una de las opciones"))
          match op:
               case 1:
                    nom=input("ingrese su nombre")
                    tel=int(input("ingrese su numero"))
                    est=int(input("1.-casado, 2.-soltero"))
                    if est==1:
                         estcivil="casado"
                    else:
                         estcivil="soltero"
                    est=int(input(" Es usted ciudadano 1.-si 2.-no"))
                    if est==1:
                         ciuda=True
                    else:
                         ciuda=False
                    ld=len(personas)+1
                    personas[ld]={"nombre":nom,
                                 "telefono":tel,
                                 "ciudadano":ciuda}
               case 2:
                    for n, personas in personas.items():
                     print(n, personas)
                    
               case 3:
                    for n, personas in personas.items():
                     print(n, personas)
                    perso=int(input('''
                        1.-nombre
                        2.-numero
                        3.-estado civil
                        4.-ciudadano
                        5.- salir
                        '''))
                    dato=int(input("que dato desea actualizar"))
                    personas[perso][dato]
                  
               case 4:
                    for n, personas in personas.items():
                        print(n, personas)
                    elim=int(input("que persona quiere borar"))
                    personas.pop(elim-1)
                    del personas[elim]
                    print(f"la persona {elim} fue eliminada")
               case 5:
                    print("saliendo..")
                    break
               case _:
                    print("opcion invalida")
     except Exception:
          print("agrege una opcion numerica")
