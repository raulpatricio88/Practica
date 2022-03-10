
import pandas as pd
import numpy as np

#mostrar todas las columnas
pd.set_option('display.max_columns', 20)

df_excel = pd.read_csv('StudentsPerformance.csv')

#sum, max, min, average, count
# print(df_excel.describe()) #solo data numerica
# por columnas
# print(df_excel.count())
# por filas
# print(df_excel.sum(axis=1))

#print(df_excel['math score'] + df_excel['reading score'] + df_excel['writing score'])

#count
#print(df_excel['gender'].value_counts())

df_excel['average'] = np.mean(df_excel, axis=1)
#if conditions
df_excel['pass/fail'] = np.where(df_excel['average'] > 70, 'Pass', 'Fail')


#multiple if conditions
conditions = [
    (df_excel['average']>=90),
    (df_excel['average']>=80) & (df_excel['average']<90),
    (df_excel['average']>=70) & (df_excel['average']<80),
    (df_excel['average']>=60) & (df_excel['average']<70),
    (df_excel['average']>=50) & (df_excel['average']<60),
    (df_excel['average']<50),
]

values = ['A', 'B', 'C', 'D', 'E', 'F']

df_excel['grades'] = np.select(conditions, values)

# sumif, countif, averageif
# solo obtener el promedio para el genero femenino

# print(df_excel[df_excel['gender'] == 'female'].count()) (filtrar y contar genero femenino)

# df_female = print(df_excel[df_excel['gender'] == 'female'] (sumar si?)
# df_female = print(df_excel[df_excel['gender'] == 'female'].count()) (contar si)
df_female = df_excel[df_excel['gender'] == 'female']
df_female['average'] = df_female.mean(axis=1) #(promedio si)
# sumar si con dos criterios:
# solo obtener el promedio para el genero femenino y grupo B
# df_2 = df_excel[(df_excel['gender'] == 'female') & (df_excel['race/ethnicity'] == 'group B ')] )preguntar a guillermo porque no cachi ni una we...

#buscarv localizar un elemento - combianr datos de 2 tablas













