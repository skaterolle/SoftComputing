# Inicio variables globales
Conjunto_Reglas_5 = "Reglas_5.dat"
Conjunto_Reglas_3 = "Reglas_3.dat"

def read_file_5(File):
    f = open(File, "r")
    lista = []
    while True:
        line = f.readline()
        if not line:
            break
        if line[0] != '@':
            numero = [float(x) for x in line.rstrip('\n').split(',')]
            lista.append(numero)
    f.close()
    return lista

def read_file_3(File):
    f = open(File, "r")
    lista = []
    while True:
        line = f.readline()
        if not line:
            break
        if line[0] != '@':
            numero = [float(x) for x in line.rstrip('\n').split(',')]
            numero.pop(3)
            numero.pop(4)
            lista.append(numero)
    f.close()
    return lista

def write_fileT(File, list):
    f = open(File, "w")
    for x in range(len(list)):
        for y in range(len(list[x])):
            f.write(str(list[x][y]))
            if y < (len(list[x]) - 1):
                f.write(", ")
        f.write("\n")

def write_file(File, list):
    f = open(File, "a")
    for x in range(len(list)):
        for y in range(len(list[x])):
            f.write(str(list[x][y]))
            if y < (len(list[x]) - 1):
                f.write(", ")
        f.write("\n")
    f.close()

def prueba1(File):
    Reglas_Iniciales = []
    Iguales = []
    Reglas_Iniciales = read_file_5(File)
    Iguales = read_file_5(Conjunto_Reglas_5)
    porcentaje = 0
    for i in range(len(Reglas_Iniciales)):
        Regla = Reglas_Iniciales[i]
        encontrado = False
        if porcentaje < int((i*100)/len(Reglas_Iniciales)):
            porcentaje = int((i*100)/len(Reglas_Iniciales))
            print("Calculando Reglas: ", porcentaje, "%")
        for j in range(len(Iguales)):
            Igual = Iguales[j]
            if set(Regla) == set(Igual):
                encontrado = True
        if not encontrado:
            Iguales.append(Regla)
    write_fileT(Conjunto_Reglas_5, Iguales)
    print("Relgas Totales: ", len(Iguales))

def prueba2(File):
    Reglas_Iniciales = []
    Iguales = []
    Reglas_Iniciales = read_file_3(File)
    Iguales = read_file_5(Conjunto_Reglas_3)
    porcentaje = 0
    for i in range(len(Reglas_Iniciales)):
        Regla = Reglas_Iniciales[i]
        encontrado = False
        if porcentaje < int((i*100)/len(Reglas_Iniciales)):
            porcentaje = int((i*100)/len(Reglas_Iniciales))
            print("Calculando Reglas: ", porcentaje, "%")
        for j in range(len(Iguales)):
            Igual = Iguales[j]
            if set(Regla) == set(Igual):
                encontrado = True
        if not encontrado:
            Iguales.append(Regla)
    write_fileT(Conjunto_Reglas_3, Iguales)
    print("Relgas Totales: ", len(Iguales))

#f = open(Conjunto_Reglas_5, "w")
f1 = open(Conjunto_Reglas_3, "w")
#f.close()
f1.close()
prueba2("training/delta_ail-5-1tra.dat")
prueba2("training/delta_ail-5-2tra.dat")
prueba2("training/delta_ail-5-3tra.dat")
prueba2("training/delta_ail-5-4tra.dat")
#prueba1("training/delta_ail-5-5tra.dat")


