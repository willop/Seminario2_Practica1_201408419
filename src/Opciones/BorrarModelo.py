import ConnectSQL as connect

def Borrar():
    conn = connect.connect()
    conn.cursor().execute('''DROP TABLE IF EXISTS Temporal;''')
    conn.cursor().execute('''DROP TABLE IF EXISTS Tsunami;''')
    conn.cursor().execute('''DROP TABLE IF EXISTS Lugar;''')
    conn.cursor().execute('''DROP TABLE IF EXISTS Ubicacion;''')
    conn.cursor().execute('''DROP TABLE IF EXISTS Tiempo;''')
    conn.commit()
    print('Base de datos vacia')
    