from sentencias import *
from myClear import clear as cl
from prettytable import PrettyTable
import htmlS
import fechas
from datetime import date
from colorama import Fore, Back, Style, init
init()
def gestion():
    cl() # clear
    print(Fore.CYAN+'''
$$$$$$\  $$$$$$$$\  $$$$$$\ $$$$$$$$\ $$$$$$\  $$$$$$\  $$\   $$\ 
$$  __$$\ $$  _____|$$  __$$\\__$$  __|\_$$  _|$$  __$$\ $$$\  $$ |
$$ /  \__|$$ |      $$ /  \__|  $$ |     $$ |  $$ /  $$ |$$$$\ $$ |
$$ |$$$$\ $$$$$\    \$$$$$$\    $$ |     $$ |  $$ |  $$ |$$ $$\$$ |
$$ |\_$$ |$$  __|    \____$$\   $$ |     $$ |  $$ |  $$ |$$ \$$$$ |
$$ |  $$ |$$ |      $$\   $$ |  $$ |     $$ |  $$ |  $$ |$$ |\$$$ |
\$$$$$$  |$$$$$$$$\ \$$$$$$  |  $$ |   $$$$$$\  $$$$$$  |$$ | \$$ |
 \______/ \________| \______/   \__|   \______| \______/ \__|  \__|                                    
    1- Agregar caso
    2- Modificar caso 
    3- Eliminar Caso
        (x) Volver al menu
        ''')
    tmp = input('\nSeleccione una opcion >>>> ')
    if tmp == '1':
        insert()
    elif tmp == '2':
        update()
    elif tmp == '3':
        delete()
    elif 'x' in tmp or 'X':
        return False
    else:
        input('''Esa opcion no se encontro...
                ( Presiona enter para continuar )''')

def fecha():
    dD = input('Digite el dia: ')
    dY = input('Digite el año: ')
    dM = input('Digite el mes: ')

    if comprob_int(dD) and comprob_int(dY) and comprob_int(dM):
        dD = int(dD); dY = int(dY); dM = int(dM);
        date_x = date(dY, dM, dD)
        return date_x
    else:
        return False

#/////////////////////////////Reportes
conexion = sqlite3.connect('robos.db')
cur = conexion.cursor() #Cursor

def select_custom(campos, tbl_field):
    cl()
    tbl = PrettyTable()
    tbl.field_names = tbl_field
    a = cur.execute(f'Select {campos} from casos_vw ')
    b = []
    cont = 0
    for x in a:
        b.append([x])
        tbl.add_rows(b[cont])
        cont += 1
    print('---------<<Carros robados: ',len(b))
    print(tbl)

#-------------Joins y group by
def group_custom(campo,tbl_field,tabla):
    cl()
    tbl = PrettyTable()
    tbl.field_names = tbl_field
    b = cur.execute(f'''SELECT {campo}, 
                    count({campo})
                    from {tabla}
                    group by {campo}''')
    for x in b:
        tbl.add_rows([x])
    print(tbl)

def zog_report():
    group_custom('Zodiaco',['Zodiaco','Cantidad de vehiculos robados'],'casos_vw')        

def reportes():
    while True:
        cl()
        print(Fore.LIGHTCYAN_EX+'''\n
 /$$$$$$$  /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$$  /$$$$$$ 
| $$__  $$| $$_____/| $$__  $$ /$$__  $$| $$__  $$|__  $$__/| $$_____/ /$$__  $$
| $$  \ $$| $$      | $$  \ $$| $$  \ $$| $$  \ $$   | $$   | $$      | $$  \__/
| $$$$$$$/| $$$$$   | $$$$$$$/| $$  | $$| $$$$$$$/   | $$   | $$$$$   |  $$$$$$ 
| $$__  $$| $$__/   | $$____/ | $$  | $$| $$__  $$   | $$   | $$__/    \____  $$
| $$  \ $$| $$      | $$      | $$  | $$| $$  \ $$   | $$   | $$       /$$  \ $$
| $$  | $$| $$$$$$$$| $$      |  $$$$$$/| $$  | $$   | $$   | $$$$$$$$|  $$$$$$/
|__/  |__/|________/|__/       \______/ |__/  |__/   |__/   |________/ \______/ 
                                                                                
    1- Listado de carros robados. 
    2- Listado de casos por signo zodiacal.
    3- Mapa de robos.
    4- Exportar Caso a HTML.
    5- Listado de casos por provincias.
    6- Listado de robos por marca.
        ''')
        tmp = input('Seleccione una opcion o (x) para volver al menu: ')
        if tmp == '1':
            select_custom('[Marca vehiculo], [Modelo vehiculo], Color, [Provincia del robo], Año', 
            ['Marca vehiculo','Modelo vehiculo','Color','Provincia del robo','Año'])
        elif tmp == '2':
            zog_report()
            input('Enter para continuar.... ')
        elif tmp == '3':
            htmlS.mapa()
        elif tmp == '4':
            htmlS.html()
        elif tmp == '5':
            group_custom('[Provincia del robo]',['Provincia del robo', 'Cantidad de robos'],'casos_vw')
        elif tmp == '6':
            group_custom('[Marca vehiculo]',['Marca vehiculo','Cantidad vehiculos robados'],'casos_vw')
        elif tmp == 'x' or tmp == 'X':
            return False
        else:
            input('Esa opcion no se encontro, de un [enter]')
        input('Presione enter para continuar')
