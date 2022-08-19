import pandas as pd 
import numpy as np 
    
def Extraercsv():

    Contenidocsv = pd.read_csv('F:/WillOP/u/Seminario2/Laboratorio/Practica1/historial_tsumamis.csv')
    df = pd.DataFrame(Contenidocsv)
    #print('/////////////////////////// Imprimiendo df ////////////////////////')
    #print(df)
    #print('/////////////////////////// Imprimiendo df.astype ////////////////////////////')
    df = df.replace({np.nan:0})
    df = df.replace("\"", '')
    df = df.replace("\'", '')
    df = df.iloc[1: , :] #Eliminando la primera fila
    
    return df