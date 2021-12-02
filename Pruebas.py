import pickle
from statistics import mean

# Abre los ficheros que quiera usar
f = open("training/delta_ail-5-1tra.dat","r")
f1 = open('Reglas-iniciales.txt', 'w') 

def cl_files(): # Cierra todos los ficheros que uso
    f.close()
    f1.close()

def media(dataset):
    return sum(dataset) / len(dataset)



Triangulos = []
Iguales = []
with f as file:
    while True:
        line = file.readline()
        if not line:
            break
        if line[0] != '@':
            Triangulos.append(line.rstrip('\n').split(','))
            f1.writelines(line)


compara = Triangulos[1]
media = 0
Rollrate = []

for i in range(len(Triangulos)):
    if Triangulos[i][5] == compara[5]:
        Iguales.append(Triangulos[i])
        Rollrate.append(Triangulos[i][0])

#print(Rollrate)
valor = 0
# Tengo que guardarlo en Rollrate como números no como Strings
valor = mean(Rollrate)
print("Media aritmética de Rollrate: ",valor)
print(len(Iguales))
cl_files()


print("Triangulos: ",len(Triangulos))
print("Terminado-------------------")

#ListTriangulos = []
# for i in range(13):
#     if i > 9:
#         #Triangulos.append(f.readline().split(','))
#         # Meto lo que leo del fichero dentro de mensaje sin el salto de línea y cortando por las comillas
#         mensaje = f.readline().rstrip('\n').split(',')
#         print(mensaje)
#         # Meto cada línea en una lista nueva dentro de Triangulos
#         Triangulos.append(mensaje)
#         #ListTriangulos.append(Triangulos)
#         #print(f.readline().split(','))
#     else:
#         print(f.readline())
#print(Triangulos)
# Este código lee cada entrada del documento
# with open('training/delta_ail-5-1tra.dat') as openfileobject:
#     for line in openfileobject:
#         Triangulos.append(line.rstrip('\n').split(','))
#         with open('parseado.txt', 'a') as f1:
#             f1.writelines(line)
#             f1.close()

#with open('parseado.txt', 'w') as f:
    # Solo sirve para guardar str
    #f.write('Doe, a deer, a female deern')
    # Para guardar listas sin anidamiento
    # f.writelines(Triangulos)
#print(Triangulos)


# El data_set tiene que ser el de 5-folds, 4 de entrenamiento y 1 final, así se hacer el 80/20
# Se lee todo el dataset y todo eso son relgas y ahora habrá que afinarlas con las que más se parezcan
# La primera vuelta será para meter todos los parametros como reglas
# Las siguientes vueltas habrá que comprobar cada una de las entradas con las demás para buscar si hay parecidas y afinar las reglas
# Cuando termine, hacer otra para ver si todo está correcto y ya con ello hacer la tabla