
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Border, Side
import time

#Producto que reune y calcula sueldos de colaboradores

book = Workbook()
sheet = book.active

top = Side(border_style='medium', color="000000")
bottom = Side(border_style='medium', color="000000")
left = Side(border_style='medium', color="000000")
right = Side(border_style='medium', color="000000")

border = Border(top=top, bottom=bottom, left=left, right=right)

opcion = 's'
print("Buen día!")

sheet['B2'] = 'Nombre'
sheet['B2'].border = border
sheet['C2'] = 'Rut'
sheet['C2'].border = border
sheet['D2'] = 'Sueldo Bruto'
sheet['D2'].border = border

for i in range (3, 71):
    while (opcion=='s'):
        print("Ingrese nombre, rut y sueldo bruto del colaborador: ")
        nombre = input("Nombre: ")
        sheet[f'B{i}'] = nombre
        sheet[f'B{i}'].border = border
        rut = input("Rut: ")
        sheet[f'C{i}'] = rut
        sheet[f'C{i}'].border = border
        sueldoB = input("Sueldo bruto: ")
        sheet[f'D{i}'] = sueldoB
        sheet[f'D{i}'].border = border
        i+=1
        opcion = input("¿Desea agregar otro colaborador? s: si / n: no \N{tab}")





book.save('Prueba_producto.xlsx')


