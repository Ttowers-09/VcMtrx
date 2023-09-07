# Números complejos

## Libreria NUMPY
La libreria Numpy también pronunciada Numpai es una biblioteca de lenguaje natural de Python, el cuál da soporte a la 
creación de vectores y matrices, junto a estas, una serie de operadores matemáticos

## ¿Qué es Pycharm y para que sirve?
Pycharm es el IDE más popular para el lenguaje de programación python.

## Como instalar la libreria numpy en Pycharm
Para poder descargar la libreria debemos hacer los siguientes pasos:
	- Abrir Pychar y crear un nuevo documento.
	- Vamos al aportado de "File" y luego a la opción de "New projects settings"
	- Se desplegará una ventana y daremos click en "Project interpreter", damos clic en la flecha donde dice 
		"Add interpreter"
	- Buscaremos el nombre de nuestro proyecto y daremos click.
	- En la parte superior izquierda aparecerá un + le daremos click y en la barra buscaremos "Numpy"
	- Daremos click y luego en la parte inferior derecha un boton en verde que dice "Add package"
	- Esperaremos que cargue y listo ya quedó la libreria instalada en nuestro entorno de programación.
	- Para importar la función escribimos "import Numpy as np" y podremos disponer de la funciones de la libreria.

## Función "Complex" en python.
La función complex devuelve un número imaginario a partir de valores cedidios como argumentos.
La parte derecha de nuestro argumento se interpreta como parte imaginaria.
tupla (a,b) -> (a, bj)
 

## Función 1 (suma de vectores complejos)
La función número 1 *sumavect*  toma dos vectores complejos defindos previamente con la función complex y los suma.
Vector 1 + Vector 2 -> Vector_resultado

## Función 2 (Suma Vector inverso aditivo complejos)
La función número 2 *sum_inver* toma un vectores complejo defindo previamente con la función complex y los suma con el 
mismo pero negativa, obtendremos un vector de tamaño igual pero en sus pocisiones tendra 0.
(Vector + (-vector 1) -> Vector 0)

## Función 3 (Multiplicación de un Escalar por un vector complejo)
La función número 3 *multEsc_vect* toma dos parámetros anteriormente definidos los cuales son un vector complejo y un 
valor escalar que pertenece a los reales; entre ellos dos se multiplican.
(Escalar * vector1 -> vector_resultado)

## Función 4 (adición de matrices complejas)
La función número 4 *SumMatrix* toma dos parámetros definidos anteriormente los cuales son dos matrices complejas de 
tamaño R^n y las suma
(Matriz1 + Matriz 2 -> matriz_resultado)

## Función 5 (Inversa (aditiva) de una matriz compleja).
La función 5 *SumAditMatriz* toma una matriz compleja definda previamente y la suma con la mismo pero negativa, 
obtendremos una matriz de tamaño igual pero en sus pocisiones tendra 0.
(matriz1 + (-matriz1) -> matriz_resultado)

## Función 6 (Multiplicación de un Escalar por una matriz compleja)
La función número 5 *MultEMatrix* toma dos parámetros anteriormente definidos los cuales son una matriz compleja y un 
valor escalar que pertenece a los reales; entre ellos dos se multiplican.
(Escalar * matriz1 -> matriz_resultado)

## Función 7 (Matriz transpuesta)
La función número 5 *transpuestaMatriz* toma una matriz y junto el comando de "np.transpose(m1)" que nos brinda la 
libreria Numpy invertimos las filas por columnas.
(matriz1 -> matriz_transpuesta)

transpuestaMatriz
La función número 7a. *transVector* toma un vector y junto np.transpose(v1) el cual nos facilita la libreria Numpy 
invertimos las filaspor columas, como es un espacio unidimensional en Pycharm lo arroja de la misma manera.
(vector1 -> vector1)

## Función 8 (Matriz conjugada)
La función número 8 *ConjMatrix* toma una matriz definida anteriormente y junto al comando de "np.conjugate(m1)" el 
cuál es propio de la libreria Numpy podemos encontrar una matriz conjugada.
(matriz1 -> matriz_conjugada)

La función número 8.a *ConjVect* toma un vector definido anteriormente y junto al comando de "np.conjugate(m1)" el cuál 
es propio de la libreria Numpy podemos encontrar un vector conjugado.
(matriz1 -> matriz_conjugada)

## Función 9 (matriz_adjunta).
La función número 9 *adjunMatrix* toma una matriz definida anteriormente y junto al comando de 
"np.conjugate(np.transpose(m1))" los cuales son propios de la libreria Numpy podemos encontrar una matriz adjunta.
(matriz -> matriz_adjunta)

## Función 10 (producto entre matrices con tamaños compatibles)
La función número 10 *productMatrix* toma dos matrizes imaginarias, ambas de tamaño R^n ylas multiplica entre ellas.
(matrix1 * matriz2 -> matriz_resultado)

## Función 11 (acción de una matriz sobre un vector)
La función número 11 *accmatrix* toma dos parámetros, el primero una matriz y el segundo un vector ambos imaginarias, 
Existe una restricción con esta operación y es que el vector debe tener la misma cantidad de filas como la matriz de 
columas.
(vectorv * matrizv -> matriz_resultado)

## Función 12 (producto interno entre vectores)
La función número 12 *ProdcIntVc* toma dos vectores complejos definidos anteriormente, junto a la función 
de "np.dot(v1,v2)" podemos calcular el producto interno entre los vectores; el producto interno también se 
denomina producto punto.
(vector1 dot vector2 -> vector_resultado)

## Función 13 (Norma de un vector)
La función número 13 *normVect* toma un vector complejo definido anteriormente y aplicando la función 
"np.linalg.norm(v1)" propia de la libreria Numpy podemos encontrar la norma.
(vector1 -> irracional)

## Función 14 (Distancia entre dos vectores)
La función número 14 *DistVect* toma dos vectores complejos definidos anteriormente y aplicando la función 
"np.linalg.norm(v2-v1)" propia de la libreria Numpy podemos encontrar la distancia entre dos vectores.
(vector2 - vector1 -> irracional)

## Función 15 (Valores  y vectores propios de una matriz)
La función número 15 *ValPropMatr* toma una matriz compleja definida anteriormente y aplicando la función 
"np.linalg.eig(m1)" propia de la libreria Numpy podemos encontrar los valores propios
(matriz -> lista)

## Como se deben ejecutar las pruebas.
Las pruebas se deben ejecetar primero llamando la libreria unitest, a partir de ahi seguimos el procedimiento de llamar 
nuesta función de la libreria pasada. a partir de ahi definimos nuestras variables a utilizar y el valor que deseamos 
esperar, definimos la operación y al final citamos "np.testing.assert_almost_equal (operación, valor esperado)"
