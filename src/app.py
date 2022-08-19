from asyncio.windows_events import NULL
import pandas as pd 
import Opciones.BorrarModelo as opcion1
import Opciones.CrearModelo as opcion2
import Opciones.ExtraerInformacion as opcion3
import Opciones.CargarInformacion as opcion4
import Consultas.Reportes as Reportes


def menu():
    print('*********** MENU ***********')
    print('* 1. Borrar modelo         *')
    print('* 2. Crear modelo          *')
    print('* 3. Extraer información   *')
    print('* 4. Cargar información    *')
    print('* 5. Realizar consultas    *')
    print('* 0. Salir                 *')
    print('****************************')


if __name__ == '__main__':
    bandera = True
    informacion = NULL
    while bandera:
        menu()
        opcion = input()
        if opcion == '1':
            print('Borrar modelo')
            opcion1.Borrar()
        elif opcion == '2':
            print('Crear modelo')
            opcion2.Crear()
        elif opcion == '3':
            print('Extraer información')
            informacion = opcion3.Extraercsv()
            print('Se extrajo la siguiente información')
            print(informacion)
        elif opcion == '4':
            print('Cargar Informacion')
            opcion4.Cargar(informacion)
        elif opcion == '5':
            print('Consultas')
            print('1. Debe mostrar un SELECT COUNT(*) de todas las tablas para ver que si realizo la carga en las tablas del modelo.')
            print('2. Cantidad de tsunamis por año. ')
            print('3. Tsunamis por país y que se muestren loa años que han tenido tsunamis')
            print('4. Promedio de Total Damage por país')
            print('5. Top 5 de países con más muertes ')
            print('6. Top 5 de años con más muertes')
            print('7. Top 5 de años que más tsunamis han tenido ')
            print('8. Top 5 de países con mayor número de casas destruidas')
            print('9. Top 5 de países con mayor número de casas dañadas')
            print('10. Promedio de altura máxima del agua por cada país.')
            opcion = input()
            Reportes.Consulta(opcion)
        else:
            print('Salir')
            bandera = False
    