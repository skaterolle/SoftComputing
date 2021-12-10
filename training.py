

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

def read_fileR(File):
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
        if "@attribute" in line:
            numero = [float(x) for x in line.partition('[')[2].replace('[','').replace(']','').strip("[ \n").split(',')]
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
            #print(list[x][y])
            f.write(list[x][y])
            if y < (len(list[x]) - 1):
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
def etiquetado_5(Regla, AT1, AT2, AT3, AT4, AT5, ATC):
    E1 = etiqueta_5(Regla[0],AT1)
    E2 = etiqueta_5(Regla[1],AT2)
    E3 = etiqueta_5(Regla[2],AT3)
    E4 = etiqueta_5(Regla[3],AT4)
    E5 = etiqueta_5(Regla[4],AT5)
    EC = etiqueta_5(Regla[5],ATC)
    Regla_R = [E1, E2, E3, E4, E5, EC]
    A1 = matching_5(Regla[0],AT1, E1)
    A2 = matching_5(Regla[1],AT2, E2)
    A3 = matching_5(Regla[2],AT3, E3)
    A4 = matching_5(Regla[3],AT4, E4)
    A5 = matching_5(Regla[4],AT5, E5)
    C = matching_5(Regla[5],ATC, EC)
    # Este sirve en el caso que queramos sacarlo mediante la suma de todos
    # emparejamiento = A1 + A2 + A3 + A4 + A5 + C
    # Minimo
    #emparejamiento = min(A1, A2, A3, A4, A5)
    # Producto
    emparejamiento = (A1 + A2 + A3 + A4 + A5 + C)/6
    Regla_R.append(emparejamiento)
    return Regla_R
    
# Devuelve la Regla con las etiquetas ya establecidas para 3 etiquetas
def etiquetado_3(Regla, AT1, AT2, AT3, AT4, AT5, ATC):
    E1 = etiqueta_3(Regla[0],AT1)
    E2 = etiqueta_3(Regla[1],AT2)
    E3 = etiqueta_3(Regla[2],AT3)
    E4 = etiqueta_3(Regla[3],AT4)
    E5 = etiqueta_3(Regla[4],AT5)
    EC = etiqueta_3(Regla[5],ATC)
    Regla_R = [E1, E2, E3, E4, E5, EC]
    A1 = matching_3(Regla[0],AT1, E1)
    A2 = matching_3(Regla[1],AT2, E2)
    A3 = matching_3(Regla[2],AT3, E3)
    A4 = matching_3(Regla[3],AT4, E4)
    A5 = matching_3(Regla[4],AT5, E5)
    C = matching_3(Regla[5],ATC, EC)
    # Este sirve en el caso que queramos sacarlo mediante la suma de todos
    # emparejamiento = A1 + A2 + A3 + A4 + A5 + C
    # Minimo
    emparejamiento = min(A1, A2, A3, A4, A5)
    # Producto
    emparejamiento = (A1 + A2 + A3 + A4 + A5 + C)/6
    Regla_R.append(emparejamiento)
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
def Descarta_Iguales(texto, Reglas_Iniciales):
    porcentaje = 0
    Iguales = []
    for i in range(len(Reglas_Iniciales)):
        Regla = Reglas_Iniciales[i]
        encontrado = False
        if porcentaje < int((i*100)/len(Reglas_Iniciales)):
            porcentaje = int((i*100)/len(Reglas_Iniciales))
            print(texto, porcentaje, "%")
        for j in range(len(Iguales)):
            Igual = Iguales[j]
            if (Regla[0] == Igual[0]) and (Regla[1] == Igual[1]) and (Regla[2] == Igual[2]) and (Regla[3] == Igual[3]) and (Regla[4] == Igual[4]) and (Regla[5] == Igual[5]):
            #if set(Regla) == set(Igual):
                encontrado = True
        if not encontrado:
            #print(i)
            Iguales.append(Regla)
    return Iguales

# Comprueba si hay Reglas cuyos antecedentes sean iguales pero sus consecuentes diferentes, se pasa después de la función Descarta_Iguales() o Comprueba_Reglas()
def comprueba_antecedentes(List):
    for x in range(len(List)):
        for y in range(len(List)):
            if x != y:
                if (List[x][0] == List[y][0]) and (List[x][1] == List[y][1]) and (List[x][2] == List[y][2]) and (List[x][3] == List[y][3]) and (List[x][4] == List[y][4]):
                    print("Iguales, X = ", x, " Y = ", y)
                    print("X = ", List[x][:-1], " Matching = ", List[x][6])
                    print("Y = ", List[y][:-1], " Matching = ", List[y][6])
                    if List[x][6] > List[y][6]:
                        List.pop(y)
                    else:
                        List.pop(x)

# Comprueba cada reglas si sus antecedentes son iguales pero sus consecuentes diferentes y coge el matching que se hizo al etiquetar cada regla
# Y se escoge aquel que tenga mayor matching, Devuelve la Lista de Reglas sin el matching
def comprueba_Reglas(List):
    Reglas_Afinadas = []
    for x in range(len(List)):
        encontrado = False
        for y in range(len(Reglas_Afinadas)):
            if (List[x][0] == Reglas_Afinadas[y][0]) and (List[x][1] == Reglas_Afinadas[y][1]) and (List[x][2] == Reglas_Afinadas[y][2]) and (List[x][3] == Reglas_Afinadas[y][3]) and (List[x][4] == Reglas_Afinadas[y][4]):
                # print("Iguales, X = ", x, " Y = ", y)
                # print("X = ", List[x][:-1], " Matching = ", List[x][6])
                # print("Y = ", Reglas_Afinadas[y][:-1], " Matching = ", Reglas_Afinadas[y][6])
                encontrado = True
                if List[x][6] > Reglas_Afinadas[y][6]:
                    Reglas_Afinadas.pop(y)
                    Reglas_Afinadas.append(List[x])
        if not encontrado:
            Reglas_Afinadas.append(List[x])
    Reglas = []
    for x in range(len(Reglas_Afinadas)):
        Reglas.append(Reglas_Afinadas[x][:-1])
    return Reglas

def prueba1(File):
    # Definición de variables de reglas
    Reglas_Iniciales = []
    Iguales = []
    # Definición de variables de Minimos y Máximos
    A1 = [0,0]
    A2 = [0,0]
    A3 = [0,0]
    A4 = [0,0]
    A5 = [0,0]
    C = [0,0]
    # Definición de variables de etiquetas
    AT1 = []
    AT2 = []
    AT3 = []
    AT4 = []
    AT5 = []
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
    DivC = (C[1] - C[0])/5
    ATC = [C[0] , C[0] + DivC, C[0] + DivC*2, C[0] + DivC*3, C[0] + DivC*4, C[0] + DivC*5]

    # Muestra por pantalla
    print("Reglas Totales: ", len(Iguales))
    print("Antecedente 1: ", A1)
    print("Antecedente 2: ", A2)
    print("Antecedente 3: ", A3)
    print("Antecedente 4: ", A4)
    print("Antecedente 5: ", A5)
    print("Consecuente: ", C)
    print("Divisor AT1: ", Div1)
    print("Triangulos AT1: ", AT1)
    print("Divisor AT2: ", Div2)
    print("Triangulos AT2: ", AT2)
    print("Divisor AT3: ", Div3)
    print("Triangulos AT3: ", AT3)
    print("Divisor AT4: ", Div4)
    print("Triangulos AT4: ", AT4)
    print("Divisor AT5: ", Div5)
    print("Triangulos AT5: ", AT5)
    print("Divisor ATC: ", DivC)
    print("Triangulos ATC: ", ATC)
    print("Regla 1: ", etiquetado_5(Iguales[0],AT1,AT2,AT3,AT4,AT5,ATC))

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
    C = Min_Max[5]
    # Definición de variables de etiquetas
    AT1 = []
    AT2 = []
    AT3 = []
    AT4 = []
    AT5 = []
    Reglas_Iniciales = read_file(File)
    porcentaje = 0

    # Comprueba los minimos y máximos de cada antecedente y consecuente y quita aquellas entradas que sean iguales
    for i in range(len(Reglas_Iniciales)):
        Regla = Reglas_Iniciales[i]
        encontrado = False
        # A1[0] = comparacion_menor(A1[0],Regla[0]) 
        # A2[0] = comparacion_menor(A2[0],Regla[1]) 
        # A3[0] = comparacion_menor(A3[0],Regla[2]) 
        # A4[0] = comparacion_menor(A4[0],Regla[3]) 
        # A5[0] = comparacion_menor(A5[0],Regla[4]) 
        # C[0] = comparacion_menor(C[0],Regla[5])

        # A1[1] = comparacion_mayor(A1[1],Regla[0]) 
        # A2[1] = comparacion_mayor(A2[1],Regla[1]) 
        # A3[1] = comparacion_mayor(A3[1],Regla[2]) 
        # A4[1] = comparacion_mayor(A4[1],Regla[3]) 
        # A5[1] = comparacion_mayor(A5[1],Regla[4]) 
        # C[1] = comparacion_mayor(C[1],Regla[5])
        if porcentaje < int((i*100)/len(Reglas_Iniciales)):
            porcentaje = int((i*100)/len(Reglas_Iniciales))
            print("Descartando Reglas iguales: ", porcentaje, "%")
        for j in range(len(Iguales)):
            Igual = Iguales[j]
            if (Regla[0] == Igual[0]) and (Regla[1] == Igual[1]) and (Regla[2] == Igual[2]) and (Regla[3] == Igual[3]) and (Regla[4] == Igual[4]) and (Regla[5] == Igual[5]):
            #if set(Regla) == set(Igual): Esto está mal, ya que no comprueba si son iguales, sino si dentro de la Lista contienen los mismos elementos sin que estén en el mismo orden
                encontrado = True
        if not encontrado:
            Iguales.append(Regla)
    
    # Saca los triangulos (Inicio y Final) de cada Antecedente y Consecuente y los guarda en una Lista
    Div1 = (A1[1] - A1[0])/5
    AT1 = [A1[0] , A1[0] + Div1, A1[0] + Div1*2, A1[0] + Div1*3, A1[0] + Div1*4, A1[0] + Div1*5]
    Div2 = (A2[1] - A2[0])/5
    AT2 = [A2[0] , A2[0] + Div2, A2[0] + Div2*2, A2[0] + Div2*3, A2[0] + Div2*4, A2[0] + Div2*5 + 0.000001] # Hay un fallo por lo que se reduce en centesimas 1 punto y hace que falle
    Div3 = (A3[1] - A3[0])/5
    AT3 = [A3[0] , A3[0] + Div3, A3[0] + Div3*2, A3[0] + Div3*3, A3[0] + Div3*4, A3[0] + Div3*5]
    Div4 = (A4[1] - A4[0])/5
    AT4 = [A4[0] , A4[0] + Div4, A4[0] + Div4*2, A4[0] + Div4*3, A4[0] + Div4*4, A4[0] + Div4*5]
    Div5 = (A5[1] - A5[0])/5
    AT5 = [A5[0] , A5[0] + Div5, A5[0] + Div5*2, A5[0] + Div5*3, A5[0] + Div5*4, A5[0] + Div5*5]
    DivC = (C[1] - C[0])/5
    ATC = [C[0] , C[0] + DivC, C[0] + DivC*2, C[0] + DivC*3, C[0] + DivC*4, C[0] + DivC*5]

    Reglas_Iniciales = Iguales
    Iguales = []
    porcentaje = 0

    # Etiqueta cada regla y les agrega su matching para usar más tarde
    for x in range(len(Reglas_Iniciales)):
        if porcentaje < int((i*100)/len(Reglas_Iniciales)):
            porcentaje = int((i*100)/len(Reglas_Iniciales))
            print("Etiquetando Reglas: ", porcentaje, "%")
        Reglas_Etiquetadas.append(etiquetado_5(Reglas_Iniciales[x],AT1,AT2,AT3,AT4,AT5,ATC))
    #Iguales = Reglas_Etiquetadas
    #for x in range(len(Reglas_Etiquetadas)):
    Iguales = Descarta_Iguales("Descartando Iguales: ",Reglas_Etiquetadas)

    Reglas_Iniciales = Iguales
    Iguales = []

    # Compruba cada Regla y quita aquellas cuyos antecedentes sean iguales y consecuentes diferentes eligiendo los que tengan un matching mayor
    # Devuelve una Lista sin el matching
    Iguales = comprueba_Reglas(Reglas_Iniciales)
    write_fileTSTR(SaveFile, Iguales[:][:-1])
    comprueba_antecedentes(Iguales)

    # Muestra por pantalla
    print("Reglas Totales: ", len(Iguales))
    print("Antecedente 1: ", A1)
    print("Antecedente 2: ", A2)
    print("Antecedente 3: ", A3)
    print("Antecedente 4: ", A4)
    print("Antecedente 5: ", A5)
    print("Consecuente: ", C)
    # print("Divisor AT1: ", Div1)
    # print("Triangulos AT1: ", AT1)
    # print("Divisor AT2: ", Div2)
    # print("Triangulos AT2: ", AT2)
    # print("Divisor AT3: ", Div3)
    # print("Triangulos AT3: ", AT3)
    # print("Divisor AT4: ", Div4)
    # print("Triangulos AT4: ", AT4)
    # print("Divisor AT5: ", Div5)
    # print("Triangulos AT5: ", AT5)
    # print("Divisor ATC: ", DivC)
    # print("Triangulos ATC: ", ATC)
    #print(Iguales[1][:-1]) # El [:-1] hace que sea la lista menos el último elemento
    #print(Iguales)
    #print("Regla 1: ", etiquetado_5(Iguales[0],AT1,AT2,AT3,AT4,AT5,ATC))

def Training_3(File, SaveFile):
    # Definición de variables de reglas
    Reglas_Iniciales = []
    Reglas_Etiquetadas = []
    Min_Max = read_min_max(File)
    Iguales = []
    # Definición de variables de Minimos y Máximos
    # A1 = [0,0]
    # A2 = [0,0]
    # A3 = [0,0]
    # A4 = [0,0]
    # A5 = [0,0]
    # C = [0,0]
    A1 = Min_Max[0]
    A2 = Min_Max[1]
    A3 = Min_Max[2]
    A4 = Min_Max[3]
    A5 = Min_Max[4]
    C = Min_Max[5]
    # Definición de variables de etiquetas
    AT1 = []
    AT2 = []
    AT3 = []
    AT4 = []
    AT5 = []
    Reglas_Iniciales = read_file(File)
    porcentaje = 0

    # Comprueba los minimos y máximos de cada antecedente y consecuente y quita aquellas entradas que sean iguales
    for i in range(len(Reglas_Iniciales)):
        Regla = Reglas_Iniciales[i]
        encontrado = False
        # A1[0] = comparacion_menor(A1[0],Regla[0]) 
        # A2[0] = comparacion_menor(A2[0],Regla[1]) 
        # A3[0] = comparacion_menor(A3[0],Regla[2]) 
        # A4[0] = comparacion_menor(A4[0],Regla[3]) 
        # A5[0] = comparacion_menor(A5[0],Regla[4]) 
        # C[0] = comparacion_menor(C[0],Regla[5])

        # A1[1] = comparacion_mayor(A1[1],Regla[0]) 
        # A2[1] = comparacion_mayor(A2[1],Regla[1]) 
        # A3[1] = comparacion_mayor(A3[1],Regla[2]) 
        # A4[1] = comparacion_mayor(A4[1],Regla[3]) 
        # A5[1] = comparacion_mayor(A5[1],Regla[4]) 
        # C[1] = comparacion_mayor(C[1],Regla[5])
        if porcentaje < int((i*100)/len(Reglas_Iniciales)):
            porcentaje = int((i*100)/len(Reglas_Iniciales))
            print("Descartando Reglas iguales: ", porcentaje, "%")
        for j in range(len(Iguales)):
            Igual = Iguales[j]
            if (Regla[0] == Igual[0]) and (Regla[1] == Igual[1]) and (Regla[2] == Igual[2]) and (Regla[3] == Igual[3]) and (Regla[4] == Igual[4]) and (Regla[5] == Igual[5]):
            #if set(Regla) == set(Igual): Esto está mal, ya que no comprueba si son iguales, sino si dentro de la Lista contienen los mismos elementos sin que estén en el mismo orden
                encontrado = True
        if not encontrado:
            Iguales.append(Regla)
    
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
    DivC = (C[1] - C[0])/3
    ATC = [C[0] , C[0] + DivC, C[0] + DivC*2, C[0] + DivC*3]

    Reglas_Iniciales = Iguales
    Iguales = []
    porcentaje = 0

    # Etiqueta cada regla y les agrega su matching para usar más tarde
    for x in range(len(Reglas_Iniciales)):
        if porcentaje < int((i*100)/len(Reglas_Iniciales)):
            porcentaje = int((i*100)/len(Reglas_Iniciales))
            print("Etiquetando Reglas: ", porcentaje, "%")
        Reglas_Etiquetadas.append(etiquetado_3(Reglas_Iniciales[x],AT1,AT2,AT3,AT4,AT5,ATC))

    #for x in range(len(Reglas_Etiquetadas)):
    Iguales = Descarta_Iguales("Descartando Iguales: ",Reglas_Etiquetadas)

    Reglas_Iniciales = Iguales
    Iguales = []

    # Compruba cada Regla y quita aquellas cuyos antecedentes sean iguales y consecuentes diferentes eligiendo los que tengan un matching mayor
    # Devuelve una Lista sin el matching
    Iguales = comprueba_Reglas(Reglas_Iniciales)
    write_fileTSTR(SaveFile, Iguales[:][:-1])
    comprueba_antecedentes(Iguales)

    # Muestra por pantalla
    print("Reglas Totales: ", len(Iguales))
    print("Antecedente 1: ", A1)
    print("Antecedente 2: ", A2)
    print("Antecedente 3: ", A3)
    print("Antecedente 4: ", A4)
    print("Antecedente 5: ", A5)
    print("Consecuente: ", C)
    # print("Divisor AT1: ", Div1)
    # print("Triangulos AT1: ", AT1)
    # print("Divisor AT2: ", Div2)
    # print("Triangulos AT2: ", AT2)
    # print("Divisor AT3: ", Div3)
    # print("Triangulos AT3: ", AT3)
    # print("Divisor AT4: ", Div4)
    # print("Triangulos AT4: ", AT4)
    # print("Divisor AT5: ", Div5)
    # print("Triangulos AT5: ", AT5)
    # print("Divisor ATC: ", DivC)
    # print("Triangulos ATC: ", ATC)
    #comprueba_antecedentes(Iguales)
    #print(Iguales)
    #print("Regla 1: ", etiquetado_3(Iguales[0],AT1,AT2,AT3,AT4,AT5,ATC))

def Controlador_5(FileL,FileR):
    Reglas = read_fileR(FileR)
    Min_Max = read_min_max(FileL)
    #print(Min_Max)
    Data = read_file(FileL)
    # Definición de variables de Minimos y Máximos
    A1 = Min_Max[0]
    A2 = Min_Max[1]
    A3 = Min_Max[2]
    A4 = Min_Max[3]
    A5 = Min_Max[4]
    C = Min_Max[5]
    # Definición de variables de etiquetas
    AT1 = []
    AT2 = []
    AT3 = []
    AT4 = []
    AT5 = []
    porcentaje = 0
    # Saca los triangulos (Inicio y Final) de cada Antecedente y Consecuente y los guarda en una Lista
    Div1 = (A1[1] - A1[0])/5
    AT1 = [A1[0] , A1[0] + Div1, A1[0] + Div1*2, A1[0] + Div1*3, A1[0] + Div1*4, A1[0] + Div1*5]
    Div2 = (A2[1] - A2[0])/5
    AT2 = [A2[0] , A2[0] + Div2, A2[0] + Div2*2, A2[0] + Div2*3, A2[0] + Div2*4, A2[0] + Div2*5 + 0.000001] # Hay un fallo por lo que se reduce en centesimas 1 punto y hace que falle
    Div3 = (A3[1] - A3[0])/5
    AT3 = [A3[0] , A3[0] + Div3, A3[0] + Div3*2, A3[0] + Div3*3, A3[0] + Div3*4, A3[0] + Div3*5]
    Div4 = (A4[1] - A4[0])/5
    AT4 = [A4[0] , A4[0] + Div4, A4[0] + Div4*2, A4[0] + Div4*3, A4[0] + Div4*4, A4[0] + Div4*5]
    Div5 = (A5[1] - A5[0])/5
    AT5 = [A5[0] , A5[0] + Div5, A5[0] + Div5*2, A5[0] + Div5*3, A5[0] + Div5*4, A5[0] + Div5*5]
    DivC = (C[1] - C[0])/5
    ATC = [C[0] , C[0] + DivC, C[0] + DivC*2, C[0] + DivC*3, C[0] + DivC*4, C[0] + DivC*5]
    
    Estimado = Calcular_defuzzi_5(Reglas, Data, AT1, AT2, AT3, AT4, AT5, ATC)
    
    return Error_Cuadratico(Estimado, Data)
    #print(Reglas)

def Controlador_3(FileL,FileR):
    Reglas = read_fileR(FileR)
    Min_Max = read_min_max(FileL)
    #print(Min_Max)
    Data = read_file(FileL)
    # Definición de variables de Minimos y Máximos
    A1 = Min_Max[0]
    A2 = Min_Max[1]
    A3 = Min_Max[2]
    A4 = Min_Max[3]
    A5 = Min_Max[4]
    C = Min_Max[5]
    # Definición de variables de etiquetas
    AT1 = []
    AT2 = []
    AT3 = []
    AT4 = []
    AT5 = []
    porcentaje = 0
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
    DivC = (C[1] - C[0])/3
    ATC = [C[0] , C[0] + DivC, C[0] + DivC*2, C[0] + DivC*3]
    
    Estimado = Calcular_defuzzi_3(Reglas, Data, AT1, AT2, AT3, AT4, AT5, ATC)
    
    return Error_Cuadratico(Estimado, Data)
    #print(Reglas)

def Error_Cuadratico(Estimado, Real):
    suma = 0
    for i in range(len(Estimado)):
        suma = Real[i][5] - Estimado[i]
    Error = (suma * suma)/len(Estimado)
    return Error


def Calcular_defuzzi_5(Reglas, Datos, AT1, AT2, AT3, AT4, AT5, ATC):
    deffu = []
    for i in range(len(Datos)):
        h = []
        sumatorio_superior = 0
        for j in range(len(Reglas)):
            minimo = []
            minimo.append(matching_5(Datos[i][0], AT1, Reglas[j][0]))
            minimo.append(matching_5(Datos[i][1], AT2, Reglas[j][1]))
            minimo.append(matching_5(Datos[i][2], AT3, Reglas[j][2]))
            minimo.append(matching_5(Datos[i][3], AT4, Reglas[j][3]))
            minimo.append(matching_5(Datos[i][4], AT5, Reglas[j][4]))
            h.append(min(minimo))
            if Reglas[j][5] == "Bajo":
                PMV = (ATC[1] - ATC[0])/2
            elif Reglas[j][5] == "Medio-Bajo":
                PMV = (ATC[2] - ATC[1])/2
            elif Reglas[j][5] == "Medio":
                PMV = (ATC[3] - ATC[2])/2
            elif Reglas[j][5] == "Medio-Alto":
                PMV = (ATC[4] - ATC[3])/2
            elif Reglas[j][5] == "Alto":
                PMV = (ATC[5] - ATC[4])/2
            suma = PMV * min(minimo)
            sumatorio_superior = sumatorio_superior + suma
            # print("PMV = ", PMV)
            # print("Minimo = ", min(minimo))
            # print("Sumatorio = ", sumatorio_superior)
        # wait = input("Press Enter to continue.")
        if sum(h) == 0:
            resultado = 0
        else:
            resultado = sumatorio_superior/sum(h)
        deffu.append(resultado)
        # print("Sumatorio = ", sumatorio_superior)
        # print("Dividendo = ", sum(h))
        # print("Resultado = ", resultado)
        # wait = input("Press Enter to continue.")
    # print("Deffu = ", deffu)
    # wait = input("Press Enter to continue.")
    return deffu

def Calcular_defuzzi_3(Reglas, Datos, AT1, AT2, AT3, AT4, AT5, ATC):
    deffu = []
    for i in range(len(Datos)):
        h = []
        sumatorio_superior = 0
        for j in range(len(Reglas)):
            minimo = []
            minimo.append(matching_3(Datos[i][0], AT1, Reglas[j][0]))
            minimo.append(matching_3(Datos[i][1], AT2, Reglas[j][1]))
            minimo.append(matching_3(Datos[i][2], AT3, Reglas[j][2]))
            minimo.append(matching_3(Datos[i][3], AT4, Reglas[j][3]))
            minimo.append(matching_3(Datos[i][4], AT5, Reglas[j][4]))
            h.append(min(minimo))
            if Reglas[j][5] == "Bajo":
                PMV = (ATC[1] - ATC[0])/2
            elif Reglas[j][5] == "Medio":
                PMV = (ATC[2] - ATC[1])/2
            elif Reglas[j][5] == "Alto":
                PMV = (ATC[3] - ATC[2])/2
            suma = PMV * min(minimo)
            sumatorio_superior = sumatorio_superior + suma
        if sum(h) == 0:
            resultado = 0
        else:
            resultado = sumatorio_superior/sum(h)
        deffu.append(resultado)
    return deffu       
        
def Training_5_Grande():
    Training_5("training/delta_ail-5-1tra.dat", "tmp/ReglasEtiquetadas5-1.txt")
    Training_5("training/delta_ail-5-2tra.dat", "tmp/ReglasEtiquetadas5-2.txt")
    Training_5("training/delta_ail-5-3tra.dat", "tmp/ReglasEtiquetadas5-3.txt")
    Training_5("training/delta_ail-5-4tra.dat", "tmp/ReglasEtiquetadas5-4.txt")
    Training_5("training/delta_ail-5-5tra.dat", "tmp/ReglasEtiquetadas5-5.txt")

def Training_3_Grande():
    Training_3("training/delta_ail-5-1tra.dat", "tmp/ReglasEtiquetadas3-1.txt")
    Training_3("training/delta_ail-5-2tra.dat", "tmp/ReglasEtiquetadas3-2.txt")
    Training_3("training/delta_ail-5-3tra.dat", "tmp/ReglasEtiquetadas3-3.txt")
    Training_3("training/delta_ail-5-4tra.dat", "tmp/ReglasEtiquetadas3-4.txt")
    Training_3("training/delta_ail-5-5tra.dat", "tmp/ReglasEtiquetadas3-5.txt")

# Pruebas de controlador para 5 etiquetas con los 5 test y las 5 pruebas
def main_5():
    print("Errores cuadráticos 5 Etiquetas: ")
    print("--------------------")
    E1 = Controlador_5("training/delta_ail-5-1tra.dat","tmp/ReglasEtiquetadas5-1.txt")
    print("Error cuadrático Test 1: ", E1 )
    E2 = Controlador_5("training/delta_ail-5-2tra.dat","tmp/ReglasEtiquetadas5-2.txt")
    print("Error cuadrático Test 2: ", E2 )
    E3 = Controlador_5("training/delta_ail-5-3tra.dat","tmp/ReglasEtiquetadas5-3.txt")
    print("Error cuadrático Test 3: ", E3 )
    E4 = Controlador_5("training/delta_ail-5-4tra.dat","tmp/ReglasEtiquetadas5-4.txt")
    print("Error cuadrático Test 4: ", E4 )
    E5 = Controlador_5("training/delta_ail-5-5tra.dat","tmp/ReglasEtiquetadas5-5.txt")
    print("Error cuadrático Test 5: ", E5 )

    
    P1 = Controlador_5("tst/delta_ail-5-1tst.dat","tmp/ReglasEtiquetadas5-1.txt")
    print("Error cuadrático Prueba 1: ", P1 )
    P2 = Controlador_5("tst/delta_ail-5-2tst.dat","tmp/ReglasEtiquetadas5-2.txt")
    print("Error cuadrático Prueba 2: ", P2 )
    P3 = Controlador_5("tst/delta_ail-5-3tst.dat","tmp/ReglasEtiquetadas5-3.txt")
    print("Error cuadrático Prueba 3: ", P3 )
    P4 = Controlador_5("tst/delta_ail-5-4tst.dat","tmp/ReglasEtiquetadas5-4.txt")
    print("Error cuadrático Prueba 4: ", P4 )
    P5 = Controlador_5("tst/delta_ail-5-5tst.dat","tmp/ReglasEtiquetadas5-5.txt")
    print("Error cuadrático Prueba 5: ", P5 )

# Pruebas de controlador para 3 etiquetas con los 5 test y las 5 pruebas
def main_3():
    print("Errores cuadráticos 3 Etiquetastiquetas: ")
    print("--------------------")
    E1 = Controlador_5("training/delta_ail-5-1tra.dat","tmp/ReglasEtiquetadas3-1.txt")
    print("Error cuadrático Test 1: ", E1 )
    E2 = Controlador_5("training/delta_ail-5-2tra.dat","tmp/ReglasEtiquetadas3-2.txt")
    print("Error cuadrático Test 2: ", E2 )
    E3 = Controlador_5("training/delta_ail-5-3tra.dat","tmp/ReglasEtiquetadas3-3.txt")
    print("Error cuadrático Test 3: ", E3 )
    E4 = Controlador_5("training/delta_ail-5-4tra.dat","tmp/ReglasEtiquetadas3-4.txt")
    print("Error cuadrático Test 4: ", E4 )
    E5 = Controlador_5("training/delta_ail-5-5tra.dat","tmp/ReglasEtiquetadas3-5.txt")
    print("Error cuadrático Test 5: ", E5 )

    P1 = Controlador_5("tst/delta_ail-5-1tst.dat","tmp/ReglasEtiquetadas3-1.txt")
    print("Error cuadrático Prueba 1: ", P1 )
    P2 = Controlador_5("tst/delta_ail-5-2tst.dat","tmp/ReglasEtiquetadas3-2.txt")
    print("Error cuadrático Prueba 2: ", P2 )
    P3 = Controlador_5("tst/delta_ail-5-3tst.dat","tmp/ReglasEtiquetadas3-3.txt")
    print("Error cuadrático Prueba 3: ", P3 )
    P4 = Controlador_5("tst/delta_ail-5-4tst.dat","tmp/ReglasEtiquetadas3-4.txt")
    print("Error cuadrático Prueba 4: ", P4 )
    P5 = Controlador_5("tst/delta_ail-5-5tst.dat","tmp/ReglasEtiquetadas3-5.txt")
    print("Error cuadrático Prueba 5: ", P5 )

#Training_3_Grande()
main_5()    
main_3()
#Training_5("training/delta_ail-5-2tra.dat", "tmp/ReglasEtiquetadas5.txt")
#Controlador("tst/delta_ail-5-1tst.dat","tmp/ReglasEtiquetadas5.txt")
#Controlador("training/delta_ail-5-2tra.dat","tmp/ReglasEtiquetadas5.txt")
#Training_3("training/delta_ail-5-3tra.dat", "tmp/ReglasEtiquetadas3.txt")







