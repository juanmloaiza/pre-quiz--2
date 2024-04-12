#Creación de la matriz
import numpy as np
matriz_4d=np.random.rand(10,30,40,30)
print(matriz_4d.size)

#Copia en 3d
matriz_3d= matriz_4d.copy()[:,:,:,0:1]

#Atributos de la matriz
print("Dimensiones:" , matriz_3d.shape)
print("Tamaño:" , matriz_3d.size)
print("Tipo de datos:" , matriz_3d.type)

#Modificación y pasar a 2d
matriz_2d= matriz_3d.reshape(-1,matriz_3d.shape[-1])

#convertir la matriz
import pandas as pd
def matriz_a_dataframe(matriz):
    df= pd.FataFrame(matriz)
    return df
de_matriz= matriz_a_dataframe(matriz_2d)

#cargar csv y .mat
import scipy.io as sio
def cargar_matriz(path):
    matriz= sio.loadmat(path)
    return matriz

def cargar_csv(path):
    df=pd.read_csv(path)
    return df 

#Operaciones básicas
def suma(matriz, axis=None):
    return np.sum(matriz, axis=axis)

def resta(matriz1, matriz2):
    return matriz1-matriz2

def multiplicacion(matriz1,matriz2):
    return np.multiply(matriz1,matriz2)

def division(matriz1,matriz2):
    return np.divide(matriz1,matriz2)

def logaritmo(matriz):
    return np.log(matriz)

def promedio(matriz, axis=None):
    return np.mean(matriz,axis=axis)

def desviacion_estandar(matriz,axis=None):
    return np.std(matriz,axis=axis)
