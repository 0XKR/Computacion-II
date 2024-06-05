def leer_arch(archivo):
    
    arch = open(archivo,'r')
    contenido = arch.readlines()
    lst_horario = []
    
    for i in range(len(contenido)):
        linea = contenido[i].split(',')
        codigo = linea[0]
        asig = linea[1]
        seccion = linea[2]
        prof = linea[3]
        lst_horas = []
        for j in range(4,len(linea)):
            lst_horas.append(linea[j])
        
        lst_horario.append([codigo,asig,seccion,prof,lst_horas])
    return lst_horario

def crear_dict():
    lst_horario = leer_arch('horario.txt')
    
    b=[]
    t=[]
    elec=[]
    m=[]
    q=[]
    c=[]
    i=[]
    
    for _ in range(len(lst_horario)):
        cod = lst_horario[_][0]
        asig = lst_horario[_][1]
        seccion = lst_horario[_][2]
        prof = lst_horario[_][3]
        horas = lst_horario[_][4]
        horario = [cod,asig,seccion,prof,horas]
        e = cod[3] #escuela
        
        if e == 'b':
            b.append(horario)
        
        elif e == 't':
            t.append(horario)
        elif e == 'e':
            elec.append(horario) 
        elif e == 'm':
            m.append(horario)
        elif e == 'q':
            q.append(horario)
        elif e == 'c':
            c.append(horario) 
        else:
            i.append(horario)
    
    dict_1 = {'b':b,'t':t,'e':elec,'m':m,'q':q,'c':c,'i':i}
    return dict_1

def contar_secc():
    lst_horario = leer_arch('horario.txt')
    dict_secciones = {}
    cod = ''
    
    lst_cods = []
    band = True

    for i in range(len(lst_horario)):
            
        cod_act = lst_horario[i][0]
        
        lst_cods.append(cod_act)
        
    for i in range(len(lst_horario)):
        
        cod_act = lst_horario[i][0]
        
        if cod != cod_act:
            num = lst_cods.count(cod_act)
            dict_secciones.setdefault(cod_act,num)
            cod = cod_act
            
    return dict_secciones

def p4y5(): #calc_porc_y_mayor()
    lst_horario = leer_arch('horario.txt')
    cont_aving = 0
    cont_total = 0
    
    asig_mayor = ''
    n_may = 0
    
    for _ in range(len(lst_horario)):
        cod = lst_horario[_][0]
        asig = lst_horario[_][1]
        seccion = lst_horario[_][2]
        prof = lst_horario[_][3]
        horas = lst_horario[_][4]
        n = len(horas)
        
        cerrada = horas[0]
        
        if not(cerrada == '(cerrada)'):
            if n > n_may:
                n_may = n
                asig_mayor = cod
                lst_mayor = [cod,int(n_may/2)]
            
            if 'aving' in horas:
                cont_aving += 1
            cont_total += 1
    porc = cont_aving * 100 / cont_total
    
    return porc,lst_mayor

def main():
    diccionarioPorEscuela = crear_dict()
    diccionarioNumeroSecciones = contar_secc()
    porcentaje,lst_asigMayorBloq = p4y5()
    print(diccionarioPorEscuela)
    print('')
    print(diccionarioNumeroSecciones)
    print('')
    print(porcentaje)
    print('')
    bloques_asign_mayor = int(diccionarioNumeroSecciones[lst_asigMayorBloq[0]]) * lst_asigMayorBloq[1]
    print(bloques_asign_mayor) ##suponiendo que cada seccion tenga la misma cantidad de bloques
    
main()
        
    
    
    
    
    
    

        
        
        
        
    
        
       

            
            
        
       
        
        
    
        
        
        
    
    
    