

def read_file(File):
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


def write_fileT(File, list):
    f = open(File, "w")
    for x in range(len(list)):
        for y in range(len(list[x])):
            f.write(str(list[x][y]))
            if y < (len(list[x]) - 1):
                f.write(", ")
        f.write("\n")

def comparacion_mayor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def comparacion_menor(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

def etiqueta(num1, T):
    if num1 > T[0] and num1 < T[1]:
        return "Bajo"




def etiquetado(Regla, min_max):
    AT1 = []
    Div = (min_max[1] - min_max[0])/5
    AT1 = [min_max[0] , min_max[0] + Div, min_max[0] + Div*2, min_max[0] + Div*3, min_max[0] + Div*4, min_max[0] + Div*5]
    Regla_R = []
    if Regla

def prueba1(File):
    Reglas_Iniciales = []
    Iguales = []
    A1 = [0,0]
    A2 = [0,0]
    A3 = [0,0]
    A4 = [0,0]
    A5 = [0,0]
    C = [0,0]
    Reglas_Iniciales = read_file(File)
    porcentaje = 0
    for i in range(len(Reglas_Iniciales)):
        Regla = Reglas_Iniciales[i]
        encontrado = False
        A1[0] = comparacion_menor(A1[0],Regla[0]) 
        A2[0] = comparacion_menor(A2[0],Regla[1]) 
        A3[0] = comparacion_menor(A3[0],Regla[2]) 
        A4[0] = comparacion_menor(A4[0],Regla[3]) 
        A5[0] = comparacion_menor(A5[0],Regla[4]) 
        C[0] = comparacion_menor(C[0],Regla[5])

        A1[1] = comparacion_mayor(A1[1],Regla[0]) 
        A2[1] = comparacion_mayor(A2[1],Regla[1]) 
        A3[1] = comparacion_mayor(A3[1],Regla[2]) 
        A4[1] = comparacion_mayor(A4[1],Regla[3]) 
        A5[1] = comparacion_mayor(A5[1],Regla[4]) 
        C[1] = comparacion_mayor(C[1],Regla[5])
        if porcentaje < int((i*100)/len(Reglas_Iniciales)):
            porcentaje = int((i*100)/len(Reglas_Iniciales))
            print("Descartando Reglas iguales: ", porcentaje, "%")
        for j in range(len(Iguales)):
            Igual = Iguales[j]
            if set(Regla) == set(Igual):
                encontrado = True
        if not encontrado:
            Iguales.append(Regla)
    AT1 = []
    Div = (A1[1] - A1[0])/5
    AT1 = [A1[0] , A1[0] + Div, A1[0] + Div*2, A1[0] + Div*3, A1[0] + Div*4, A1[0] + Div*5]


    print("Reglas Totales: ", len(Iguales))
    print("Antecedente 1: ", A1)
    print("Antecedente 2: ", A2)
    print("Antecedente 3: ", A3)
    print("Antecedente 4: ", A4)
    print("Antecedente 5: ", A5)
    print("Consecuente: ", C)
    print("DivisorAT1: ", Div)
    print("Triangulos: ", AT1)
prueba1("training/delta_ail-5-1tra.dat")
