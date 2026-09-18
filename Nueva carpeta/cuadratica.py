# def resolver_chicharronera(a: float, b: float  , c: float = 0) -> float|tuple|None:
#     """Obtiene las soluciones de una ecuación de segundo grado

#     Args:
#         a (float): coeficiente cuadratico
#         b (float): coeficiente lineal
#         c (float, optional): termino independiente. Defaults to 0.

#     Returns:
#         float: encuentra 1 solucion | 
#         tuple: encuentra 2 soluciones |
#         None: cuando no existe solucion
#     """
#     discriminante = b**2 - (4 * a * c)

#     if discriminante < 0: # no hay raices
#         solucion = None
#     elif discriminante > 0: # hay 2 raices
#         #x1, x2
#         x1 = (-b + discriminante ** 0.5) / 2 * a
#         x2 = (-b - discriminante ** 0.5) / 2 * a
#         solucion = x1, x2
#     else: # hay una sola raiz
#         solucion = -b / 2 * a

#     return solucion

# #####################################################

# cuadratico = 1
# lineal = 4



# resultado = resolver_chicharronera(cuadratico, lineal,-5 ) # posicional
# print(resultado)

# resultado = resolver_chicharronera(b = lineal, c = independiente, a = cuadratico)
# print(resultado)





# def dibujar_boton(texto, ct, cts, cf, cfs, cb, cbs):
#     pass

# dibujar_boton("Presioname", 
#               cb = "rojo", 
#               ct = "azul", 
#               cf = "rosa", 
#               cbs  = "negro", 
#               cfs = "gris",
#               cts = "verde")


    # """Obtiene las soluciones de una ecuación de segundo grado

    # Args:
    #     a (float): coeficiente cuadratico
    #     b (float): coeficiente lineal
    #     c (float): termino independiente

    # Returns:
    #     float: encuentra 1 solucion | 
    #     tuple: encuentra 2 soluciones |
    #     None: cuando no existe solucion
    # """

# def saludar(nombre, mensaje = None):
#     if mensaje != None:
#         print(f"{nombre}, {mensaje}")
#     else:
#         print(f"Hola {nombre}, te doy la bienvenida")

# # saludar("Gonzalo", "como estas?")
# saludar("Gonzalo")


def saludar(nombre, apellido, es_formal = False):
    if es_formal == True:
        print(f"Buenas tardes: {apellido}, {nombre}. Como esta ud?")
    else:
        print(f"Hola {nombre}... Sos un genio!!!")

saludar("Pedro", "Ruiz", True)