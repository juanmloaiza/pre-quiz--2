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

