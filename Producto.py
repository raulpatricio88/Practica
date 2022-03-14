
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

jornada1 = 0
opcion = 's'
print("Buen día!")

sheet['B2'] = 'Nombre'
sheet['B2'].border = border
sheet['C2'] = 'Rut'
sheet['C2'].border = border
sheet['D2'] = 'Cargo'
sheet['D2'].border = border
sheet['E2'] = 'Sueldo base'
sheet['E2'].border = border
sheet['F2'] = 'Fecha de ingreso'
sheet['F2'].border = border
sheet['G2'] = 'Jornada'
sheet['G2'].border = border
sheet['H2'] = 'Años de antiguedad'
sheet['H2'].border = border
sheet['J2'] = 'Gratificacion legal'
sheet['J2'].border = border

for i in range (3, 71):
    while (opcion=='s'):
        print("Ingrese los datos del colaborador: ")
        nombre = input("Nombre: ")
        sheet[f'B{i}'] = nombre
        sheet[f'B{i}'].border = border
        rut = input("Rut: ")
        sheet[f'C{i}'] = rut
        sheet[f'C{i}'].border = border
        cargo = input("Cargo: ")
        sheet[f'D{i}'] = cargo
        sheet[f'D{i}'].border = border

        fechaIng = input("Fecha de ingreso: (formato dd-mm-aa) ")
        sheet[f'F{i}'] = fechaIng
        sheet[f'F{i}'].border = border

        jornada = input("Tipo de jornada: c: completa / m: media ")
        if(jornada=='c'):
            jornada1='Completa'
        else:
            jornada1='Media'
        sheet[f'G{i}'] = jornada1
        sheet[f'G{i}'].border = border
        antiwedad = input("Años de antiguedad: ")
        sheet[f'H{i}'] = antiwedad
        sheet[f'H{i}'].border = border
        sueldoB = float(input("Sueldo base: "))
        sheet[f'E{i}'] = sueldoB
        sheet[f'E{i}'].border = border
        grat = float(input("Gratificacion legal: $"))
        sheet[f'J{i}'] = grat
        sheet[f'J{i}'].border = border

        sueldoN= sueldoB + grat - (sueldoB)*0.19
        print("El sueldo neto es: $", + float(sueldoN))
        i+=1
        opcion = input("¿Desea agregar otro colaborador? s: si / n: no \N{tab}")

print("Documento generado satisfactoriamente. Que tenga un buen día!")
book.save('Prueba_producto.xlsx')


