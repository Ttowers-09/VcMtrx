import numpy as np
def sumavect (v1, v2):
    result = v1 + v2
    return (result)
def sum_inver (v1):
    result = v1 + (-v1)
    return (result)
def multEsc_vect (E, v1):
    result = E * v1
    return (result)
def SumMatrix (m1,m2):
    result = m1 + m2
    return (result)

def SumAditMatriz (m1):
    result = m1 + (-m1)
    return (result)

def MultEMatrix (E, m1):
    result = E * m1
    return (result)

def transpuestaMatriz (m1):
    result = np.transpose(m1)
    return (result)

def transVector (v1):
    result = np.transpose(v1)
    return (result)

def ConjMatrix (m1):
    result = np.conjugate(m1)
    return (result)

def ConjVect (v1):
    result = np.conjugate(v1)
    return (result)

def adjunMatrix (m1):
    result = np.conjugate(np.transpose(m1))
    return (result)

def productMatrix (m1, m2):
    result = m1 * m2
    return (result)

def accmatrix (m, v):
    result = np.dot(m, v)
    return (result)

def ProdcIntVc (v1, v2):
    result = np.dot (v1, v2)
    return (result)

def normVect (v1):
    result = np.linalg.norm(v1)
    return (result)

def DistVect (v1, v2):
    result = np.linalg.norm(v2-v1)
    return (result)

def ValPropMatr (m1):
    result = np.linalg.eig(m1)
    return (result)
def Vectprop (m1):
    result = np.linalg.eig(m1)
    return (result)

if __name__ == '__main__':
    v1 = np.array([complex(-2,31), complex(14, -10), complex (16, -35)])
    v2 = np.array([complex(11,-27), complex(50, 19), complex (-4, 44)])
    v = np.array([[complex(1, 3), complex(4, 5)]])

    E = 4
    m1 = np.matrix([[complex(1,3), complex(4, -6)], [ complex (7, -9),complex(2,-5)]])
    m2= np.matrix ([[complex(1,3), complex(4, 5)], [ complex (6, -5),complex(9,-0)]])
    v = np.array ([[complex(1,3), complex(4, 5)]])
    m = np.matrix([complex(11, -27)])



    print ("Suma de vectores complejos")
    print (sumavect (v1, v2))
    print ("Suma de inversos aditivos de un vector complejo")
    print(sum_inver (v1))
    print ("Multiplicación de una escalar por un vector complejo")
    print (multEsc_vect (E, v1))
    print("Suma de matrices complejas")
    print( SumMatrix (m1,m2))
    print("Inverso aditivo de una matriz compleja")
    print(SumAditMatriz (m1))
    print ("Multiplicacion de una matriz compleja por un escalar")
    print( MultEMatrix (E, m1))
    print("Transpuesta de una matriz compleja")
    print(transpuestaMatriz (m1))
    print("Transpuesta de un vector")
    print (transVector (v1))
    print ("Conjugada de una matriz")
    print (ConjMatrix (m1))
    print("Conjugada de un vector")
    print (ConjVect (v1))
    print ("Adjunta de una matriz")
    print ( adjunMatrix (m1))
    print ("producto entre dos matrices de tamaño compatible")
    print ( productMatrix (m1, m2))
    print ("Acción de un vector sobre una matriz")
    print (accmatrix (m, v))
    print("Producto interno de dos vectores")
    print(ProdcIntVc (v1, v2))
    print("Norma de un vector")
    print (normVect (v2))
    print("distancia entre dos vectores")
    print(DistVect (v1, v2))
    print("Vales y vectores propios de una matriz")
    print (ValPropMatr (m1))
    print (Vectprop(m1))