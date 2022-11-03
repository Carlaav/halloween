import numpy as np

def sarrus33_carla(M):
    # convertimos a numpy
    M = np.matrix(M) # matriz original
    subm = np.matrix(M[:,0:2]) # submatrix para ampliar
    M = np.concatenate((M,subm),axis=1) # matriz ampeada
    positivos = 0 
    negativos = 0
    for i in range(3):
        positivos = positivos + M[0,i]*M[1,i+1]*M[2,i+2] # suma de positivos
        negativos = negativos - M[2,i]*M[1,i+1]*M[0,i+2]# suma de negtivo
    return(positivos+negativos)



if __name__ == "__main__":
    #matriz 
    matriz = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            matriz[i][j] = float(input("Posicion ({},{}) = ".format(i,j)))
    print(sarrus33_carla(matriz))
