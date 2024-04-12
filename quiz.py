#Creación de la matriz
import numpy as np
matriz_4d=np.random.rand(10,30,40,30)
print(matriz_4d.size)

#Copia en 3d
matriz_3d= matriz_4d.copy()[:,:,:,0:1]
