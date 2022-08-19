import pandas as pd 
import numpy as np 
import ConnectSQL as connect

def Consulta(num):
    
    if num == '1':
        conn = connect.connect()
        df = pd.read_sql(''' select (select count(*) from Tsunami) as Tsunami,(select count(*) from Lugar) as Lugar, (select count(*) from Ubicacion) as Ubicacion, (select count(*) from Tiempo) as Tiempo;''',conn)
        print('\n\n\n\n\n')
        print('********* Reporte 1 ********')
        print(df.to_string())
        print('\n\n\n')


    elif num == '2':
        conn = connect.connect()
        df = pd.read_sql(''' select Anio as year, sum(ID_Tsunami) as No_Tsunamis from Tsunami
inner join Tiempo on Tiempo.ID_tiempo = Tsunami.FK_id_tiempo
group by Anio
order by year; ''',conn)
        print('\n\n\n\n\n')
        print('********* Reporte 2 ********')
        print(df.to_string())
        print('\n\n\n')


    elif num == '3':
        conn = connect.connect()
        df = pd.read_sql(''' select Anio as year, sum(ID_Tsunami) as No_Tsunamis from Tsunami
inner join Tiempo on Tiempo.ID_tiempo = Tsunami.FK_id_tiempo
group by Anio
order by year; ''',conn)
        print('\n\n\n\n\n')
        print('********* Reporte 3 ********')
        print(df.to_string())
        print('\n\n\n')


    elif num == '4':
        conn = connect.connect()
        df = pd.read_sql(''' select Lugar.Pais, avg(Tsunami.Total_damage) as Promedio_Total_Damage from Tsunami
inner join Lugar on Lugar.ID_lugar = Tsunami.FK_id_lugar
group by Lugar.Pais
order by Pais; ''',conn)
        print('\n\n\n\n\n')
        print('********* Reporte 4 ********')
        print(df.to_string())
        print('\n\n\n')


    elif num == '5':
        conn = connect.connect()
        df = pd.read_sql(''' select TOP 5 Lugar.Pais, sum(Tsunami.Total_deaths) as Muertes from Tsunami
inner join Lugar on Lugar.ID_lugar = Tsunami.FK_id_lugar
group by Lugar.Pais
order by Muertes desc; ''',conn)
        print('\n\n\n\n\n')
        print('********* Reporte 5 ********')
        print(df.to_string())
        print('\n\n\n')


    elif num == '6':
        conn = connect.connect()
        df = pd.read_sql(''' select TOP 5 Anio, sum(Tsunami.Total_deaths) as Muertes from Tsunami
inner join Tiempo on Tiempo.ID_tiempo = Tsunami.FK_id_tiempo
group by Anio
order by Muertes desc; ''',conn)
        print('\n\n\n\n\n')
        print('********* Reporte 6 ********')
        print(df.to_string())
        print('\n\n\n')


    elif num == '7':
        conn = connect.connect()
        df = pd.read_sql(''' select TOP 5 Anio, sum(Tsunami.ID_tsunami) as No_Tsunamis from Tsunami
inner join Tiempo on Tiempo.ID_tiempo = Tsunami.FK_id_tiempo
group by Anio
order by No_Tsunamis desc; ''',conn)
        print('\n\n\n\n\n')
        print('********* Reporte 7 ********')
        print(df.to_string())
        print('\n\n\n')

    elif num == '8':
        conn = connect.connect()
        df = pd.read_sql(''' select TOP 5 Pais, sum(Tsunami.Total_houses_destroyed) as Casas_destruidas from Tsunami
inner join Lugar on Lugar.ID_lugar = Tsunami.FK_id_lugar
group by Pais
order by Casas_destruidas desc; ''',conn)
        print('\n\n\n\n\n')
        print('********* Reporte 8 ********')
        print(df.to_string())
        print('\n\n\n')

    elif num == '9':
        conn = connect.connect()
        df = pd.read_sql('select TOP 5 Pais, sum(Tsunami.Total_houses_damaged) as Casas_dañadas from Tsunami inner join Lugar on Lugar.ID_lugar = Tsunami.FK_id_lugar group by Pais order by Casas_dañadas desc;',conn)        
        print('\n\n\n\n\n')
        print('********* Reporte 9 ********')
        print(df.to_string())
        print('\n\n\n')

    else:
        conn = connect.connect()
        df = pd.read_sql('select Pais, avg(Tsunami.Maximum_water_height) as Altura_Maxima_agua from Tsunami inner join Lugar on Lugar.ID_lugar = Tsunami.FK_id_lugar group by Pais order by Altura_Maxima_agua desc;',conn)
        print('\n\n\n\n\n')
        print('********* Reporte 10 ********')
        print(df.to_string())
        print('\n\n\n')
