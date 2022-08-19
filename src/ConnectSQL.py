import pyodbc
from decouple import config

def connect():
    try:
        conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server='+config('SERVER_SQL')+';'
            'Database='+config('DATABASE')+';'
            'UID='+config('USER')+';'
            'Trusted_Connection=yes;'
        )
        print('Conexion exitosa')
        return conn
    except Exception as e:
        print('Ocurrio un error al conectar con sql server: ',e)       