import sqlite3
from myClear import clear as cl
from prettytable import PrettyTable
import funciones
import fechas
import zodiaco
import json
from colorama import Fore, Back, Style, init
init()
conexion = sqlite3.connect('robos.db')
cur = conexion.cursor() #Cursor

def tablas():
    cur.execute('''CREATE TABLE IF NOT EXISTS provincias
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion NVARCHAR (50) ) ''')
    #///////////
    cur.execute('''CREATE TABLE IF NOT EXISTS marcas
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion NVARCHAR (50) )''')
    #///////////
    cur.execute('''CREATE TABLE IF NOT EXISTS modelos
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion NVARCHAR (50) )''')
    #/////////// tabla principal
    cur.execute('''CREATE TABLE IF NOT EXISTS casos (
    Id                   INTEGER PRIMARY KEY AUTOINCREMENT,
    Chasis               NVARCHAR,
    Placa                NVARCHAR (50),
    Marca                INTEGER,
    Modelo               INTEGER,
    Color                NVARCHAR (50),
    Año                  INTEGER,
    Fecha                DATETIME,
    Nombre               NVARCHAR (50),
    Cedula               INTEGER (15),
    Descripcion          NVARCHAR (50),
    Telefono             INTEGER (50),
    Provincia            INTEGER,
    Latitud              NVARCHAR (20),
    Longitud             NVARCHAR (20),
    Estado               NVARCHAR (50),
    Fecha_encuentro      DATETIME,
    Comentario_encuentro NVARCHAR (100),
    Zodiaco              NVARCHAR (50) 
);
    ''')
    conexion.commit()
def join():
    cur.execute('''
create view IF NOT EXISTS casos_vw
AS
SELECT t1.Id,t1.Chasis,t1.Placa,t1.Color,t1.Año,t1.Fecha,
t1.Nombre,t1.Cedula,t1.Descripcion,t1.Telefono,t1.Latitud,t1.Longitud,
t1.Estado,t1.Fecha_encuentro,t1.Comentario_encuentro,
t2.descripcion as [Marca vehiculo],
t3.descripcion as [Modelo vehiculo],  
t4.descripcion as [Provincia del robo],t1.Zodiaco 
FROM casos t1 
inner join marcas t2 on t1.Marca = t2.id
inner join modelos t3 on t1.Modelo = t3.id
inner join provincias t4 on t1.Provincia = t4.id
    ''')
    conexion.commit()
tablas()
join()

#--------------Sentencias globales
def select(tabla, campos):
    TBL = PrettyTable()
    TBL.field_names = campos
    valores = cur.execute(f'''SELECT * FROM {tabla} ''')
    for x in valores:
        TBL.add_rows([x])
    print(TBL)

def comprob_int(num):
    try:
        int(num)
        return True
    except:
        return False    

def main_select():
    tbl = PrettyTable()
    tbl.field_names = ['Id','Chasis','Estado','Fecha encuentro','Nombre','Cedula','Marca','Modelo','Provincida']
    var = cur.execute('''select Id,Chasis,Estado,Fecha_encuentro,Nombre,Cedula,[Marca vehiculo],[Modelo vehiculo],[Provincia del robo] from casos_vw''')
    for x in var:
        tbl.add_rows([x])
    print(tbl)

def actualizar_comprob(campo, idx):
    #-----No perderme
    valor = ''
    quest = '' 
    p = cur.execute(f'Select * from casos WHERE id  = {idx}')
    
    a = cur.execute(f'SELECT {campo} FROM casos WHERE Id = {idx}')
    for x in a:
        #-------------Valor que tiene el campo right now 
        valor = x[0] 
    if campo == 'Estado':
        xl = PrettyTable()
        xl.field_names = ['Id','Estado']
        xl.add_row(['1','Encontrado'])
        print(xl)
        xlmp = input('Seleccione una opcion: ')

        if comprob_int(xlmp):
            xlmp = int(xlmp)
            if xlmp > 1 or xlmp < 0:
                input('Solo puede seleccionar el numero 1... (presione enter para continuar)')
            else:
                quest = 'Encontrado'
        else:
            return False
    #/////////////------FECHA ENCUENTRO
    elif campo == 'Fecha_encuentro':
        print('Digite la fecha del encuentro!!!! :D')
        quest = funciones.fecha()
        if quest == False:
            input('Ponga la fecha del encuentro correctamente.... (presione enter para continuar)')
            return False
        #//////////////////////////------TABLA MARCA
    elif campo == 'Marca':
        select('marcas', ['ID','Marcas de vehiculos']) #----------- Menu
        quest = input(f'''El campo --{campo}-- tiene el valor <<{valor}>> digite el nuevo valor
        o dejelo vacio para no cambiar: ''')
        #//////////////////////////------TABLA MODELO
    elif campo == 'Modelo':
        select('modelos', ['ID','Modelos de vehiculos']) #----------- Menu
        quest = input(f'''El campo --{campo}-- tiene el valor <<{valor}>> digite el nuevo valor
        o dejelo vacio para no cambiar: ''')
        #//////////////////////////------TABLA PROVINCIA
    elif campo == 'Provincia':
        select('provincias', ['ID','Provincias']) #----------- Menu
        quest = input(f'''El campo --{campo}-- tiene el valor <<{valor}>> digite el nuevo valor
        o dejelo vacio para no cambiar: ''')
    else:        
        quest = input(f'''El campo --{campo}-- tiene el valor <<{valor}>> digite el nuevo valor
        o dejelo vacio para no cambiar: ''')
    #/////////////
    if '' == quest:
        quest = valor
    cur.execute(f'''update casos SET {campo} = "{quest}"
                    WHERE Id = {idx} ''')
    conexion.commit()

def error():
    input('''Digite correctamente el Id
            (Presione enter para continuar...)
            ''')
def bien():
    input('''Operacion efectuada :D
            (Presione enter para continuar...)''')

#------------Sentencias del programa

def insert():
    cl()
    try:
            
        print(Fore.LIGHTYELLOW_EX+'''
    ______  __    __   ______   ________  _______   ________  ______   _______  
    /      |/  \  /  | /      \ /        |/       \ /        |/      \ /       \ 
    $$$$$$/ $$  \ $$ |/$$$$$$  |$$$$$$$$/ $$$$$$$  |$$$$$$$$//$$$$$$  |$$$$$$$  |
    $$ |  $$$  \$$ |$$ \__$$/ $$ |__    $$ |__$$ |   $$ |  $$ |__$$ |$$ |__$$ |
    $$ |  $$$$  $$ |$$      \ $$    |   $$    $$<    $$ |  $$    $$ |$$    $$< 
    $$ |  $$ $$ $$ | $$$$$$  |$$$$$/    $$$$$$$  |   $$ |  $$$$$$$$ |$$$$$$$  |
    _$$ |_ $$ |$$$$ |/  \__$$ |$$ |_____ $$ |  $$ |   $$ |  $$ |  $$ |$$ |  $$ |
    / $$   |$$ | $$$ |$$    $$/ $$       |$$ |  $$ |   $$ |  $$ |  $$ |$$ |  $$ |
    $$$$$$/ $$/   $$/  $$$$$$/  $$$$$$$$/ $$/   $$/    $$/   $$/   $$/ $$/   $$/ 
    ''')
        Chasis = input('Digite el chasis del vehiculo >>>> ') #comprobar
        Placa =  input('Digite la placa del vehiculo >>>> ')
        select('marcas', ['ID','Marcas de vehiculos']) #----------- Menu
        Marca =  input('Digite la marca del vehiculo >>>> ')
        select('modelos', ['ID','Modelos de vehiculos'])  #-------- Menu
        Modelo =  input('Digite el modelo del vehiculo >>>> ') #comprobar
        if comprob_int(Marca) and comprob_int(Modelo):
            Color = input('Digite el color del vehiculo >>>> ')
            Año = input('Digite el año del vehiculo >>>> ') #comprobar
            if comprob_int(Año) == False:
                print('\nMinimo escribe el año en numeros...')
            else:
                Fecha = False
                while Fecha == False:
                    print('\n')
                    print('Ahora digitaremos la fecha del (ROBO) del vehiculo\n')
                    quest = input('Puede digitar (x) si quiere volver a atras o cualquier cosa para continuar >>>> ')
                    if 'x' in quest or 'X' in quest:
                        return False
                    else:
                        Fecha = funciones.fecha()
                        if Fecha == False:
                            input('''Escriba correctamente la fecha
                            (Presione enter para continuar)''')
                            print('\n')
            
                Nombre = input('Digite el nombre del denunciante >>>> ')
                Cedula = input('Digite la cedula del denunciante >>>> ') #comprobar
                if comprob_int(Cedula):
                    Descripcion = input('Digite la descripcion del vehiculo: ')
                    Telefono = input('Digite el telefono del denunciante: ') #comprobar
                    select('provincias', ['ID','Provincias']) #------------ Menu
                    Provincia = input('Digite la provincia donde sucedio: ') #comprobar
                    if comprob_int(Telefono) and comprob_int(Provincia):
                        Latitud = input('Digite la latitud donde sucedio: ')
                        Longitud = input('Digite la longitud donde sucedio: ')
                        Estado = 'Robado'
                        Fecha_encuentro = 'NULL'
                        Comentario_encuentro = 'NULL'
                        #-------------------------
                        # print(Fecha)
                        zodiac = zodiaco.zodiaco_x(Fecha)
                        #----------------------
                        cur.execute(f'''INSERT INTO casos (Chasis, Placa, Marca, Modelo, Color, Año, Fecha, Nombre,
                        Cedula, Descripcion, Telefono, Provincia, Latitud, Longitud, Estado, Fecha_encuentro, 
                        Comentario_encuentro, Zodiaco)
                        values (
                            "{Chasis}","{Placa}",{int(Marca)},{int(Modelo)},"{Color}",{int(Año)},"{Fecha}","{Nombre}"
                            ,{int(Cedula)},"{Descripcion}",{int(Telefono)},{int(Provincia)},"{Latitud}",
                            "{Longitud}","{Estado}","{Fecha_encuentro}","{Comentario_encuentro}","{zodiac}"
                            )
                        ''')
                        bien()
                        conexion.commit()
                        #--------------- Zodiaco
                    else:
                        print('''Escriba el telefono en numeros y 
                                seleccione la provincia correctamente''')
                        input()
                else:
                    print('Escriba la cedula correctamente.')
                    input()
        else:
            print('La marca y el modelo no fueron seleccionadas correctamente.')
        input('\nDigite enter para continuar...') 
    except Exception as inst:
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)
        input()          # __str__ al
#-----------Encontrado
def encontrado():
    while True:
        cl()
        print(Fore.LIGHTYELLOW_EX+'''
      __      __  _     _            _         ______                       _                 _       
      \ \    / / | |   (_)          | |       |  ____|                     | |               | |      
      \ \  / ___| |__  _  ___ _   _| | ___   | |__   _ __   ___ ___  _ __ | |_ _ __ __ _  __| | ___  
      \ \/ / _ | '_ \| |/ __| | | | |/ _ \  |  __| | '_ \ / __/ _ \| '_ \| __| '__/ _` |/ _` |/ _ \ 
        \  |  __| | | | | (__| |_| | | (_) | | |____| | | | (_| (_) | | | | |_| | | (_| | (_| | (_) |
        \/ \___|_| |_|_|\___|\__,_|_|\___/  |______|_| |_|\___\___/|_| |_|\__|_|  \__,_|\__,_|\___/  ''')
        main_select()
        tmp = input('''Digite el Id del caso del vehiculo encontrado: 
            o (x) para volver al menu principal ''')
        if comprob_int(tmp):
            tmp = int(tmp)
            if confirm_select(tmp) == False:
                error()
            else:
                if actualizar_comprob('Fecha_encuentro', tmp) == False:
                    input('Digite la fecha correctamente... (presione enter para continuar)')
                else:
                    actualizar_comprob('Estado', tmp)
                    actualizar_comprob('Comentario_encuentro ', tmp)
                    bien()
        elif tmp == 'x' or tmp == 'X':
            return False
        else:
            error()


def confirm_select(id_x):
    LISTA_SELECT = []
    confirm_select = False
    for x in cur.execute(f'Select id from casos where id = {id_x}'):
            LISTA_SELECT.append(x)
    print(LISTA_SELECT)
    for y in LISTA_SELECT: # Comprobacion si existe
        print(y)
        if id_x in y:
            confirm_select = True
        else:
            confirm_select = False

    return confirm_select
#-------------------------------- ACTUALIZAR -------------------------

def update():
    #------------Inicio
    main_select()
    id_x = input('''Digita el numero de Id del caso a actualizar: 
                           o digite (x) para volver a atras ''')
    if comprob_int(id_x):
        id_x = int(id_x)
        if confirm_select(id_x):
            actualizar_comprob('Placa',id_x)
            actualizar_comprob('Marca',id_x)
            actualizar_comprob('Modelo',id_x)
            actualizar_comprob('Provincia',id_x)
            actualizar_comprob('Color',id_x)
            actualizar_comprob('Año',id_x)
            actualizar_comprob('Nombre',id_x)
            actualizar_comprob('Cedula',id_x)
            actualizar_comprob('Descripcion',id_x)
            actualizar_comprob('Telefono',id_x)
            actualizar_comprob('Latitud',id_x)
            actualizar_comprob('Longitud',id_x)
            bien()
        else:
            error()

    elif id_x == 'x' or id_x =='X':
        return False
    else:
        error()
    
def delete():
    main_select()
    tmp = input('''Digite el numero de id del caso a eliminar: ''')
    if comprob_int(tmp):
        
        cur.execute(f'DELETE FROM casos WHERE Id = {tmp}')
        conexion.commit()
        bien()
        
    else:
        print('Por favor digite un numero')
        input()


#config


def gest_one(tabla, valor):
    while True:

        cl()
        if tabla == 'provincias':
            print('''
    $$$$$$$\  $$$$$$$\   $$$$$$\  $$\    $$\ $$$$$$\ $$\   $$\  $$$$$$\  $$$$$$\  $$$$$$\   $$$$$$\  
    $$  __$$\ $$  __$$\ $$  __$$\ $$ |   $$ |\_$$  _|$$$\  $$ |$$  __$$\ \_$$  _|$$  __$$\ $$  __$$\ 
    $$ |  $$ |$$ |  $$ |$$ /  $$ |$$ |   $$ |  $$ |  $$$$\ $$ |$$ /  \__|  $$ |  $$ /  $$ |$$ /  \__|
    $$$$$$$  |$$$$$$$  |$$ |  $$ |\$$\  $$  |  $$ |  $$ $$\$$ |$$ |        $$ |  $$$$$$$$ |\$$$$$$\  
    $$  ____/ $$  __$$< $$ |  $$ | \$$\$$  /   $$ |  $$ \$$$$ |$$ |        $$ |  $$  __$$ | \____$$\ 
    $$ |      $$ |  $$ |$$ |  $$ |  \$$$  /    $$ |  $$ |\$$$ |$$ |  $$\   $$ |  $$ |  $$ |$$\   $$ |
    $$ |      $$ |  $$ | $$$$$$  |   \$  /   $$$$$$\ $$ | \$$ |\$$$$$$  |$$$$$$\ $$ |  $$ |\$$$$$$  |
    \__|      \__|  \__| \______/     \_/    \______|\__|  \__| \______/ \______|\__|  \__| \______/  ''')
        elif tabla == 'marcas':
            print('''
    $$\      $$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
    $$$\    $$$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
    $$$$\  $$$$ |$$ /  $$ |$$ |  $$ |$$ /  \__|$$ /  $$ |$$ /  \__|
    $$\$$\$$ $$ |$$$$$$$$ |$$$$$$$  |$$ |      $$$$$$$$ |\$$$$$$\  
    $$ \$$$  $$ |$$  __$$ |$$  __$$< $$ |      $$  __$$ | \____$$\ 
    $$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |  $$ |$$\   $$ |
    $$ | \_/ $$ |$$ |  $$ |$$ |  $$ |\$$$$$$  |$$ |  $$ |\$$$$$$  |
    \__|     \__|\__|  \__|\__|  \__| \______/ \__|  \__| \______/  ''')
        elif tabla == 'modelos':
            print('''
    $$\      $$\  $$$$$$\  $$$$$$$\  $$$$$$$$\ $$\       $$$$$$\   $$$$$$\  
    $$$\    $$$ |$$  __$$\ $$  __$$\ $$  _____|$$ |     $$  __$$\ $$  __$$\ 
    $$$$\  $$$$ |$$ /  $$ |$$ |  $$ |$$ |      $$ |     $$ /  $$ |$$ /  \__|
    $$\$$\$$ $$ |$$ |  $$ |$$ |  $$ |$$$$$\    $$ |     $$ |  $$ |\$$$$$$\  
    $$ \$$$  $$ |$$ |  $$ |$$ |  $$ |$$  __|   $$ |     $$ |  $$ | \____$$\ 
    $$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |     $$ |  $$ |$$\   $$ |
    $$ | \_/ $$ | $$$$$$  |$$$$$$$  |$$$$$$$$\ $$$$$$$$\ $$$$$$  |\$$$$$$  |
    \__|     \__| \______/ \_______/ \________|\________|\______/  \______/ ''')
        print('''
                1 - Agregar
                2 - Editar
                3 - Eliminar\n''')
    #------------------------------------------            
        tmp = input('Seleccione una opcion del menu o (x) para volver al menu: ')
        if tmp == '1':
            valorX = input(f'Digita {valor} o (x) para volver a atras: ')
            if valorX == '' or valorX =='x' or valorX == 'X':
                return False
            else:
                cur.execute(f'''INSERT INTO {tabla} (descripcion) VALUES ("{valorX}") ''')
                conexion.commit()
                print('Operacion Completada :D')

        elif tmp == '2':
            select(tabla, ['ID', 'DESCRIPCION'])
            idX = input('Seleccione el id que quiere editar o (x) para volver a atras: ')
            if comprob_int(idX) == False:
                error()
            else:
                idX = int(idX)
                if confirm_select(idX) == False:
                    error()
                else:
                    if idX == 'x' or idX == 'X':
                        return False
                    else:        
                        #///////////// Consulta
                        newX = input('Digite el nuevo valor: ')
                        cur.execute(f'''UPDATE {tabla} 
                                        SET (descripcion) = "{newX}"
                                        WHERE  id = {idX} ''')
                        conexion.commit()
                        print('Operacion Completada :D')

        elif tmp == '3':
            select(tabla, ['ID', 'DESCRIPCION'])
            idX = input('Seleccione el id que quiere editar o (x) para volver a atras: ')
            if comprob_int(idX) == False:
                error()
            else:
                idX = int(idX)
                if confirm_select(idX) == False:
                    error()
                else:
                    if idX == 'x' or idX == 'X':
                        return False
                    else:        
                        #///////////// Consulta
                        cur.execute(f'''DELETE  
                                        FROM {tabla}
                                        WHERE  id = {idX} ''')
                        conexion.commit()
                        print('Operacion Completada :D')
            #---------------
        if 'x' in tmp or 'X' in tmp:
            return False

def config():
    x = 0
    while True:
        if x <= 0:
            cl()
        else:
            input('Presiona enter para continuar')
            cl()
        print(Fore.GREEN+'''
$$$$$$\  $$$$$$$$\  $$$$$$\ $$$$$$$$\ $$$$$$\  $$$$$$\  $$\   $$\ 
$$  __$$\ $$  _____|$$  __$$\\__$$  __|\_$$  _|$$  __$$\ $$$\  $$ |
$$ /  \__|$$ |      $$ /  \__|  $$ |     $$ |  $$ /  $$ |$$$$\ $$ |
$$ |$$$$\ $$$$$\    \$$$$$$\    $$ |     $$ |  $$ |  $$ |$$ $$\$$ |
$$ |\_$$ |$$  __|    \____$$\   $$ |     $$ |  $$ |  $$ |$$ \$$$$ |
$$ |  $$ |$$ |      $$\   $$ |  $$ |     $$ |  $$ |  $$ |$$ |\$$$ |
\$$$$$$  |$$$$$$$$\ \$$$$$$  |  $$ |   $$$$$$\  $$$$$$  |$$ | \$$ |
 \______/ \________| \______/   \__|   \______| \______/ \__|  \__|                   
            1 - Gestionar provincias
            2 - Gestionar marcas de autos
            3 - Gestionar modelos de autos
        ''')
        tmp = input('\nSeleccione una opcion o digite (x) para volver al menu: ')
        if tmp == '1':
            gest_one('provincias', 'una provincia')
        elif tmp == '2':
            gest_one('marcas', 'una marca')
        elif tmp == '3':
            gest_one('modelos', 'un modelo')
        elif 'x' in tmp or 'X' in tmp:
            return False
        else:
            input('''Esa opcion no se encontro...
                    (Presiona enter para continuar)
            ''')
        x += 1