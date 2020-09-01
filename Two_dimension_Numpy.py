import numpy as np
X=np.array([[1,0,1],[2,2,2]])
a=X[1,0:2] #selecciona la array 1 y sus casillas de 0 a 2 (sin incluir la 2): [1, 0]
#print(a)

#Comandos de las arrays
# a.ndim  - número de dimensiones de la matriz
# a.shape - forma de la matriz: 2x3, 3x3, 4x4... en forma (2,3), (3,3)...
# a.size - tamaño de la matriz, es decir, nº de elementos. Si la m es 3x3, 9.


#np.sin(Z) otras operaciones con los números de la matriz
# z.T transpone la matriz
X=np.array([[1,0],[0,1]])
Y=np.array([[2,1],[1,2]])
Z=np.dot(X,Y) #multiplicación "dot product"
print (Z)
print(X*Y)