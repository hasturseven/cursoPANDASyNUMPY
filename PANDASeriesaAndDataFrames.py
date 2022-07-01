import pandas as pd

psg_players = pd.Series(['Navas', 'Mbappe', 'Neymar', 'Messie'],
                        index=[1, 7, 10, 30]
                        )  # le estoy dando el index a cada jugador osea ese sera su identificador si no le paso el orden del index
# si no le pongo el index comenzra en 0 el cual sera asignado para navas y terminando en 3 el cual sera el de messie
print(psg_players)

# otra manera de definir los pandas sires son con los diccionarios
""" lo podemos pasar de esta manera o podemos hacerlo de otra manera
diccionario=pd.Series({1:'navas',7:'mbappe',10:'neymar',30:'messie'}
                        )
print(diccionario)"""
# esta es la otra manera
diccionario = {1: 'navas', 7: 'mbappe', 10: 'neymar', 30: 'messie'}
psg_players_diccionario = pd.Series(diccionario)
print(psg_players_diccionario)

#tambien podemos manejarlo como un vector paandole la posicion que seria el index
print(psg_players[30])

#tambien puedo hacer el slice
print(psg_players[::-1])

#AHORA USANDO EL DATAFRAME
diccionario_info={'jugador':['Navas', 'Mbappe', 'Neymar', 'Messie'],'Altura':[183.0,170.0,177.0,165.0],'Goles':[2,200,300,450]}

dataframeNuevo=pd.DataFrame(diccionario_info,index=[1, 7, 10, 30])

print(dataframeNuevo)

print()
print("tambien puedo mostrar las columnas",dataframeNuevo.columns)
print("tambien puedo mostrar los index que son como las filas",dataframeNuevo.index)
