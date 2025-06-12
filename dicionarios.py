#dicionario es un conjunto de pares de datos
dic={"nombre ": "elizabeth", "numero ":961383599, "casado ":True }
print(dic)
dic["nombre "]="elizabeth troncoso "
print(dic)
dic["ciudad"]="Italia"
print(dic)
frutas={"naranja":500, "manzana": 900, "granada":1500}
print(frutas)
frutas["mandarinas"]=1200
print(frutas)
for kay,value in frutas.items():
    print(kay, "$ ",value)