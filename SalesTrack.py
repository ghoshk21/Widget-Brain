import datetime, xlrd
book = xlrd.open_workbook("/home/nimish/Sales/sales data 2019 1-3.xlsx")
sh = book.sheet_by_index(0)
a1 = sh.cell_value(rowx=1, colx=2)

s = sh.nrows
print s

for row in (1,s-1):
	a1 = sh.cell_value(row, colx=2)
	a1 = (a1-43525)*10000000
	a1 = int(a1*24*60)
	a2 = sh.cell_value(row+1, colx=2)
	a2 = (a2-43525)*10000000
	a2 = int(a2*24*60)
	diff = a2-a1
	if diff>15 or diff==15:
		print a2, sh.cell_value(row+1,colx=3)


##Unfortunately couldn't finish on time, the plan was to:
#1. Load the excel file
#2. Read the datetime column in correct format
#3. Find two consecutive time difference and check if its greater than or equal to 15 mins, if yes, save those rows in a csv file and save it.


 
