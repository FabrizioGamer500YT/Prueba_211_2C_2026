#########GER############
def funcion(nombre):
    print(nombre)

def otra_funcion(nombre):
    print(f"Su nombre es: {nombre}")

#########GONZA#############

def incrementar(w):
    w += 5
    print(f"Durante de la fx {(w)}") #15 
    return w

x = 10
print(f"Antes de la fx {(x)}") # 10
x = incrementar(x)
print(f"Despues de la fx {(x)}") # 10
