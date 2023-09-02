#--------------------------------------------------------------------------------------------------------------------------------------
#Python program to parse header file and read all prototypes of function and insert it into excel sheet with unique ID start with IDX0.
#--------------------------------------------------------------------------------------------------------------------------------------


import re
import openpyxl as xl

arguments = []
returns   = [] 
protype   = []

def parsing(header):

    with open(header,'r') as funcs:
        file = funcs.read()

    with open("lcd.h", "r") as f:

        for line in f:
            return_type = line.split()
            if return_type:
                returns.append(return_type[0])

    pattern = r'\(.*?\)|\w+ |;|\s'
    founds = re.sub(pattern,' ',file)
    pattern = r'\w+\S'
    founds = re.findall(pattern,founds)
    for word in founds:
        founds = word.split()
        protype.append(founds)
    
    
    pattern = r'\(.*?\)'
    matches = re.findall(pattern,file)
    for match in matches:
        arguments.append(match.strip())

    workbook = xl.Workbook()
    sheet = workbook.active

    sheet['A1'] = 'ID'
    sheet['B1'] = 'Return'
    sheet['C1'] = 'Fun_Prototype'
    sheet['D1'] = 'Fun_Arguments'

    row = 0
    for i in range(len(returns)):
         row = i+2
         sheet[f'A{row}'] = f'IDX{i}'
         sheet[f'B{row}'] = returns[i]
         sheet[f'c{row}'] = protype[i][0]
         sheet[f'D{row}'] = arguments[i]


    workbook.save('Header_File.xlsx')
    

parsing('lcd.h')