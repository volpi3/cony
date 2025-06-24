#crud de diccionario 

def act_juego(dict):
    mostrar_juegos(dict)
    act=int(input("seleccione el juego que quiere actualizar "))
    while True:
        print('''1.- nombre
              2.- precio
              3.- codigo
              4.- salir
              ''')
        dato=int(input("ingrese la opcuio que quiere actializar "))
        match dato:
            case 1:
                n=input("ingrese el nuevo nombre")
                dict[act]["nombre"]=n
            
            case 2:
                n=input("ingrese el precio nuevo ")
                dict[act]["precio"]=n
            case 3:
                n=input("ingrese el codigo nuevo ")
                dict[act]["codigo"]=n
            case 4:
                print("saliendo")
                break
            case _:
                prit("seleccione una opion valida")
def mostrar_juegos(juegos):
    for j, datos in juegos.titems():
                print(j,datos)
def borar_juego(dict):
    mostrar_juegos(dict)
    borar=int(input("seleccione l juego que quiere borar"))
def valida_code(clave):
    mayuscula=0
    minuscula=0
    numero=0
    for palabra in clave:
        if palabra.isupper():
            mayuscula+=1
        if palabra.islower():
            minuscula+=1
        if palabra.isdigit():
            numero+=1
def agre_juego(dic):

        
        ultima=list(dic.keys())[-1]
        nombre=int(input("ingrese el nombre del juego "))
        precio=int(input("ingrese el precio "))
        while True:
            code=int(input("ingrese un codigo "))
            if valida_code(code):
                dic[ultima+1]={
                "nombre":nombre,
                "precio":precio
                }
                print("juego ingresado con exito ")
                break
            else:
                print("codigo invalido deve ingresar 2 mayusculas 2 minusculas ")

juegos={1:{"nombre": "planta vs zombies",
       "precio": 1500,
       "codigo": "Dphh06"},
        2:{"nombre": "mario cars",
        "precio": "8000",
        "codigo": "BDil77"}
    }
while True:
    print('''
          1.- agregar juego
          2.- mostrar juego 
          3.- actualizar juego
          4.-borar juego 
          5.-salir
           ''')
    op=int(input("ingrese una opcion"))
    match op:
        case 1:
            agre_juego(juegos)
          
        case 2:
            mostrar_juegos(juegos)
        case 3:
            act_juego(juegos)
        case 4:
            borar_juego(juegos)
        case 5:
             print("saliendo del programa")
             break
        case _:
            print("opcion inavlida")


