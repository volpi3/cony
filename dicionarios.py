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


