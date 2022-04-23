import funciones
import sentencias
from myClear import clear as cl
import webbrowser
from colorama import Fore, Back, Style, init
init()
cl()
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')
while True:
    print(Fore.RED +'''
        /$$$$$$            /$$$$$$          /$$ /$$ /$$
        |_  $$_/           /$$__  $$        | $$| $$| $$
        | $$   /$$$$$$$ | $$  \__//$$$$$$ | $$| $$| $$
        | $$  | $$__  $$| $$$$   /$$__  $$| $$| $$| $$
        | $$  | $$  \ $$| $$_/  | $$  \ $$|__/|__/|__/
        | $$  | $$  | $$| $$    | $$  | $$            
        /$$$$$$| $$  | $$| $$    |  $$$$$$/ /$$ /$$ /$$
        |______/|__/  |__/|__/     \______/ |__/|__/|__/ 


        Programa creado by: Maycol Daniel Perez Ciprian
        Curso de Introduccion a la programacion
        Prof. Amadis Suarez
''')
    input('Presione enter para continuar... ')
    break
while True:
    cl()
    print(Fore.WHITE+'''
         /$$      /$$           /$$          
        | $$$    /$$$          |__/          
        | $$$$  /$$$$  /$$$$$$  /$$ /$$$$$$$ 
        | $$ $$/$$ $$ |____  $$| $$| $$__  $$
        | $$  $$$| $$  /$$$$$$$| $$| $$  \ $$
        | $$\  $ | $$ /$$__  $$| $$| $$  | $$
        | $$ \/  | $$|  $$$$$$$| $$| $$  | $$
        |__/     |__/ \_______/|__/|__/  |__/
                                     
    1 - Gestionar Casos. 
    2 - Registrar Vehículo encontrado
    3 - Reportes
    4 - Configuración
    5 - Acerca De
    6 - Salir
    ''')
    tmp = input('Seleccione una opcion >>>>>> ')
    if tmp == '1':
        funciones.gestion()
    elif tmp == '2':
        sentencias.encontrado()
    elif tmp == '3':
        funciones.reportes()
    elif tmp == '4':
        sentencias.config()
    elif tmp == '5':
        print('''
  /$$$$$$  /$$                 /$$                           /$$                     
 /$$__  $$| $$                |__/                          | $$                     
| $$  \ $$| $$$$$$$   /$$$$$$  /$$  /$$$$$$  /$$$$$$$   /$$$$$$$  /$$$$$$            
| $$$$$$$$| $$__  $$ /$$__  $$| $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$           
| $$__  $$| $$  \ $$| $$  \__/| $$| $$$$$$$$| $$  \ $$| $$  | $$| $$  \ $$           
| $$  | $$| $$  | $$| $$      | $$| $$_____/| $$  | $$| $$  | $$| $$  | $$           
| $$  | $$| $$$$$$$/| $$      | $$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$//$$ /$$ /$$
|__/  |__/|_______/ |__/      |__/ \_______/|__/  |__/ \_______/ \______/|__/|__/|__/ ''')
        webbrowser.open('https://youtu.be/VaI_Ky5Uh_c')
    elif tmp == '6':
        cl()
        print('''
 /$$$$$$        /$$ /$$                           /$$  /$$  /$$   
 /$$__  $$      | $$|__/                          |  $$|  $$|  $$  
| $$  \ $$  /$$$$$$$ /$$  /$$$$$$   /$$$$$$$       \  $$\  $$\  $$ 
| $$$$$$$$ /$$__  $$| $$ /$$__  $$ /$$_____/        \  $$\  $$\  $$
| $$__  $$| $$  | $$| $$| $$  \ $$|  $$$$$$          /$$/ /$$/ /$$/
| $$  | $$| $$  | $$| $$| $$  | $$ \____  $$        /$$/ /$$/ /$$/ 
| $$  | $$|  $$$$$$$| $$|  $$$$$$/ /$$$$$$$/       /$$/ /$$/ /$$/  
|__/  |__/ \_______/|__/ \______/ |_______/       |__/ |__/ |__/   

''')
        input('Enter para salir. ')
        break
    else:
        input('''Por favor seleccione correctamente
                (Presione enter para continuar)
                ''')