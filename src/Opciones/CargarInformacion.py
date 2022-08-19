import pandas as pd 
import numpy as np 
import ConnectSQL as connect




def Cargar(df):
    print('Se obtubo un dataframe:')
    print(df)
    #conexion a la base de datos
    #print('Prueba de conexion a la base de datos')
         
    conn = connect.connect()
    for row in df.itertuples():
        #print('Consulta:\n\n')
        #print('''INSERT INTO Practica1Semi2.dbo.Temporal(Anio,Mes,Dia,Hora,Minuto,Segundo,Tsunami_event_validity, Tsunami_cause_code,Earthquake_Magnitude, Deposits, Latitude, Longitude, Maximun_water_height,Number_of_runups, Tsunami_magnitude, Tsunami_intensity, Total_deaths, Total_missing, Total_missing_description, Total_injuries, Total_damage, Total_damage_description, Total_houses_destroyed, Total_houses_damaged, Country, Location_name) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',row.Year,row.Mo,row.Dy,row.Hr,row.Mn,row.Sec,row.Tsunami_Event_Validity,row.Tsunami_Cause_Code,row.Earthquake_Magnitude,row.Deposits,row.Latitude, row.Longitude,row.Maximum_Water_Height, row.Number_of_Runups, row.Tsunami_Magnitude, row.Tsunami_Intensity, row.Total_Deaths, row.Total_Missing, row.Total_Missing_Description, row.Total_Injuries, row.Total_Damage, row.Total_Damage_Description, row.Total_Houses_Destroyed, row.Total_Houses_Damaged, row.Country, row.Location_Name)
        conn.cursor().execute('''INSERT INTO Practica1Semi2.dbo.Temporal(Anio,Mes,Dia,Hora,Minuto,Segundo,Tsunami_event_validity, Tsunami_cause_code,Earthquake_Magnitude, Deposits, Latitude, Longitude, Maximun_water_height,Number_of_runups, Tsunami_magnitude, Tsunami_intensity, Total_deaths, Total_missing, Total_missing_description, Total_injuries, Total_damage, Total_damage_description, Total_houses_destroyed, Total_houses_damaged, Country, Location_name) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',row.Year,row.Mo,row.Dy,row.Hr,row.Mn,row.Sec,row.Tsunami_Event_Validity,row.Tsunami_Cause_Code,row.Earthquake_Magnitude,row.Deposits,row.Latitude, row.Longitude,row.Maximum_Water_Height, row.Number_of_Runups, row.Tsunami_Magnitude, row.Tsunami_Intensity, row.Total_Deaths, row.Total_Missing, row.Total_Missing_Description, row.Total_Injuries, row.Total_Damage, row.Total_Damage_Description, row.Total_Houses_Destroyed, row.Total_Houses_Damaged, row.Country, row.Location_Name)
        #cursor.execute('''INSERT INTO Practica1Semi2.dbo.prueba (nombre,numero) values(?,?)''',row.Year,row.Mo)
    
    conn.cursor().execute(''' insert into dbo.Tiempo(Anio,Mes,Dia,Hora,Minutos, Segundo)
select distinct Temporal.Anio, Temporal.Mes, Temporal.Dia, Temporal.Hora, Temporal.Minuto, Temporal.Segundo from Temporal; ''')    

    conn.cursor().execute(''' insert into dbo.Ubicacion(Latitud,Longitud)
select distinct Temporal.Latitude, Temporal.Longitude from Temporal where Latitude is not null and Longitude is not null; ''')

    conn.cursor().execute(''' insert into Lugar (Pais,Ciudad)
select distinct Temporal.Country, Temporal.Location_name from Temporal where Country is not null and Location_name is not null; ''')

    conn.cursor().execute(''' Insert into Tsunami(FK_id_lugar ,FK_id_tiempo ,FK_id_ubicacion ,Tsunami_event_validity ,Tsunami_cause_code ,Earthquake_magnitude ,Deposits ,Maximum_water_height ,Number_of_runups,Tsunami_magnitude ,Tsunami_intensity ,Total_deaths ,Total_missing ,Total_missing_description ,Total_injuries ,Total_damage ,Total_damage_description ,Total_houses_destroyed ,Total_houses_damaged )
	               select distinct ID_lugar, ID_tiempo, ID_ubicacion, Tsunami_event_validity,Tsunami_cause_code, Earthquake_magnitude,Deposits, Maximun_water_height, Number_of_runups,Tsunami_magnitude, Tsunami_intensity, Total_deaths, Total_missing, Total_missing_description, Total_injuries, Total_damage, Total_damage_description, Total_houses_destroyed, Total_houses_damaged from Temporal
	inner join Lugar on Lugar.Pais = Temporal.Country and Lugar.Ciudad = Temporal.Location_name
	inner join Tiempo on Tiempo.Anio = Temporal.Anio and Tiempo.Mes = Temporal.Mes and Tiempo.Dia = Temporal.Dia and Tiempo.Hora = Temporal.Hora and Tiempo.Minutos = Temporal.Minuto and Tiempo.Segundo = Temporal.Segundo
	inner join Ubicacion on Ubicacion.Latitud = Temporal.Latitude and Ubicacion.Longitud = Temporal.Longitude; ''')

    conn.commit()    
    conn.close()
    
