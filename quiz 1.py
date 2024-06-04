def leer_insc(archivo):
    arch = open(archivo,'r')
    contenido = arch.readlines()
    lst_inscritos = []

    for i in range(len(contenido)):
        l = contenido[i].strip('\n') #esto para quitar el salto de linea
        linea = l.split(',')
        ced = linea[0]
        nom = linea[1]
        materias = []
        for j in range(2,len(linea)):
            materias.append(linea[j])

        valor = [ced,nom,materias]
        lst_inscritos.append(valor)
    arch.close()
    return lst_inscritos

def leer_pensum(archivo):
    arch = open(archivo,'r')
    contenido = arch.readlines()
    escuela = contenido[0].strip('\n')
    lst_pensum = []
    for i in range(1,len(contenido)):
        linea = contenido[i].split(',')
        cod = linea[0]
        asig = linea[1]
        t = int(linea[2])
        p = int(linea[3])
        l = int(linea[4])
        uc = float(linea[5])
        lst_req = []
        for j in range(6,len(linea)):
            lst_req.append(linea[j])
            
        valor = [cod,asig,t,p,l,uc,lst_req]
        lst_pensum.append(valor)
    arch.close()

    return lst_pensum

def crear_dicc():
    lst_inscritos = leer_insc('inscritos.txt')
    dict1 = {}
    lista_basico = []
    s1 = []
    s2 = []
    s3 = []
    s4 = []
    s5 = []
    s6 = []
    s7 = []
    s8 = []
    s9 = []
    s10 = []

    for i in range(len(lst_inscritos)):
        cod = lst_inscritos[i][2][0]
        ced = lst_inscritos[i][0]
        nom = lst_inscritos[i][1]
        asig = lst_inscritos[i][2]
        semestre = int(cod[2])
        basico = cod[3]

        if basico == 'b':
            lista_basico.append(nom)
        
        if semestre == 1:
            s1.append([ced,asig])
        elif semestre == 2:
            s2.append([ced,asig])
        elif semestre == 3:
            s3.append([ced,asig])
        elif semestre == 4:
            s4.append([ced,asig])
        elif semestre == 5:
            s5.append([ced,asig])
        elif semestre == 6:
            s6.append([ced,asig])
        elif semestre == 7:
            s7.append([ced,asig])
        elif semestre == 8:
            s8.append([ced,asig])
        elif semestre == 9:
            s9.append([ced,asig])
        else:
            s10.append([ced,asig])
        dict1 = {1:s1,2:s2,3:s3,4:s4,5:s5,6:s6,7:s7,8:s8,9:s9,10:s10}

    return dict1,lista_basico

def calc_horas():

    lst_inscritos = leer_insc('inscritos.txt')
    lst_pensum = leer_pensum('pensum.txt')
    lst_alumnosYhoras = []
    cont_paral = 0
    for i in range(len(lst_inscritos)):
        
        horas = 0
        nombre = lst_inscritos[i][1]
        materias = lst_inscritos[i][2]
        band = True
        for j in range(len(lst_pensum)):
            materia = lst_pensum[j][0]
            hora_p = lst_pensum[j][2]
            hora_t = lst_pensum[j][3]
            hora_l = lst_pensum[j][4]
            requisitos = lst_pensum[j][6]
            hora_total = hora_t + hora_l + hora_p 

            if materia in materias:
                horas += hora_total

                if ('//' in requisitos) and band:
                    cont_paral += 1
                    band = False
            
        lst_alumnosYhoras.append([nombre,horas])
    
    return lst_alumnosYhoras,cont_paral

a,b = calc_horas()
print(a)
print(b)


            
            








