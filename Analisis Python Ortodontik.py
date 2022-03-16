import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import numpy as np
from PIL import Image

sheet2 = pd.read_excel("2021 Gastos Ortodontik.xlsx", sheet_name = "Totales")
print(sheet2.describe()) #solo DATOS NUMERICOS
#print(sheet2.describe())
#df_meses = sheet2.iloc[:, [3,4,5,6,7]]
#df_meses_mean = round(df_meses.mean(), 0)

#df_meses_sum = df_meses.sum(axis=1)
#df_meses_sum1 = df_meses_sum.head(10)
#df_meses_sum1.to_excel("suma_Totales_ortodontik.xlsx")

#df_meses_mean.to_excel("promedio_Totales_ortodontik.xlsx")

#df_meses_mean.plot(kind="bar")
#para exportar el grafico a png
#plt.savefig("df_meses_mean.png", dpi=300)
#plt.show()




#wb = openpyxl.load_workbook('analisis_ortodontik.xlsx')
#ws = wb.active

#img = openpyxl.drawing.image('df_meses_mean.png')
#Image.open("df_meses_mean.png")
#img.anchor(ws.cell('F1'))

#ws.add_image(img)
#wb.save('analisis_ortodontik.xls')

#grafico de lineas:
#df_meses_mean.plot()





