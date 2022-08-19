CREATE DATABASE Practica1Semi2;

use Practica1Semi2;

create Table Temporal(
	Anio VARCHAR(100) NULL,
    Mes VARCHAR(100) NULL,
    Dia VARCHAR(100) NULL,
    Hora VARCHAR(100) NULL,
    Minuto VARCHAR(100) NULL,
    Segundo VARCHAR(100) NULL,
    Tsunami_event_validity VARCHAR(100) NULL,
    Tsunami_cause_code VARCHAR(100) NULL,
    Earthquake_magnitude VARCHAR(100) NULL,
    Deposits VARCHAR(100) NULL,
    Latitude VARCHAR(100) NULL,
    Longitude VARCHAR(100) NULL,
    Maximun_water_height VARCHAR(100) NULL,
    Number_of_runups VARCHAR(100) NULL,
    Tsunami_magnitude VARCHAR(100) NULL,
    Tsunami_intensity VARCHAR(100) NULL,
    Total_deaths VARCHAR(100) NULL,
    Total_missing VARCHAR(100) NULL,
    Total_missing_description VARCHAR(100) NULL,
    Total_injuries VARCHAR(100) NULL,
    Total_damage VARCHAR(100) NULL,
    Total_damage_description VARCHAR(100) NULL,
    Total_houses_destroyed VARCHAR(100) NULL,
    Total_houses_damaged VARCHAR(100) NULL,
    Country VARCHAR(100) NULL,
    Location_name VARCHAR(100) NULL
)

delete from Temporal;
select * from Temporal;
DROP TABLE IF EXISTS Temporal;





select * from Tiempo;
Create Table Tiempo(
	ID_tiempo int Not null identity(1,1) primary key,
	Anio int NULL,
	Mes int NULL,
	Dia int Null,
	Hora float Null,
	Minutos float NULL,
	Segundo float NULL
)

insert into dbo.Tiempo(Anio,Mes,Dia,Hora,Minutos, Segundo)
select distinct Temporal.Anio, Temporal.Mes, Temporal.Dia, Temporal.Hora, Temporal.Minuto, Temporal.Segundo from Temporal;

DROP TABLE IF EXISTS Tiempo;



Create Table Ubicacion(
	ID_ubicacion int Not null identity(1,1) primary key,
	Latitud float NULL,
	Longitud float NULL
)

insert into dbo.Ubicacion(Latitud,Longitud)
select distinct Temporal.Latitude, Temporal.Longitude from Temporal where Latitude is not null and Longitude is not null;

select * from dbo.Ubicacion;


DROP TABLE IF EXISTS Ubicacion;




Create Table Lugar(
	ID_lugar int Not null identity(1,1) primary key,
	Pais varchar(100) NULL,
	Ciudad varchar (100) NULL,
)

insert into Lugar (Pais,Ciudad)
select distinct Temporal.Country, Temporal.Location_name from Temporal where Country is not null and Location_name is not null;

select * from Lugar;


DROP TABLE IF EXISTS Lugar;


create table Tsunami(
	ID_Tsunami int Not null identity(1,1) primary key,
	FK_id_lugar int not null,
	FK_id_tiempo int not null,
	FK_id_ubicacion int not null,
	Tsunami_event_validity float,
	Tsunami_cause_code float,
	Earthquake_magnitude float,
	Deposits float,
	Maximum_water_height float,
	Number_of_runups float,
	Tsunami_magnitude float,
	Tsunami_intensity float,
	Total_deaths float,
	Total_missing float,
	Total_missing_description float,
	Total_injuries float,
	Total_damage float,
	Total_damage_description float,
	Total_houses_destroyed float,
	Total_houses_damaged float,
	constraint FK_tsunami_lugar FOREIGN KEY (FK_id_lugar) REFERENCES Lugar(ID_lugar),
	constraint FK_tsunami_tiempo FOREIGN KEY (FK_id_tiempo) REFERENCES Tiempo(ID_tiempo),
	constraint FK_tsunami_ubicacion FOREIGN KEY (FK_id_ubicacion) REFERENCES Ubicacion(ID_ubicacion)
	)

	DROP TABLE IF EXISTS Tsunami;


	select * from Tsunami;
	Insert into Tsunami(FK_id_lugar ,FK_id_tiempo ,FK_id_ubicacion ,Tsunami_event_validity ,Tsunami_cause_code ,Earthquake_magnitude ,Deposits ,Maximum_water_height ,Number_of_runups,Tsunami_magnitude ,Tsunami_intensity ,Total_deaths ,Total_missing ,Total_missing_description ,Total_injuries ,Total_damage ,Total_damage_description ,Total_houses_destroyed ,Total_houses_damaged )
	               select distinct ID_lugar, ID_tiempo, ID_ubicacion, Tsunami_event_validity,Tsunami_cause_code, Earthquake_magnitude,Deposits, Maximun_water_height, Number_of_runups,Tsunami_magnitude, Tsunami_intensity, Total_deaths, Total_missing, Total_missing_description, Total_injuries, Total_damage, Total_damage_description, Total_houses_destroyed, Total_houses_damaged from Temporal
	inner join Lugar on Lugar.Pais = Temporal.Country and Lugar.Ciudad = Temporal.Location_name
	inner join Tiempo on Tiempo.Anio = Temporal.Anio and Tiempo.Mes = Temporal.Mes and Tiempo.Dia = Temporal.Dia and Tiempo.Hora = Temporal.Hora and Tiempo.Minutos = Temporal.Minuto and Tiempo.Segundo = Temporal.Segundo
	inner join Ubicacion on Ubicacion.Latitud = Temporal.Latitude and Ubicacion.Longitud = Temporal.Longitude;


use Practica1Semi2;

/*
Reporte 1
*/
select (select count(*) from Tsunami) as Tsunami,(select count(*) from Lugar) as Lugar, (select count(*) from Ubicacion) as Ubicacion, (select count(*) from Tiempo) as Tiempo;

/*
Reporte 2
*/
select Anio as year, sum(ID_Tsunami) as No_Tsunamis from Tsunami
inner join Tiempo on Tiempo.ID_tiempo = Tsunami.FK_id_tiempo
group by Anio
order by year;

/*
Reporte 3
*/
select Anio as year, sum(ID_Tsunami) as No_Tsunamis from Tsunami
inner join Tiempo on Tiempo.ID_tiempo = Tsunami.FK_id_tiempo
group by Anio
order by year;


