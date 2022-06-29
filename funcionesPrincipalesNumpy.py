import numpy as np

arr=np.random.randint(1,20,10)

#usando reshape la ocnvertiremos en matrix
matriz=np.reshape(arr,(2,-1),'C')
#el menos uno es que lo cuadre sin importar la cantidad de datos
print(matriz)
#para saber el maximo valor usamos .max
#al parametro max se le puede psar un eje recordando que el 1 es x (en este caso las filas) y con el 0 (cero) es el y (en este caso las columnas
print("mostrando el maximo valor de mi matriz",np.max(matriz,0),np.max(matriz,1) )

#argmax() me da el indice de donde se encuentra el valor mas grande del array y si esta repetido muestra el del menor indice osea el que se encuentra primero tambien le podemos pasar los ejes

print("mostrando el indice de donde esta el valor mas grande de la matriz" , np.argmax(matriz),np.argmax(matriz,1),np.argmax(matriz, 0))

#y para el minimo tenemos el min y argmin
#si uso con matriz me genera un error pero en realidad no lo hay por eso es mejor usar con el np.min ya que como matriz es una instancia de np por la razon es un se convierte en np por eso podemos usar matriz en lugar de np
print("valor mas pequeño" ,matriz.min(),np.argmin(matriz),np.argmin(matriz,1),np.argmin(matriz,0))

#np.ptp() es de un pico a otro pico es decir pic to pic esto me retorna el pico mas bajo y mas alto pero la diferencia tambien podemos usar ejes
print("la diferencia entre el pico mas alto y bajo de la matriz ", np.ptp(matriz)," ahora con ejes ", np.ptp(matriz,0),np.ptp(matriz,1))

#para la estadistica podemos generar el pporcentaje segun el que yo quiera ejemplo hallar el valor medio de la matriz
print("generando la media de mi matriz",np.percentile(matriz,50))
#para organizar lam atriz hacemos el sort
print("esto me organizara la matriz de menor mayor",np.sort(matriz))
#np.median me da la mediana de un arreglo la ventaja del eprcentil es que puedo ponerle el porcentaje que yo quiera como todas las opciones podemos meterle los ejes a las anteripres tambien se le puede meter
print("esta es la mediada  y tambien la otra es con eje",np.median(matriz),np.median(matriz,1))
#ahora la desviacion estandar la logramos con np.std
print("desviacion estandar ", np.std(matriz))
#el np-var me da la varianza
print("imprimiendo la varianza", np.var(matriz))
#np.mean me da la media del arreglo
print("obteniendo la mediana ", np.mean(matriz))

#concatenar arrays
arreglo1=np.array([[1,2],[3,4]])
arreglo2=np.array([5,6])

print("aca se ve que el arreglo2 es un vector",arreglo2)
#si hacemos esto generara error tenemos que llevar ambo a la misma dimension y lo podemos hacer de diferentes maneras el cero son las filas y el 1 las columnas
#arreglo3=np.concatenate((arreglo1,arreglo2),axis=0)


#convirtiendolo en matriz con reshape
#arreglo2=np.reshape(arreglo2,(1,-1))


#tambien lo podriamos convertir en dos dimensiones de esta manera con expand_dimns
arreglo2=np.expand_dims(arreglo2,axis=0)
print("y ahora podemos ver que convetimos el arreglo2 en una matriz osea dos dimensiones ya lo podemos ocncatenar",arreglo2)
#concatenando el arreglo
arreglo3=np.concatenate((arreglo1,arreglo2),axis=0)
print(arreglo3)

#"""" ahora si lo hubiera querido por el eje 1 osea columnas   usamos la transpuesta  con arreglo2.T nos transpone la matriz  """
arreglo3=np.concatenate((arreglo1,arreglo2.T),axis=1)
print("ahora con la transpuesta",arreglo3)

