#lista de archivos 
archs=["tablaxy1.txt",
      "tablaxy2.txt",
      "tablaxy3.txt"]
#funcion de leer archivo 
def leer(archivo):
    arch=open(archivo,"r")
    lineas=arch.readlines()
    return lineas #devuelve lista con las lineas 

#funcion de calculos 
def calcular(archivo):
    #inicializamos contadores y acumuladores
    c=0
    x_sum=0
    y_sum=0
    acum_x2 = 0
    acum_xy = 0
    min_x=float("inf")
    max_x=0
    min_y=float("inf")
    max_y=0
    
    lst_archivo=leer(archivo)
    
    #ciclo para recorrer cada linea del archivo
    for registro in lst_archivo:
        lst_linea=registro.split(",") #convierte la linea en 2 elementos (x,y)
        x=float(lst_linea[0])
        y=float(lst_linea[1].rstrip("\n")) #.rstrip se usa para quitar el salto de linea
        x_sum += x #sumatoria de x
        y_sum += y #sumatoria de y
    
        
        acum_x2 = acum_x2 + x ** 2 #calcular x²
        acum_xy = acum_xy + x * y #calcular x*y
        
        c += 1 #contador de lineas
        #calcular maximos y minimos
        if max_x<x:
            max_x=x
        if min_x>x:
            min_x=x
        if max_y<y:
            max_y=y
        if min_y>y:
            min_y=y
    
    #calcular promedios 
    prom_x=x_sum/c
    prom_y=y_sum/c
    
    c1 = (c*acum_xy - x_sum*y_sum)/(c*acum_x2-x_sum**2)
    c2 = (y_sum/c)-(c1*x_sum)/c
    
    error = 0
    
    #se usa otro ciclo para calcular el error (porque es una sumatoria)
    for registro in lst_archivo:
        lst_linea=registro.split(",")
        x=float(lst_linea[0])
        y=float(lst_linea[1].rstrip("\n"))
        
        error = error + (y-c2-c1*x)**2 
    
    #retornamos las variables
    return x_sum,y_sum,max_x,min_x,max_y,min_y,prom_x,prom_y,acum_x2,acum_xy,c1,c2,error
        
def main():
    
    #ciclo para recorrer los n archivos
    for archivo in archs:
        lst_archivo=leer(archivo) #llamamos la funcion leer para leer el archivo
        print("archivo:",archivo)
        for registro in lst_archivo:
            lst_linea=registro.split(",")
            x=float(lst_linea[0])
            y=float(lst_linea[1].rstrip("\n"))
            print(f"X={x}",f"Y={y}")
        #llamamos a la funcion calcular para procesar los datos del archivo
        xs,ys,max_x,min_x,max_y,min_y,prom_x,prom_y,acum_x2,acum_xy,c1,c2,error=calcular(archivo)
        #impresion en pantalla
        print(f"sumatoria de x={xs:.2f}")
        print(f"sumatoria de y={ys:.2f}")
        print(f"maximo valor de x={max_x:.2f}")
        print(f"minimo valor de x={min_x:.2f}")
        print(f"maximo valor de y={max_y:.2f}")
        print(f"minimo valor de y={min_y:.2f}")
        print(f"promedio de los valores de  x={prom_x:.2f}")
        print(f"promedio de los valores de y={prom_y:.2f}")
        print(f"suma de x²={acum_x2:.2f}")
        print(f"suma de x*y={acum_xy:.2f}")
        print(f'Y=({c1:.2f})X+({c2:.2f})+({error:.2f})')
        print("\n")

main()   #llamada del main


#----_&&&&&&&_#$&---

    
    
    