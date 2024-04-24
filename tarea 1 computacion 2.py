#libreta de contactos
def calc_edad(anio):
    
    edad=2024-int(anio)
    return edad

def agregar(lista):    
    
    telf = input('ingrese el telefono: ')
    nomb = input('ingrese el nombre: ')
    apell = input('ingrese el apellido: ')
    dia = input('ingrese el dia de nacimiento: ')
    mes = input('ingrese el mes de nacimiento: ')
    anio = input('ingrese el anho de nacimiento: ')
    fecha = (dia,mes,anio)
    edad = calc_edad(anio)
    lst_contacto = [telf,nomb,apell,fecha,edad]
    lista.extend([lst_contacto])
    return lista

def consultar(lista):
    
    apellido = input('ingrese el apellido a consultar:')
    resp = 's'
    for j in range(len(lista)):  
        if lista[j][2] == apellido:
            lst_contacto = lista[j]
                #cad=','.join(lst_contacto)
                
            if resp == 's':
                print(f'el contacto es: {lst_contacto}')
                    
            else:
                break
        resp = input('quieres consultar si hay otro contacto con ese apellido? [s/n]:')
    print('\nno se encontraron mas contactos con ese apellido')
def mod(lista):
    
    tlf = input('Inserte el numero de telefono del contacto a modificar: ')
    resp = ''
    for i in range(len(lista)):
        if lista[i][0] == tlf:
            lst_contacto = lista[i]
            #cad = ','.join(lst_contacto)
            resp = input(f'Desea modificar el contacto: {lst_contacto} [s/n]?: ')
            if resp == 's':
                telf = input('ingrese el nuevo telefono: ')
                nomb = input('ingrese el nuevo nombre: ')
                apell = input('ingrese el nuevo apellido: ')
                dia = input('ingrese el nuevo dia de nacimiento: ')
                mes = input('ingrese el nuevo mes de nacimiento: ')
                anio = input('ingrese el nuevo anho de nacimiento: ')
                fecha = (dia,mes,anio)
                edad = calc_edad(anio)
                lst_contacto = [telf,nomb,apell,fecha,edad]
                lista[i] = lst_contacto
                return lista
            else:
                break
                
    print('No se encontro ese numero =c')          

def eliminar(lista):
    
    tlf = input('Inserte el numero de telefono del contacto a eliminar: ')
    resp = 'n'
    for k in range(len(lista)):
        if lista[k][0] == tlf:
            lst = lista[k]
            #cad = ','.join(lst)
            resp = input(f'Estas seguro de querer eliminar el contacto {lst}?[s/n]')
            if resp == 's':
                lista.pop(k)
                break

        else:
            print('No se elimino ningun contacto')   

def main():
    
    print('Bienvenido al programa!')
    print('_'*25+'\n'+'_'*25)
    print('Libreta de contactos...')
    lst_contactos = []
    while True:
        print('\n\nOpciones:\n1.Agregar contacto\n2.Consultar contacto\n3.Modificar contacto\n4.Eliminar contacto\n5.salir')
        resp = int(input('elija un opcion: '))
        if resp == 1:
            lst_contactos = agregar(lst_contactos)
        elif resp == 2:
            consultar(lst_contactos)
        elif resp == 3:
            lst_contactos = mod(lst_contactos)
        elif resp == 4:
            lst_contactos = eliminar(lst_contactos)
        else:
            break

if __name__ == '__main__':
    main()