
archs = ['tablaxy1.txt',
         'tablaxy2.txt',
         'tablaxy3.txt']

def leer(archivo):
    arch = open(archivo,'r')
    lineas = arch.readlines()
    
    return lineas

def calcular(archivo):
    cont=0
    acum_x=0
    acum_y=0
    min_x=float('inf')
    max_x=0
    min_y=float('inf')
    max_y=0
    lst_archivo = leer(archivo)

    for registro in lst_archivo:
        lst_linea=registro.split(',')
        x=float(lst_linea[0])
        y=float(lst_linea[1].rstrip('\n'))
        acum_x += x
        acum_y += y
        cont += 1
        if max_x < x:
            max_x = x
        if min_x > x:
            min_x = x
        if max_y < y:
            max_y = y
        if min_y > y:
            min_y = y
            
    prom_x = acum_x / cont
    prom_y = acum_y / cont
    
    return acum_x,acum_y,max_x,max_y,min_x,min_y,prom_x,prom_y
        
def main():
    
    for i in archs:
        lst_archivo = leer(i)
        print('archivo: ',i)
        for registro in lst_archivo:
            lst_linea=registro.split(',')
            x=float(lst_linea[0])
            y=float(lst_linea[1].rstrip('\n'))
            print(x,y)
        
        #print('\n')
        total_x,total_y,max_x,max_y,min_x,min_y,prom_x,prom_y = calcular(i)
        print(f'la sumatoria de x es= {total_x}')
        print(f'la sumatoria de y es= {total_y}')
        print(f'la valor max de x es= {max_x}')
        print(f'la valor max de y es= {max_y}')
        print(f'la valor min de x es= {min_x}')
        print(f'la valor min de y es= {min_y}')
        print(f'El promedio de x es= {prom_x:.2f}')
        print(f'El promedio de y es= {prom_y:.2f}')
        print('\n')

main()
    
    