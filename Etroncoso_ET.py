productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}
# Pybooks le solicita lo siguiente:
# Un menú que tenga las siguientes opciones
# *** MENU PRINCIPAL ***
# 1. Stock marca.
# 2. Búsqueda por precio.
# 3. Actualizar precio.
# 4. Salir

def búsqueda_preci(precio_minimo,precio_maximo):

    try:
                    while True:
                        precio_minimo=int(input("ingrese el precio minimo "))
                        precio_maximo=int(input("ingrese el precio maximo "))
                        if precio_minimo>precio_maximo:
                            print("el precio minimo no puede ser mayor que el precio maximo ")
                            break
                        rango=[]
                        for modelo, dat_stock in stock.items():
                            precio=dat_stock[0]
                            if precio_minimo <= precio_maximo:
                                marca=productos[modelo][0]
                            rango.append((marca + ".-" + modelo + precio))
                            if rango:
                                rango.sort()
                                print("/nModelos encontados en el rango del precio ")
                                for item in rango:
                                    print(f"modelo:{item[0]} - precio:{item[1]} ")
                            else:
                                print("no hay notbuck en el rangode os precios ingresados ")
    except ValueError:
                print("ERROR debe ingresar valores enteros")
def actualizar_precio(modelo):
     modelo=int(input("ingrese que modelo desea actualizar ")).strip().upper()
     if modelo in stock:
            nuevo_precio=int(input("ingrese el precio ah actualizar"))
            if nuevo_precio( modelo, nuevo_precio):
                print("precio actualizado ")
            else:
                print("el modelo no existe ")
     
while True:
    try:
        print('''
            1.- Stock marca
            2.- Buqueda por precio
            3.- actualizar precio
            4.- salir
            ''')
        op=int(input("ingrese una opcion "))
        match op:
            case 1 :
                for i,n in stock.items():
                    print(i,n)

            case 2 :
                  búsqueda_preci()
               
            case 3 :
                actualizar_precio()
            case 4 :
                print("saliendo el programa ")
                break
            case _:
                print("opcion incorrecta")
    except Exception as e:
        print ("ingrese una opcion valida ")

       # precio_minimo=float(input("ingrese el precio minimo "))
                # precio_maximo=float(input("ingrese el precio maximo "))