import pandas as pd
from openpyxl import Workbook
import numpy as np
sheet2 = pd.read_excel("2021 Gastos Ortodontik.xlsx", sheet_name = "Totales")
#print(sheet2.describe())
df_meses = sheet2.iloc[:, [3,4,5,6,7]]
print(df_meses)
#df_meses = sheet2.iloc[]

