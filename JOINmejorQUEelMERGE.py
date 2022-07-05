import pandas as pd
"""recordar que el join trabaja con indices y es mejor y mas rapido que trabajar con merge"""

izq = pd.DataFrame({'A': ['A0','A1','A2'],
  'B':['B0','B1','B2']},
  index=['k0','k1','k2'])

der =pd.DataFrame({'C': ['C0','C1','C2'],
  'D':['D0','D1','D2']},
  index=['k0','k2','k3'])

#paa lo mismo que en el merge en canto la izquierda y derecha etc...
uninendoJoin= izq.join(der)


print(uninendoJoin,"union estandar")

#ahora usaremos inner para que me presente los datos comunes
innerJoin= izq.join(der,how='inner')
print(innerJoin,"usnado inner join")

#------- ahora con el outer traera todos los datos de ambos dataframes  asi se compartan entre si
outerJoin= izq.join(der,how='outer')
print(outerJoin,"usando outer join")

#--------------- ahora darle prioridad al letf trayendo los datos de la izq y solo los datos que comparta con el de la dere lo mismo pasa cuando damos rigth traera todos los datos de la derecha y solo los que se ocmparta con los de a izquiera
leftJoin= izq.join(der,how='left')
print(leftJoin,"usando left join")

rigthJoin= izq.join(der,how='right')
print(rigthJoin,"usando rigth join")

