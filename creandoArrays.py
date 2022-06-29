import numpy as np
# asi crearemos un array de un rango en especifico y el ter argumento son los saltos
array = np.arange(0, 10, 2)
print(array)
# asi creamos un arreglo de ceros
arrayZeros = np.zeros(7)
print(arrayZeros)
# si queremos que sea tipo matriz le pasamos la cantidad como una tupla ej el de zeros es el mas usado en ciencia de datos
matriz10x10 = np.zeros((10, 10))
print(matriz10x10)
# asi crearemos un array de unos
arregloUnos = np.ones(6)
print('imprimiendo arreglo de uno', arregloUnos)
# y apara crear matrix lo mismo
matrizUnos = np.ones((6, 6))
print("imprimiendo matriz de unos ", matrizUnos)


# esta fucion nos crea una matriz identidad obviamente cuadrada segun el rango que le pasemos
matrizIdentidad = np.eye(5)
print("imprimeindo la matriz identidad ", matrizIdentidad)

# genrar valores aleatorios con numpy y me da un valor aleatorio entre 0 y 1
valorAleatorioEscalar = np.random.rand()
# ahora arreglo de la posicin que yo le pase de o y 1
arregloAleatorio = np.random.rand(4)
print(arregloAleatorio)

# ahora una matriz de 0 y 1
matrizAleatorio = np.random.rand(4, 4)
print(matrizAleatorio)
# ahora un entero entre un rango  este caso sera de 1 a 15
enteroEnUnRango = np.random.randint(1, 15)
print(enteroEnUnRango)
# y ahora lo llevaremos a una estructura definida en este caso una tupla 10x10 que lo convierte en una matriz
matrizRangoAleatoriot = np.random.randint(1, 15, (10, 10))
print(matrizRangoAleatoriot)


# funcion linspace nos sirve para decir que genere una distribucion o apartir de un rango que le damos nos re una matriz o arreglo de una cantidad especifica que es el tercer valor que le pasamos
arregloDeCiertaCantidadLaCaulLeDoyYO = np.linspace(0, 20, 40)
# le estoy diciendo creame un arreglo con los numeros del 0 al 20  pero me tienes que dar 100 datos dentro de ese rango los cuales no se repetiran
print(arregloDeCiertaCantidadLaCaulLeDoyYO)

