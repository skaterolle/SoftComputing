

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
            numero = [str(x) for x in line.rstrip('\n').split(',')]
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
    Regla_R = [etiqueta_5(Regla[0],AT1), etiqueta_5(Regla[1],AT2), etiqueta_5(Regla[2],AT3), etiqueta_5(Regla[3],AT4), etiqueta_5(Regla[4],AT5), etiqueta_5(Regla[5],ATC)]
    return Regla_R
    
# Devuelve la Regla con las etiquetas ya establecidas para 3 etiquetas
def etiquetado_3(Regla, AT1, AT2, AT3, AT4, AT5, ATC):
    Regla_R = [etiqueta_3(Regla[0],AT1), etiqueta_3(Regla[1],AT2), etiqueta_3(Regla[2],AT3), etiqueta_3(Regla[3],AT4), etiqueta_3(Regla[4],AT5), etiqueta_3(Regla[5],ATC)]
    return Regla_R

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
            if set(Regla) == set(Igual):
                encontrado = True
        if not encontrado:
            #print(i)
            Iguales.append(Regla)
    return Iguales

def comprueba_antecedentes(List):
    for x in range(len(List)):
        for y in range(len(List)):
            if x != y:
                if (List[x][0] == List[y][0]) and (List[x][1] == List[y][1]) and (List[x][2] == List[y][2]) and (List[x][3] == List[y][3]) and (List[x][4] == List[y][4]):
                    print("Iguales, X = ", x, " Y = ", y)
                    print("X = ", List[x][:-1])
                    print("Y = ", List[y][:-1])

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

def Training_5(File):
    # Definición de variables de reglas
    Reglas_Iniciales = []
    Reglas_Etiquetadas = []
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
            if (Regla[0] == Igual[0]) and (Regla[1] == Igual[1]) and (Regla[2] == Igual[2]) and (Regla[3] == Igual[3]) and (Regla[4] == Igual[4]) and (Regla[5] == Igual[5]):
            #if set(Regla) == set(Igual): Esto está mal, ya que no comprueba si son iguales, sino si dentro de la Lista contienen los mismos elementos sin que estén en el mismo orden
                encontrado = True
        if not encontrado:
            Iguales.append(Regla)
    
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

    for x in range(len(Reglas_Iniciales)):
        if porcentaje < int((i*100)/len(Reglas_Iniciales)):
            porcentaje = int((i*100)/len(Reglas_Iniciales))
            print("Etiquetando Reglas: ", porcentaje, "%")
        Reglas_Etiquetadas.append(etiquetado_5(Reglas_Iniciales[x],AT1,AT2,AT3,AT4,AT5,ATC))

    #for x in range(len(Reglas_Etiquetadas)):
    Iguales = Descarta_Iguales("Descartando Iguales: ",Reglas_Etiquetadas)

    write_fileTSTR("ReglasEtiquetadas5.txt", Iguales)
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
    comprueba_antecedentes(Iguales)
    #print(Iguales)
    #print("Regla 1: ", etiquetado_5(Iguales[0],AT1,AT2,AT3,AT4,AT5,ATC))

def Training_3(File):
    # Definición de variables de reglas
    Reglas_Iniciales = []
    Reglas_Etiquetadas = []
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
            if (Regla[0] == Igual[0]) and (Regla[1] == Igual[1]) and (Regla[2] == Igual[2]) and (Regla[3] == Igual[3]) and (Regla[4] == Igual[4]) and (Regla[5] == Igual[5]):
            #if set(Regla) == set(Igual): Esto está mal, ya que no comprueba si son iguales, sino si dentro de la Lista contienen los mismos elementos sin que estén en el mismo orden
                encontrado = True
        if not encontrado:
            Iguales.append(Regla)
    

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

    for x in range(len(Reglas_Iniciales)):
        if porcentaje < int((i*100)/len(Reglas_Iniciales)):
            porcentaje = int((i*100)/len(Reglas_Iniciales))
            print("Etiquetando Reglas: ", porcentaje, "%")
        Reglas_Etiquetadas.append(etiquetado_3(Reglas_Iniciales[x],AT1,AT2,AT3,AT4,AT5,ATC))

    #for x in range(len(Reglas_Etiquetadas)):
    Iguales = Descarta_Iguales("Descartando Iguales: ",Reglas_Etiquetadas)

    write_fileTSTR("ReglasEtiquetadas3.txt", Iguales)
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
    #print(Iguales)
    #print("Regla 1: ", etiquetado_3(Iguales[0],AT1,AT2,AT3,AT4,AT5,ATC))

def Controlador(FileL,FileR):
    Reglas = read_fileR(FileR)
    Data = read_file(FileL)
    print(Reglas)

Controlador("tst/delta_ail-5-1tst.dat","ReglasEtiquetadas3.txt")
#Training_3("training/delta_ail-5-3tra.dat")
#Training_5("training/delta_ail-5-2tra.dat")
