
f = open("training/delta_ail-5-1tra.dat","r")
Triangulos = []
#ListTriangulos = []
for i in range(13):
    if i > 9:
        #Triangulos.append(f.readline().split(','))
        # Meto lo que leo del fichero dentro de mensaje sin el salto de línea y cortando por las comillas
        mensaje = f.readline().rstrip('\n').split(',')
        print(mensaje)
        # Meto cada línea en una lista nueva dentro de Triangulos
        Triangulos.append(mensaje)
        #ListTriangulos.append(Triangulos)
        #print(f.readline().split(','))
    else:
        print(f.readline())
#print(Triangulos)
f.close()

# El data_set tiene que ser el de 5-folds, 4 de entrenamiento y 1 final, así se hacer el 80/20
# Se lee todo el dataset y todo eso son relgas y ahora habrá que afinarlas con las que más se parezcan
# La primera vuelta será para meter todos los parametros como reglas
# Las siguientes vueltas habrá que comprobar cada una de las entradas con las demás para buscar si hay parecidas y afinar las reglas
# Cuando termine, hacer otra para ver si todo está correcto y ya con ello hacer la tabla