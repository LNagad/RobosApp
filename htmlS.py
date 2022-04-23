import folium, webbrowser
from sentencias import *
from os import system
from myClear import clear as cl
from peewee import *
def mapa():
    m = folium.Map(location=[18.65657, -70.6934349], zoom_start = 9)
    select_x = cur.execute('SELECT * FROM casos_vw')

    for x in select_x:
        folium.Marker(
            location=[x[10], x[11]],
            popup=f'''
            <div 
            style="width: 400px; display: flex; justify-content: space-between; 
            flex-wrap: wrap; border-bottom: 10px solid #000">
            <h3 style="width: 48%;">Chasis: <span style="font-size: 16px; font-weight: bold; color: red;">{x[1]}     </span></h3> 
            <h3 style="width: 48%;">Placa:  <span style="font-size: 16px; font-weight: bold; color: red;">{x[2]}     </span></h3>
            <h3 style="width: 48%;">Fecha:  <span style="font-size: 16px; font-weight: bold; color: red;">{x[5]}     </span></h3>
            <h3 style="width: 48%;">Marca:  <span style="font-size: 16px; font-weight: bold; color: red;">{x[15]}    </span></h3>
            <h3 style="width: 48%;">Modelo: <span style="font-size: 16px; font-weight: bold; color: red;">{x[16]}    </span></h3>
            <h3 style="width: 48%;">Provincia: <span style="font-size: 16px; font-weight: bold; color: red;">{x[17]}    </span></h3>
            <h3 style="width: 48%;">Nombre: <span style="font-size: 16px; font-weight: bold; color: red;">{x[6]}     </span></h3>
            <h3 style="width: 48%;">Cedula: <span style="font-size: 16px; font-weight: bold; color: red;">{x[7]}     </span></h3>
            <h3 style="width: 48%;">Zodiaco del caso:  <span style="font-size: 16px; font-weight: bold; color: red;">{x[18]}     </span></h3>
            <h3 style="width: 98%;">Descripcion: <span style="font-size: 16px; font-weight: bold; color: red;">{x[8]}</span></h3>
            </div>''',
            icon=folium.Icon(color="red", icon="info-sign"),
        ).add_to(m)

    m.save('mapa.html')
    webbrowser.open('mapa.html')


def html():
    while True:
            
        cl()
        main_select()
        idx = input('Seleccione un Id del caso para exportar el caso o (x) para volver al menu: ')
        if idx == 'x' or idx == 'X':
            return False
        elif comprob_int(idx):
            idx = int(idx)
            select_x = cur.execute(f'SELECT * FROM casos_vw WHERE Id = {idx}')
            try:
                    
                for x in select_x:
                    if len(x) > 0:
                        chasis = x[1]
                        placa = x[2]
                        color = x[3]
                        año = x[4]
                        fecha = x[5]
                        nombre = x[6]
                        cedula = x[7]
                        descripcion = x[8]
                        telefono = x[9]
                        estado = x[12]
                        fecha_encuentro = x[13]
                        comentario_encuentro = x[14]
                        modelo = x[15]
                        marca = x[16]
                        provincia = x[17]
                        zodiaco = x[18]
                        html = f'''
                            <!DOCTYPE html>
                <html lang="en">
                <head>
                    <link rel="stylesheet" href="styles/styles.css">
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Solicitud de reporte</title>
                </head>
                <body>
                    
                    <header>
                        <div class="logo">
                            <img src="https://www.policianacional.gob.do/wp-content/uploads/2017/02/Logo-de-la-PN-01.png" alt="">
                        </div>
                        <div class="parrafos">
                            <h2>POLICIA NACIONAL</h2>
                            <h2><b>DIRECCION DE INVESTIGACIONES CRIMINALES DE REPUBLICA DOMINICANA.</b></h2>
                            <h2> POR LA PATRIA</h2>
                            <h2 style="text-decoration: underline; font-weight: bold;">AÑO DE LA CONSOLIDACION DE LA SEGURIDAD ALIMENTARIA.</h2>
                        </div>
                    </header>
                    <main>
                        <section class="descripcion">
                            <h2>Acta de denuncia</h2>
                            <p>
                                En la fecha de {fecha} la victima {nombre} con nro. identidad {cedula} Fue victima de un ROBO de un vehiculo, modelo {modelo} de la marca {marca}, chasis {chasis}, sucedio en la provincia de {provincia}, descripcion...{descripcion}
                            </p>
                        </section>
                        <section class="denunciante">
                        <div>
                                <p>Nombre denunciante: {nombre}</p>
                                <p>Zodiaco del caso: {zodiaco}</p>
                                <h2>Denunciante, tel: {telefono} </h2>
                                <h2>Vehiculo, placa: {placa} </h2>
                        </div>
                        </section>
                    </main>
                    <script>
                    //     javascript:window.print()
                    // </script>
                </body>
                </html>
                    '''
                        archivo = open('index.html', 'w', encoding='utf-8')
                        archivo.write(html)
                        archivo.close()
                        webbrowser.open('index.html')
                        input('Bien')
                    else:
                        input('Esa opcion no se encontro... (digite enter para continuar)')
            except:
                input('Esa opcion no se encontro... (digite enter para continuar)')