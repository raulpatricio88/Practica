import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook
import numpy as np
#from PIL import Image

book = Workbook()

sheet = pd.read_excel("2021 Gastos Ortodontik.xlsx", sheet_name="1100 Operacional")
#sheet = index_col="Alcance" #esta indicacion de indice esta chocando con iloc

#print(sheet.describe()) #solo para DATOS NUMERICOS
#seleccion:
#df_meses4 = sheet.select_dtypes(include=['float64', 'str', 'int64'])

df_meses = sheet.iloc[:, [1,3,4,5,6,7]] #iloc es solo para indices integer

#ciclo que extraiga hacia una BD

c=0
j=1
for i in range (2, 7):
        sum = sheet['D2'] = sheet['D2'] +
        sheet[f'chr(ord(c)+j){i}'] = sheet[f'chr(ord(c)+i){i}'].sum()
        j+=1

#promedio:
#df_meses_prom = round(df_meses.mean(axis=0), 0)
#df_meses_prom = df_meses_prom.head(15)
#df_meses_prom.to_excel("promedio_Totales_ortodontik.xlsx")

#suma de las filas:
#df_meses_sum = df_meses.sum(axis=1)
#df_meses_sum1 = df_meses_sum.head(10)
#df_meses_sum1.to_excel("suma_Totales_ortodontik.xlsx")

#grafico de barras del promedio
#df_meses_prom.plot(kind="bar")

#plt.savefig("df_meses_prom.png", dpi=300)
#plt.show()

#1- calcular costos totales por proveedor
#2- agregar columna rut
#3- SQLite