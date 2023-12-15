from openpyxl import load_workbook
workbook = load_workbook(filename="TdF Stages Riders Results (2011-).xlsx", read_only=True)
#print(workbook.sheetnames)

results23 = workbook['TdF2013 Results']
for row in results23:
    print(row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value)
#    for cell in row:
#        print(cell.value)
