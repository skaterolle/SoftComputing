
from pathlib import Path
import statistics

def read_file(File):
    Path("./Clasificador/tmp").mkdir(parents=True, exist_ok=True)
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

def read_fileR(File):
    Path("./Clasificador/tmp").mkdir(parents=True, exist_ok=True)
    f = open(File, "r")
    lista = []
    while True:
        line = f.readline()
        if not line:
            break
        if line[0] != '@':
            numero = [str(x) for x in line.replace(' ','').rstrip('\n').split(',')]
            lista.append(numero)
    f.close()
    return lista

def read_min_max(File):
    f = open(File, "r")
    lista = []
    while True:
        line = f.readline()
        if not line:
            break
        if "@attribute" in line and "TypeGlass" not in line:
            numero = [float(x) for x in line.partition('[')[2].replace('[','').replace(']','').strip("[ \n").split(',')]
            lista.append(numero)
        elif "@attribute" in line and "TypeGlass" in line:
            numero = [float(x) for x in line.partition('{')[2].replace('{','').replace('}','').strip("{ \n").split(',')]
            lista.append(numero)
    f.close()
    return lista

#Escribe en un fichero pasado por parametro una lista pasada por parametro que sea de tipo float
def write_fileT(File, list):
    f = open(File, "w")
    for x in range(len(list)):
        for y in range(len(list[x])):
            f.write(str(list[x][y]))
            if y < (len(list[x]) - 1):
                f.write(", ")
        f.write("\n")

#Escribe en un fichero pasado por parametro una lista pasada por parametro que sea de tipo str
def write_fileTSTR(File, list):
    f = open(File, "w")
    for x in range(len(list)):
        for y in range(len(list[x])):
            #print("Y: ", y, "\tpos: ", len(list[x])-1, "\tElemento: ", list[x])
            if y < (len(list[x]) - 2):
                f.write(list[x][y])
                if y < (len(list[x]) - 2):
                    f.write(", ")
            elif y >= (len(list[x])- 2) and y <= (len(list[x])):
                #print("Numero: ",list[x][y])
                f.write(str(list[x][y]))
                if y == len(list[x])-2:
                    f.write(", ")
        f.write("\n")

# Devuelve el mayor numero entre 2
def comparacion_mayor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Devuelve el menor numero entre 2
def comparacion_menor(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

# Se pasa un número y una lista, dependiendo de entre que valores esté, devuelve en 5 etiquetas diferents
# La lista son los inicios y finales de las etiquetas
def etiqueta_5(num, T):
    if num >= T[0] and num < T[1]:
        return "Bajo"
    elif num >= T[1] and num < T[2]:
        return "Medio-Bajo"
    elif num >= T[2] and num < T[3]:
        return "Medio"
    elif num >= T[3] and num < T[4]:
        return "Medio-Alto"
    elif num >= T[4] and num <= T[5]:
        return "Alto"
    else:
        return num

# Se pasa un número y una lista, dependiendo de entre que valores esté, devuelve en 3 etiquetas diferents
# IMPORTANTE, hay que poner <= || >= sino no cogería aquellos que coinciden con el corte
def etiqueta_3(num, T):
    if num >= T[0] and num < T[1]:
        return "Bajo"
    elif num >= T[1] and num < T[2]:
        return "Medio"
    elif num >= T[2] and num <= T[3]:
        return "Alto"
    else:
        return num

# Devuelve la Regla con las etiquetas ya establecidas para 5 etiquetas
def etiquetado_5(Regla, AT1, AT2, AT3, AT4, AT5,AT6,AT7,AT8,AT9):
    E1 = etiqueta_5(Regla[0],AT1)
    E2 = etiqueta_5(Regla[1],AT2)
    E3 = etiqueta_5(Regla[2],AT3)
    E4 = etiqueta_5(Regla[3],AT4)
    E5 = etiqueta_5(Regla[4],AT5)
    E6 = etiqueta_5(Regla[5],AT6)
    E7 = etiqueta_5(Regla[6],AT7)
    E8 = etiqueta_5(Regla[7],AT8)
    E9 = etiqueta_5(Regla[8],AT9)
    EC = Regla[9]
    Regla_R = [E1, E2, E3, E4, E5, E6, E7, E8, E9, EC]
    # A1 = matching_5(Regla[0],AT1, E1)
    # A2 = matching_5(Regla[1],AT2, E2)
    # A3 = matching_5(Regla[2],AT3, E3)
    # A4 = matching_5(Regla[3],AT4, E4)
    # A5 = matching_5(Regla[4],AT5, E5)
    # A6 = matching_5(Regla[5],AT6, E6)
    # A7 = matching_5(Regla[6],AT7, E7)
    # A8 = matching_5(Regla[7],AT8, E8)
    # A9 = matching_5(Regla[8],AT9, E9)
    #print(Regla[9], ATC, EC)
    # Este sirve en el caso que queramos sacarlo mediante la suma de todos
    # emparejamiento = A1 + A2 + A3 + A4 + A5 + C
    # Minimo
    #print(A1, A2, A3, A4, A5, A6, A7, A8, A9)
    #print(E8)
    #entrada = input("Pulse Enter")
    # emparejamiento = min(A1, A2, A3, A4, A5, A6, A7, A8, A9)
    # Producto
    #emparejamiento = (A1 * A2 * A3 * A4 * A5 * C)
    # Regla_R.append(emparejamiento)
    return Regla_R
    
# Devuelve la Regla con las etiquetas ya establecidas para 3 etiquetas
def etiquetado_3(Regla, AT1, AT2, AT3, AT4, AT5, AT6, AT7, AT8, AT9):
    E1 = etiqueta_3(Regla[0],AT1)
    E2 = etiqueta_3(Regla[1],AT2)
    E3 = etiqueta_3(Regla[2],AT3)
    E4 = etiqueta_3(Regla[3],AT4)
    E5 = etiqueta_3(Regla[4],AT5)
    E6 = etiqueta_3(Regla[5],AT6)
    E7 = etiqueta_3(Regla[6],AT7)
    E8 = etiqueta_3(Regla[7],AT8)
    E9 = etiqueta_3(Regla[8],AT9)
    EC = Regla[9]
    Regla_R = [E1, E2, E3, E4, E5, E6, E7, E8, E9, EC]
    # A1 = matching_3(Regla[0],AT1, E1)
    # A2 = matching_3(Regla[1],AT2, E2)
    # A3 = matching_3(Regla[2],AT3, E3)
    # A4 = matching_3(Regla[3],AT4, E4)
    # A5 = matching_3(Regla[4],AT5, E5)
    # C = matching_3(Regla[5],ATC, EC)
    # Este sirve en el caso que queramos sacarlo mediante la suma de todos
    # emparejamiento = A1 + A2 + A3 + A4 + A5 + C
    # Minimo
    # emparejamiento = min(A1, A2, A3, A4, A5)
    # Producto
    #emparejamiento = (A1 * A2 * A3 * A4 * A5 * C)
    # Regla_R.append(emparejamiento)
    return Regla_R

# Devuelve el valor del matching dependiendo de 5 etiquetas
# Num a comprobar, Lista de triangulo, etiqueta
def matching_5(num, AT, E):
    T = []
    if E == "Bajo":
        T.append(AT[0])
        medio = (AT[1] - AT[0])/2
        T.append(AT[0] + medio)
        T.append(AT[1])
    elif E == "Medio-Bajo":
        T.append(AT[1])
        medio = (AT[2] - AT[1])/2
        T.append(AT[1] + medio)
        T.append(AT[2])
    elif E == "Medio":
        T.append(AT[2])
        medio = (AT[3] - AT[2])/2
        T.append(AT[2] + medio)
        T.append(AT[3])
    elif E == "Medio-Alto":
        T.append(AT[3])
        medio = (AT[4] - AT[3])/2
        T.append(AT[3] + medio)
        T.append(AT[4])
    elif E == "Alto":
        T.append(AT[4])
        medio = (AT[5] - AT[4])/2
        T.append(AT[4] + medio)
        T.append(AT[5])

    if num <= T[0]:
        return 0
    elif num >= T[2]:
        return 0
    elif num == T[1]:
        return 1
    elif num > T[0] and num < T[1]:
        #print("Matching: ",num, T[0], T[1])
        #print("Return: ", ((num - T[0])/(T[1]-T[0])))
        return (num - T[0])/(T[1]-T[0])
    elif num > T[1] and num <= T[2]:
        return (num - T[2])/(T[1] - T[2])

# Devuelve el valor del matching dependiendo de 3 etiquetas
def matching_3(num, AT, E):
    T = []
    if E == "Bajo":
        T.append(AT[0])
        medio = (AT[1] - AT[0])/2
        T.append(AT[0] + medio)
        T.append(AT[1])
    elif E == "Medio":
        T.append(AT[1])
        medio = (AT[2] - AT[1])/2
        T.append(AT[1] + medio)
        T.append(AT[2])
    elif E == "Alto":
        T.append(AT[2])
        medio = (AT[3] - AT[2])/2
        T.append(AT[2] + medio)
        T.append(AT[3])
    
    if num < T[0]:
        return 0
    elif num > T[2]:
        return 0
    elif num == T[1]:
        return 1
    elif num >= T[0] and num < T[1]:
        return (num - T[0])/(T[1]-T[0])
    elif num > T[1] and num <= T[2]:
        return (num - T[2])/(T[1] - T[2])

# Devuelve una lista donde se descartan las reglas iguales
def Descarta_Iguales(Reglas_Iniciales):
    porcentaje = 0
    Iguales = []
    for i in range(len(Reglas_Iniciales)):
        Regla = Reglas_Iniciales[i]
        encontrado = False
        if porcentaje < int((i*100)/len(Reglas_Iniciales)):
            porcentaje = int((i*100)/len(Reglas_Iniciales))
            #print(texto, porcentaje, "%")
        for j in range(len(Iguales)):
            Igual = Iguales[j]
            #print(Regla)
            if (Regla[0] == Igual[0]) and (Regla[1] == Igual[1]) and (Regla[2] == Igual[2]) and (Regla[3] == Igual[3]) and (Regla[4] == Igual[4]) and (Regla[5] == Igual[5]) and (Regla[6] == Igual[6]) and (Regla[7] == Igual[7]) and (Regla[8] == Igual[8]) and (Regla[9] == Igual[9]) and (Regla[10] == Igual[10]):
                #print(Regla[j])
                encontrado = True
        if not encontrado:
            Iguales.append(Regla)
    return Iguales

def Comprueba_Todo(Regla1, Regla2):
    if (Regla1[0] == Regla2[0]) and (Regla1[1] == Regla2[1]) and (Regla1[2] == Regla2[2]) and (Regla1[3] == Regla2[3]) and (Regla1[4] == Regla2[4]) and (Regla1[5] == Regla2[5]) and (Regla1[6] == Regla2[6]) and (Regla1[7] == Regla2[7]) and (Regla1[8] == Regla2[8]) and (Regla1[9] == Regla2[9]):
        return True
    else:
        return False

def Comprueba_Antecedentes(Regla1, Regla2):
    if (Regla1[0] == Regla2[0]) and (Regla1[1] == Regla2[1]) and (Regla1[2] == Regla2[2]) and (Regla1[3] == Regla2[3]) and (Regla1[4] == Regla2[4]) and (Regla1[5] == Regla2[5]) and (Regla1[6] == Regla2[6]) and (Regla1[7] == Regla2[7]) and (Regla1[8] == Regla2[8]):
        return True
    else:
        return False


def Peso(Reglas):
    Reglas_con_peso = []
    for i in range(len(Reglas)):
        Regla = Reglas[i]
        Sj = 0
        S = 0
        #print(Regla, i)
        for j in range(len(Reglas)):
            comprueba = Reglas[j]
            if(Comprueba_Todo(Regla,comprueba)):
                Sj += 1
        for k in range(len(Reglas)):
            comprueba = Reglas[k]
            if(Comprueba_Antecedentes(Regla,comprueba)):
                S += 1
        Resultado = Sj/S
        Regla.append(Resultado)
        Reglas_con_peso.append(Regla)
    return Reglas_con_peso

# Comprueba si hay Reglas cuyos antecedentes sean iguales pero sus consecuentes diferentes, se pasa después de la función Descarta_Iguales() o Comprueba_Reglas()
def comprueba_antecedentes_iguales(List):
    for x in range(len(List)):
        for y in range(len(List)):
            if x != y:
                if Comprueba_Antecedentes(List[x], List[y]):
                    print("Iguales, X = ", x, " Y = ", y)
                    print("X = ", List[x][:], " Clase = ", List[x][9])
                    print("Y = ", List[y][:], " Clase = ", List[y][9])
                    # if List[x][10] > List[y][10]:
                    #     List.pop(y)
                    # else:
                    #     List.pop(x)

# Comprueba cada reglas si sus antecedentes son iguales pero sus consecuentes diferentes y coge el matching que se hizo al etiquetar cada regla
# Y se escoge aquel que tenga mayor matching, Devuelve la Lista de Reglas sin el matching
def comprueba_Reglas(List):
    Reglas_Afinadas = []
    for x in range(len(List)):
        encontrado = False
        for y in range(len(Reglas_Afinadas)):
            if Comprueba_Antecedentes(List[x], Reglas_Afinadas[y]):
                #print(List[x])
                encontrado = True
                #print(List[x])
                if List[x][10] > Reglas_Afinadas[y][10] and List[x][9] == List[y][9]:
                    Reglas_Afinadas.pop(y)
                    Reglas_Afinadas.append(List[x])
        if not encontrado:
            Reglas_Afinadas.append(List[x])
    Reglas = []
    for x in range(len(Reglas_Afinadas)):
        Reglas.append(Reglas_Afinadas[x][:])
    return Reglas

def Training_5(File, SaveFile):
    # Definición de variables de reglas
    Reglas_Iniciales = []
    Reglas_Etiquetadas = []
    Min_Max = read_min_max(File)
    Iguales = []
    # Definición de variables de Minimos y Máximos
    A1 = Min_Max[0]
    A2 = Min_Max[1]
    A3 = Min_Max[2]
    A4 = Min_Max[3]
    A5 = Min_Max[4]
    A6 = Min_Max[5]
    A7 = Min_Max[6]
    A8 = Min_Max[7]
    A9 = Min_Max[8]
    C = Min_Max[9]
    #print(C)
    # Definición de variables de etiquetas
    AT1 = []
    AT2 = []
    AT3 = []
    AT4 = []
    AT5 = []
    AT6 = []
    AT7 = []
    AT8 = []
    AT9 = []
    Reglas_Iniciales = read_file(File)
    porcentaje = 0

    # Saca los triangulos (Inicio y Final) de cada Antecedente y Consecuente y los guarda en una Lista
    Div1 = (A1[1] - A1[0])/5
    AT1 = [A1[0] , A1[0] + Div1, A1[0] + Div1*2, A1[0] + Div1*3, A1[0] + Div1*4, A1[0] + Div1*5]
    Div2 = (A2[1] - A2[0])/5
    AT2 = [A2[0] , A2[0] + Div2, A2[0] + Div2*2, A2[0] + Div2*3, A2[0] + Div2*4, A2[0] + Div2*5] 
    Div3 = (A3[1] - A3[0])/5
    AT3 = [A3[0] , A3[0] + Div3, A3[0] + Div3*2, A3[0] + Div3*3, A3[0] + Div3*4, A3[0] + Div3*5]
    Div4 = (A4[1] - A4[0])/5
    AT4 = [A4[0] , A4[0] + Div4, A4[0] + Div4*2, A4[0] + Div4*3, A4[0] + Div4*4, A4[0] + Div4*5]
    Div5 = (A5[1] - A5[0])/5
    AT5 = [A5[0] , A5[0] + Div5, A5[0] + Div5*2, A5[0] + Div5*3, A5[0] + Div5*4, A5[0] + Div5*5]
    Div6 = (A6[1]- A6[0])/5
    AT6 = [A6[0] , A6[0] + Div6, A6[0] + Div6*2, A6[0] + Div6*3, A6[0] + Div6*4, A6[0] + Div6*5]
    Div7 = (A7[1]- A7[0])/5
    AT7 = [A7[0] , A7[0] + Div7, A7[0] + Div7*2, A7[0] + Div7*3, A7[0] + Div7*4, A7[0] + Div7*5]
    Div8 = (A8[1]- A8[0])/5
    AT8 = [A8[0] , A8[0] + Div8, A8[0] + Div8*2, A8[0] + Div8*3, A8[0] + Div8*4, A8[0] + Div8*5]
    Div9 = (A9[1]- A9[0])/5
    AT9 = [A9[0] , A9[0] + Div9, A9[0] + Div9*2, A9[0] + Div9*3, A9[0] + Div9*4, A9[0] + Div9*5]
    DivC = (C[1] - C[0])/5
    ATC = [C[0] , C[0] + DivC, C[0] + DivC*2, C[0] + DivC*3, C[0] + DivC*4, C[0] + DivC*5]
    #print(ATC)

    porcentaje = 0
    # Etiqueta cada regla y les agrega su matching para usar más tarde
    for x in range(len(Reglas_Iniciales)):
        if porcentaje < int((x*100)/len(Reglas_Iniciales)):
            porcentaje = int((x*100)/len(Reglas_Iniciales))
            #print("Etiquetando Reglas: ", porcentaje, "%")
        Reglas_Etiquetadas.append(etiquetado_5(Reglas_Iniciales[x],AT1,AT2,AT3,AT4,AT5,AT6,AT7,AT8,AT9))
    #Iguales = Descarta_Iguales("Descartando Iguales: ",Reglas_Etiquetadas)
    Reglas_Iniciales = Peso(Reglas_Etiquetadas)
    #Reglas_Iniciales = Iguales
    #Iguales = []

    # Compruba cada Regla y quita aquellas cuyos antecedentes sean iguales y consecuentes diferentes eligiendo los que tengan un matching mayor
    # Devuelve una Lista sin el matching
    Iguales = comprueba_Reglas(Reglas_Iniciales)
    #print(Iguales)
    #comprueba_antecedentes_iguales(Iguales)
    #Iguales = Descarta_Iguales(Iguales)
    write_fileTSTR(SaveFile, Iguales[:][:])
    comprueba_antecedentes_iguales(Iguales)

    # Muestra por pantalla
    #print("Reglas Totales: ", len(Iguales))
    # Devuelve el número de Reglas
    return len(Iguales)

def Training_3(File, SaveFile):
    # Definición de variables de reglas
    Reglas_Iniciales = []
    Reglas_Etiquetadas = []
    Min_Max = read_min_max(File)
    Iguales = []
    # Definición de variables de Minimos y Máximos
    A1 = Min_Max[0]
    A2 = Min_Max[1]
    A3 = Min_Max[2]
    A4 = Min_Max[3]
    A5 = Min_Max[4]
    A6 = Min_Max[5]
    A7 = Min_Max[6]
    A8 = Min_Max[7]
    A9 = Min_Max[8]
    C = Min_Max[9]
    # Definición de variables de etiquetas
    AT1 = []
    AT2 = []
    AT3 = []
    AT4 = []
    AT5 = []
    AT6 = []
    AT7 = []
    AT8 = []
    AT9 = []
    Reglas_Iniciales = read_file(File)

    # Saca los triangulos (Inicio y Final) de cada Antecedente y Consecuente y los guarda en una Lista
    Div1 = (A1[1] - A1[0])/3
    AT1 = [A1[0] , A1[0] + Div1, A1[0] + Div1*2, A1[0] + Div1*3]
    Div2 = (A2[1] - A2[0])/3
    AT2 = [A2[0] , A2[0] + Div2, A2[0] + Div2*2, A2[0] + Div2*3]
    Div3 = (A3[1] - A3[0])/3
    AT3 = [A3[0] , A3[0] + Div3, A3[0] + Div3*2, A3[0] + Div3*3]
    Div4 = (A4[1] - A4[0])/3
    AT4 = [A4[0] , A4[0] + Div4, A4[0] + Div4*2, A4[0] + Div4*3]
    Div5 = (A5[1] - A5[0])/3
    AT5 = [A5[0] , A5[0] + Div5, A5[0] + Div5*2, A5[0] + Div5*3]
    Div6 = (A6[1]- A6[0])/3
    AT6 = [A6[0] , A6[0] + Div6, A6[0] + Div6*2, A6[0] + Div6*3 + 0.00001] # Vuelve a haber el problema de que no da el numero completo
    Div7 = (A7[1]- A7[0])/3
    AT7 = [A7[0] , A7[0] + Div7, A7[0] + Div7*2, A7[0] + Div7*3]
    Div8 = (A8[1]- A8[0])/3
    AT8 = [A8[0] , A8[0] + Div8, A8[0] + Div8*2, A8[0] + Div8*3]
    Div9 = (A9[1]- A9[0])/3
    AT9 = [A9[0] , A9[0] + Div9, A9[0] + Div9*2, A9[0] + Div9*3]
    DivC = (C[1] - C[0])/3
    ATC = [C[0] , C[0] + DivC, C[0] + DivC*2, C[0] + DivC*3]

    # Etiqueta cada regla y les agrega su matching para usar más tarde
    for x in range(len(Reglas_Iniciales)):
        Reglas_Etiquetadas.append(etiquetado_3(Reglas_Iniciales[x],AT1,AT2,AT3,AT4,AT5,AT6, AT7, AT8, AT9))

    #Iguales = Descarta_Iguales("Descartando Iguales: ",Reglas_Etiquetadas)
    Reglas_Iniciales = Peso(Reglas_Etiquetadas)
    #Reglas_Iniciales = Iguales
    #Iguales = []

    # Compruba cada Regla y quita aquellas cuyos antecedentes sean iguales y consecuentes diferentes eligiendo los que tengan un matching mayor
    # Devuelve una Lista sin el matching
    Iguales = comprueba_Reglas(Reglas_Iniciales)
    #print(Iguales)
    #comprueba_antecedentes_iguales(Iguales)
    Iguales = Descarta_Iguales(Iguales)
    write_fileTSTR(SaveFile, Iguales[:][:])
    # Muestra por pantalla
    #print("Reglas Totales: ", len(Iguales))
    # Devuelve el número de reglas
    return len(Iguales)

def Controlador_5(FileL,FileR):
    Reglas = read_fileR(FileR)
    Min_Max = read_min_max(FileL)
    Data = read_file(FileL)
    # Definición de variables de Minimos y Máximos
    A1 = Min_Max[0]
    A2 = Min_Max[1]
    A3 = Min_Max[2]
    A4 = Min_Max[3]
    A5 = Min_Max[4]
    A6 = Min_Max[5]
    A7 = Min_Max[6]
    A8 = Min_Max[7]
    A9 = Min_Max[8]
    C = Min_Max[9]
    #print(C)
    # Definición de variables de etiquetas
    AT1 = []
    AT2 = []
    AT3 = []
    AT4 = []
    AT5 = []
    AT6 = []
    AT7 = []
    AT8 = []
    AT9 = []
    porcentaje = 0

    # Saca los triangulos (Inicio y Final) de cada Antecedente y Consecuente y los guarda en una Lista
    Div1 = (A1[1] - A1[0])/5
    AT1 = [A1[0] , A1[0] + Div1, A1[0] + Div1*2, A1[0] + Div1*3, A1[0] + Div1*4, A1[0] + Div1*5]
    Div2 = (A2[1] - A2[0])/5
    AT2 = [A2[0] , A2[0] + Div2, A2[0] + Div2*2, A2[0] + Div2*3, A2[0] + Div2*4, A2[0] + Div2*5] 
    Div3 = (A3[1] - A3[0])/5
    AT3 = [A3[0] , A3[0] + Div3, A3[0] + Div3*2, A3[0] + Div3*3, A3[0] + Div3*4, A3[0] + Div3*5]
    Div4 = (A4[1] - A4[0])/5
    AT4 = [A4[0] , A4[0] + Div4, A4[0] + Div4*2, A4[0] + Div4*3, A4[0] + Div4*4, A4[0] + Div4*5]
    Div5 = (A5[1] - A5[0])/5
    AT5 = [A5[0] , A5[0] + Div5, A5[0] + Div5*2, A5[0] + Div5*3, A5[0] + Div5*4, A5[0] + Div5*5]
    Div6 = (A6[1]- A6[0])/5
    AT6 = [A6[0] , A6[0] + Div6, A6[0] + Div6*2, A6[0] + Div6*3, A6[0] + Div6*4, A6[0] + Div6*5]
    Div7 = (A7[1]- A7[0])/5
    AT7 = [A7[0] , A7[0] + Div7, A7[0] + Div7*2, A7[0] + Div7*3, A7[0] + Div7*4, A7[0] + Div7*5]
    Div8 = (A8[1]- A8[0])/5
    AT8 = [A8[0] , A8[0] + Div8, A8[0] + Div8*2, A8[0] + Div8*3, A8[0] + Div8*4, A8[0] + Div8*5]
    Div9 = (A9[1]- A9[0])/5
    AT9 = [A9[0] , A9[0] + Div9, A9[0] + Div9*2, A9[0] + Div9*3, A9[0] + Div9*4, A9[0] + Div9*5]
    #print(ATC)

    Aciertos = Calcular_defuzzi_5(Reglas, Data, AT1, AT2, AT3, AT4, AT5, AT6, AT7, AT8, AT9)
    # print(Aciertos/len(Data))
    return Aciertos/len(Data)
    #return Error_Cuadratico(Estimado, Data)
    #print(Reglas)

def Controlador_3(FileL,FileR):
    Reglas = read_fileR(FileR)
    Min_Max = read_min_max(FileL)
    Data = read_file(FileL)
    # Definición de variables de Minimos y Máximos
    A1 = Min_Max[0]
    A2 = Min_Max[1]
    A3 = Min_Max[2]
    A4 = Min_Max[3]
    A5 = Min_Max[4]
    A6 = Min_Max[5]
    A7 = Min_Max[6]
    A8 = Min_Max[7]
    A9 = Min_Max[8]
    C = Min_Max[9]
    # Definición de variables de etiquetas
    AT1 = []
    AT2 = []
    AT3 = []
    AT4 = []
    AT5 = []
    AT6 = []
    AT7 = []
    AT8 = []
    AT9 = []

    # Saca los triangulos (Inicio y Final) de cada Antecedente y Consecuente y los guarda en una Lista
    Div1 = (A1[1] - A1[0])/3
    AT1 = [A1[0] , A1[0] + Div1, A1[0] + Div1*2, A1[0] + Div1*3]
    Div2 = (A2[1] - A2[0])/3
    AT2 = [A2[0] , A2[0] + Div2, A2[0] + Div2*2, A2[0] + Div2*3]
    Div3 = (A3[1] - A3[0])/3
    AT3 = [A3[0] , A3[0] + Div3, A3[0] + Div3*2, A3[0] + Div3*3]
    Div4 = (A4[1] - A4[0])/3
    AT4 = [A4[0] , A4[0] + Div4, A4[0] + Div4*2, A4[0] + Div4*3]
    Div5 = (A5[1] - A5[0])/3
    AT5 = [A5[0] , A5[0] + Div5, A5[0] + Div5*2, A5[0] + Div5*3]
    Div6 = (A6[1]- A6[0])/3
    AT6 = [A6[0] , A6[0] + Div6, A6[0] + Div6*2, A6[0] + Div6*3 + 0.00001] # Vuelve a haber el problema de que no da el numero completo
    Div7 = (A7[1]- A7[0])/3
    AT7 = [A7[0] , A7[0] + Div7, A7[0] + Div7*2, A7[0] + Div7*3]
    Div8 = (A8[1]- A8[0])/3
    AT8 = [A8[0] , A8[0] + Div8, A8[0] + Div8*2, A8[0] + Div8*3]
    Div9 = (A9[1]- A9[0])/3
    AT9 = [A9[0] , A9[0] + Div9, A9[0] + Div9*2, A9[0] + Div9*3]
    
    #Estimado = Calcular_defuzzi_3(Reglas, Data, AT1, AT2, AT3, AT4, AT5, AT6, AT7, AT8, AT9)
    Aciertos = Calcular_defuzzi_3(Reglas, Data, AT1, AT2, AT3, AT4, AT5, AT6, AT7, AT8, AT9)
    # print(Aciertos/len(Data))
    return Aciertos/len(Data)
    #return Error_Cuadratico(Estimado, Data)
    #print(Reglas)

def Error_Cuadratico(Estimado, Real):
    suma = 0
    for i in range(len(Estimado)):
        suma = Real[i][5] - Estimado[i]
    Error = (suma * suma)/len(Estimado)
    return Error


def Calcular_defuzzi_5(Reglas, Datos, AT1, AT2, AT3, AT4, AT5, AT6, AT7, AT8, AT9):
    acierto = 0
    for i in range(len(Datos)):
        h = []
        #compara = etiquetado_5(Datos[i], AT1, AT2, AT3, AT4, AT5, AT6, AT7, AT8, AT9)
        sumatorio_superior = 0
        compara = []
        for j in range(len(Reglas)):
            minimo = []
            comparado = []
            resultado = []
            minimo.append(matching_5(Datos[i][0], AT1, Reglas[j][0]))
            minimo.append(matching_5(Datos[i][1], AT2, Reglas[j][1]))
            minimo.append(matching_5(Datos[i][2], AT3, Reglas[j][2]))
            minimo.append(matching_5(Datos[i][3], AT4, Reglas[j][3]))
            minimo.append(matching_5(Datos[i][4], AT5, Reglas[j][4]))
            minimo.append(matching_5(Datos[i][5], AT6, Reglas[j][5]))
            minimo.append(matching_5(Datos[i][6], AT7, Reglas[j][6]))
            minimo.append(matching_5(Datos[i][7], AT8, Reglas[j][7]))
            minimo.append(matching_5(Datos[i][8], AT9, Reglas[j][8]))
            comparado.append(float(min(minimo)))
            comparado.append(float(Reglas[j][10]))
            # print(statistics.mean(comparado))
            # input("Enter")
            resultado.append(statistics.mean(comparado))
            resultado.append(float(Reglas[j][9]))
            compara.append(resultado)
        GA = 0.0
        sol = []
        for j in range(len(compara)):
            #print(compara[j], GA)
            if compara[j][0] > GA: # Si cambio a >= baja el acierto
                GA = compara[j][0]
                sol = compara[j]
        #print(Datos[i][9], GA, sol[1])
        # print(statistics.mean(compara[2]))
        if Datos[i][9] == sol[1]:
            acierto += 1
            #minimo.append(Datos[i][9])
            #print(minimo)
            #h.append(min(minimo))
            # if Comprueba_Antecedentes(compara, Reglas[j]):
            #     #print("Antecendentes Iguales", float(Reglas[j][9]) == float(compara[9]))
            #     if (float(Reglas[j][9]) == float(compara[9])):
            #         #print(acierto)
            #         acierto += 1
    return acierto

def Calcular_defuzzi_3(Reglas, Datos, AT1, AT2, AT3, AT4, AT5, AT6, AT7, AT8, AT9):
    acierto = 0
    for i in range(len(Datos)):
        h = []
        #compara = etiquetado_5(Datos[i], AT1, AT2, AT3, AT4, AT5, AT6, AT7, AT8, AT9)
        sumatorio_superior = 0
        compara = []
        for j in range(len(Reglas)):
            minimo = []
            comparado = []
            resultado = []
            minimo.append(matching_3(Datos[i][0], AT1, Reglas[j][0]))
            minimo.append(matching_3(Datos[i][1], AT2, Reglas[j][1]))
            minimo.append(matching_3(Datos[i][2], AT3, Reglas[j][2]))
            minimo.append(matching_3(Datos[i][3], AT4, Reglas[j][3]))
            minimo.append(matching_3(Datos[i][4], AT5, Reglas[j][4]))
            minimo.append(matching_3(Datos[i][5], AT6, Reglas[j][5]))
            minimo.append(matching_3(Datos[i][6], AT7, Reglas[j][6]))
            minimo.append(matching_3(Datos[i][7], AT8, Reglas[j][7]))
            minimo.append(matching_3(Datos[i][8], AT9, Reglas[j][8]))
            comparado.append(float(min(minimo)))
            comparado.append(float(Reglas[j][10]))
            resultado.append(statistics.mean(comparado))
            resultado.append(float(Reglas[j][9]))
            compara.append(resultado)
        GA = 0.0
        sol = []
        for j in range(len(compara)):
            #print(compara[j], GA)
            if compara[j][0] > GA: # Si cambio a >= baja el acierto
                GA = compara[j][0]
                sol = compara[j]
        #print(Datos[i][9], GA, sol[1])
        # print(statistics.mean(compara[2]))
        if Datos[i][9] == sol[1]:
            acierto += 1
            #minimo.append(Datos[i][9])
            #print(minimo)
            #h.append(min(minimo))
            # if Comprueba_Antecedentes(compara, Reglas[j]):
            #     #print("Antecendentes Iguales", float(Reglas[j][9]) == float(compara[9]))
            #     if (float(Reglas[j][9]) == float(compara[9])):
            #         #print(acierto)
            #         acierto += 1
    return acierto
        

def training_5_todos():
    print("\nTrainin con 5 etiquetas: ")
    print("------------------------")
    T1 = Training_5("Clasificador/training/glass-10-1tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-1.txt")
    print("Reglas del primer Training: ", T1)
    T2 = Training_5("Clasificador/training/glass-10-2tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-2.txt")
    print("Reglas del segundo Training: ", T2)
    T3 = Training_5("Clasificador/training/glass-10-3tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-3.txt")
    print("Reglas del tercero Training: ", T3)
    T4 = Training_5("Clasificador/training/glass-10-4tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-4.txt")
    print("Reglas del cuarto Training: ", T4)
    T5 = Training_5("Clasificador/training/glass-10-5tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-5.txt")
    print("Reglas del quinto Training: ", T5)
    T6 = Training_5("Clasificador/training/glass-10-6tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-6.txt")
    print("Reglas del sexto Training: ", T6)
    T7 = Training_5("Clasificador/training/glass-10-7tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-7.txt")
    print("Reglas del septimo Training: ", T7)
    T8 = Training_5("Clasificador/training/glass-10-8tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-8.txt")
    print("Reglas del octavo Training: ", T8)
    T9 = Training_5("Clasificador/training/glass-10-9tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-9.txt")
    print("Reglas del noveno Training: ", T9)
    T10 = Training_5("Clasificador/training/glass-10-10tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-10.txt")
    print("Reglas del decimo Training: ", T10)

    resultado = (T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 + T9 + T10)/10
    print("\nMedia de Reglas: ", resultado)

def training_3_todos():
    print("\nTrainin con 3 etiquetas: ")
    print("------------------------")
    T1 = Training_3("Clasificador/training/glass-10-1tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-1.txt")
    print("Reglas del primer Training: ", T1)
    T2 = Training_3("Clasificador/training/glass-10-2tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-2.txt")
    print("Reglas del segundo Training: ", T2)
    T3 = Training_3("Clasificador/training/glass-10-3tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-3.txt")
    print("Reglas del tercero Training: ", T3)
    T4 = Training_3("Clasificador/training/glass-10-4tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-4.txt")
    print("Reglas del cuarto Training: ", T4)
    T5 = Training_3("Clasificador/training/glass-10-5tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-5.txt")
    print("Reglas del quinto Training: ", T5)
    T6 = Training_3("Clasificador/training/glass-10-6tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-6.txt")
    print("Reglas del sexto Training: ", T6)
    T7 = Training_3("Clasificador/training/glass-10-7tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-7.txt")
    print("Reglas del septimo Training: ", T7)
    T8 = Training_3("Clasificador/training/glass-10-8tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-8.txt")
    print("Reglas del octavo Training: ", T8)
    T9 = Training_3("Clasificador/training/glass-10-9tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-9.txt")
    print("Reglas del noveno Training: ", T9)
    T10 = Training_3("Clasificador/training/glass-10-10tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-10.txt")
    print("Reglas del decimo Training: ", T10)

    resultado = (T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 + T9 + T10)/10
    print("\nMedia de Reglas: ", resultado)

def controlador_5():
    print("\nAccuracy con 5 etiquetas: ")
    print("----------------------------")
    print("\nTraining:---------------")
    T1 = Controlador_5("Clasificador/training/glass-10-1tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-1.txt")
    print("Accuracy del primer Training: ", "%.2f" % (T1*100))
    T2 = Controlador_5("Clasificador/training/glass-10-2tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-2.txt")
    print("Accuracy del primer Training: ", "%.2f" % (T2*100))
    T3 = Controlador_5("Clasificador/training/glass-10-3tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-3.txt")
    print("Accuracy del tercero Training: ", "%.2f" % (T3*100))
    T4 = Controlador_5("Clasificador/training/glass-10-4tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-4.txt")
    print("Accuracy del cuarto Training: ", "%.2f" % (T4*100))
    T5 = Controlador_5("Clasificador/training/glass-10-5tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-5.txt")
    print("Accuracy del quinto Training: ", "%.2f" % (T5*100))
    T6 = Controlador_5("Clasificador/training/glass-10-6tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-6.txt")
    print("Accuracy del sexto Training: ", "%.2f" % (T6*100))
    T7 = Controlador_5("Clasificador/training/glass-10-7tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-7.txt")
    print("Accuracy del septimo Training: ", "%.2f" % (T7*100))
    T8 = Controlador_5("Clasificador/training/glass-10-8tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-8.txt")
    print("Accuracy del octavo Training: ", "%.2f" % (T8*100))
    T9 = Controlador_5("Clasificador/training/glass-10-9tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-9.txt")
    print("Accuracy del noveno Training: ", "%.2f" % (T9*100))
    T10 = Controlador_5("Clasificador/training/glass-10-10tra.dat", "Clasificador/tmp/ReglasEtiquetadas5-10.txt")
    print("Accuracy del decimo Training: ", "%.2f" % (T10*100))

    resultado = ((T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 + T9 + T10)/10)*100
    print("\nMedia de Accuracy del Training: ", "%.2f" % resultado)


    print("\nTest:---------------")
    T1 = Controlador_5("Clasificador/tst/glass-10-1tst.dat", "Clasificador/tmp/ReglasEtiquetadas5-1.txt")
    print("Accuracy del primer Test: ", "%.2f" % (T1*100))
    T2 = Controlador_5("Clasificador/tst/glass-10-2tst.dat", "Clasificador/tmp/ReglasEtiquetadas5-2.txt")
    print("Accuracy del primer Test: ", "%.2f" % (T2*100))
    T3 = Controlador_5("Clasificador/tst/glass-10-3tst.dat", "Clasificador/tmp/ReglasEtiquetadas5-3.txt")
    print("Accuracy del tercero Test: ", "%.2f" % (T3*100))
    T4 = Controlador_5("Clasificador/tst/glass-10-4tst.dat", "Clasificador/tmp/ReglasEtiquetadas5-4.txt")
    print("Accuracy del cuarto Test: ", "%.2f" % (T4*100))
    T5 = Controlador_5("Clasificador/tst/glass-10-5tst.dat", "Clasificador/tmp/ReglasEtiquetadas5-5.txt")
    print("Accuracy del quinto Test: ", "%.2f" % (T5*100))
    T6 = Controlador_5("Clasificador/tst/glass-10-6tst.dat", "Clasificador/tmp/ReglasEtiquetadas5-6.txt")
    print("Accuracy del sexto Test: ", "%.2f" % (T6*100))
    T7 = Controlador_5("Clasificador/tst/glass-10-7tst.dat", "Clasificador/tmp/ReglasEtiquetadas5-7.txt")
    print("Accuracy del septimo Test: ", "%.2f" % (T7*100))
    T8 = Controlador_5("Clasificador/tst/glass-10-8tst.dat", "Clasificador/tmp/ReglasEtiquetadas5-8.txt")
    print("Accuracy del octavo Test: ", "%.2f" % (T8*100))
    T9 = Controlador_5("Clasificador/tst/glass-10-9tst.dat", "Clasificador/tmp/ReglasEtiquetadas5-9.txt")
    print("Accuracy del noveno Test: ", "%.2f" % (T9*100))
    T10 = Controlador_5("Clasificador/tst/glass-10-10tst.dat", "Clasificador/tmp/ReglasEtiquetadas5-10.txt")
    print("Accuracy del decimo Test: ", "%.2f" % (T10*100))

    resultado = ((T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 + T9 + T10)/10)*100
    print("\nMedia de Accuracy del Test ", "%.2f" % resultado)

def controlador_3():
    print("\nAccuracy con 3 etiquetas: ")
    print("----------------------------")
    print("\nTraining:---------------")
    T1 = Controlador_3("Clasificador/training/glass-10-1tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-1.txt")
    print("Accuracy del primer Training: ", "%.2f" % (T1*100))
    T2 = Controlador_3("Clasificador/training/glass-10-2tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-2.txt")
    print("Accuracy del primer Training: ", "%.2f" % (T2*100))
    T3 = Controlador_3("Clasificador/training/glass-10-3tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-3.txt")
    print("Accuracy del tercero Training: ", "%.2f" % (T3*100))
    T4 = Controlador_3("Clasificador/training/glass-10-4tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-4.txt")
    print("Accuracy del cuarto Training: ", "%.2f" % (T4*100))
    T5 = Controlador_3("Clasificador/training/glass-10-5tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-5.txt")
    print("Accuracy del quinto Training: ", "%.2f" % (T5*100))
    T6 = Controlador_3("Clasificador/training/glass-10-6tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-6.txt")
    print("Accuracy del sexto Training: ", "%.2f" % (T6*100))
    T7 = Controlador_3("Clasificador/training/glass-10-7tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-7.txt")
    print("Accuracy del septimo Training: ", "%.2f" % (T7*100))
    T8 = Controlador_3("Clasificador/training/glass-10-8tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-8.txt")
    print("Accuracy del octavo Training: ", "%.2f" % (T8*100))
    T9 = Controlador_3("Clasificador/training/glass-10-9tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-9.txt")
    print("Accuracy del noveno Training: ", "%.2f" % (T9*100))
    T10 = Controlador_3("Clasificador/training/glass-10-10tra.dat", "Clasificador/tmp/ReglasEtiquetadas3-10.txt")
    print("Accuracy del decimo Training: ", "%.2f" % (T10*100))

    resultado = ((T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 + T9 + T10)/10)*100
    print("\nMedia de Accuracy del Training: ", "%.2f" % resultado)


    print("\nTest:---------------")
    T1 = Controlador_3("Clasificador/tst/glass-10-1tst.dat", "Clasificador/tmp/ReglasEtiquetadas3-1.txt")
    print("Accuracy del primer Test: ", "%.2f" % (T1*100))
    T2 = Controlador_3("Clasificador/tst/glass-10-2tst.dat", "Clasificador/tmp/ReglasEtiquetadas3-2.txt")
    print("Accuracy del primer Test: ", "%.2f" % (T2*100))
    T3 = Controlador_3("Clasificador/tst/glass-10-3tst.dat", "Clasificador/tmp/ReglasEtiquetadas3-3.txt")
    print("Accuracy del tercero Test: ", "%.2f" % (T3*100))
    T4 = Controlador_3("Clasificador/tst/glass-10-4tst.dat", "Clasificador/tmp/ReglasEtiquetadas3-4.txt")
    print("Accuracy del cuarto Test: ", "%.2f" % (T4*100))
    T5 = Controlador_3("Clasificador/tst/glass-10-5tst.dat", "Clasificador/tmp/ReglasEtiquetadas3-5.txt")
    print("Accuracy del quinto Test: ", "%.2f" % (T5*100))
    T6 = Controlador_3("Clasificador/tst/glass-10-6tst.dat", "Clasificador/tmp/ReglasEtiquetadas3-6.txt")
    print("Accuracy del sexto Test: ", "%.2f" % (T6*100))
    T7 = Controlador_3("Clasificador/tst/glass-10-7tst.dat", "Clasificador/tmp/ReglasEtiquetadas3-7.txt")
    print("Accuracy del septimo Test: ", "%.2f" % (T7*100))
    T8 = Controlador_3("Clasificador/tst/glass-10-8tst.dat", "Clasificador/tmp/ReglasEtiquetadas3-8.txt")
    print("Accuracy del octavo Test: ", "%.2f" % (T8*100))
    T9 = Controlador_3("Clasificador/tst/glass-10-9tst.dat", "Clasificador/tmp/ReglasEtiquetadas3-9.txt")
    print("Accuracy del noveno Test: ", "%.2f" % (T9*100))
    T10 = Controlador_3("Clasificador/tst/glass-10-10tst.dat", "Clasificador/tmp/ReglasEtiquetadas3-10.txt")
    print("Accuracy del decimo Test: ","%.2f" % (T10*100))

    resultado = ((T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 + T9 + T10)/10)*100
    print("\nMedia de Accuracy del Test ", "%.2f" % resultado)


training_5_todos()
training_3_todos()
controlador_5()
controlador_3()

# Training_5("Clasificador/training/glass-10-1tra.dat", "Clasificador/tmp/ReglasEtiquetadas5.txt")
# Training_3("Clasificador/training/glass-10-1tra.dat", "Clasificador/tmp/ReglasEtiquetadas3.txt")
# AciertTraining = Controlador_5("Clasificador/training/glass-10-1tra.dat", "Clasificador/tmp/ReglasEtiquetadas5.txt")
# AciertoTest = Controlador_5("Clasificador/tst/glass-10-1tst.dat", "Clasificador/tmp/ReglasEtiquetadas5.txt")
# print("Acierto del training = ", AciertTraining)
# print("Acierto de Test = ", AciertoTest)
# AciertTraining = Controlador_3("Clasificador/training/glass-10-1tra.dat", "Clasificador/tmp/ReglasEtiquetadas3.txt")
# AciertoTest = Controlador_3("Clasificador/tst/glass-10-1tst.dat", "Clasificador/tmp/ReglasEtiquetadas3.txt")
# print("Acierto del training 3 Etiquetas = ", AciertTraining)
# print("Acierto de Test = ", AciertoTest)
#Controlador("tst/delta_ail-5-1tst.dat","tmp/ReglasEtiquetadas5.txt")
#Controlador("training/delta_ail-5-2tra.dat","tmp/ReglasEtiquetadas5.txt")
#Training_3("training/delta_ail-5-3tra.dat", "tmp/ReglasEtiquetadas3.txt")