import ConnectSQL as connect

def Crear():
    conn = connect.connect()
    conn.cursor().execute('''create Table Temporal(
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
)''')
    conn.cursor().execute('''Create Table Tiempo(
	ID_tiempo int Not null identity(1,1) primary key,
	Anio int NULL,
	Mes int NULL,
	Dia int Null,
	Hora float Null,
	Minutos float NULL,
	Segundo float NULL
)''')
    conn.cursor().execute('''Create Table Ubicacion(
	ID_ubicacion int Not null identity(1,1) primary key,
	Latitud float NULL,
	Longitud float NULL
)''')
    conn.cursor().execute('''Create Table Lugar(
	ID_lugar int Not null identity(1,1) primary key,
	Pais varchar(100) NULL,
	Ciudad varchar (100) NULL,
)''')

    conn.cursor().execute('''create table Tsunami(
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
	)''')

    conn.commit()
    print('Modelo creado con exito')
    