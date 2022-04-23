import fechas
from datetime import date

def zodiaco_x(zod):
    zod = str(zod)
    dY = zod[0:4];
    dY = int(dY)
    dM = zod[5:7] 
    dM = int(dM) 
    dD = zod[8:10] 
    dD = int(dD) 

    #/////////////////////// Extraccion de dia y uso de funciones
    fecha = date(dY, dM , dD)
    mes = fecha.month
    dia = fecha.day
    zodiaco_x = fechas.zodiaco(mes,dia)
    
    return zodiaco_x