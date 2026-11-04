#CMP-131, Week 08, Lab 08, Sales Bar Chart, Nov 4, 2026

ast="*"
store=(int("Enter Number of Store: "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Sales Bar Chart")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in range (store ):
	sales=int(input("Enter Today's Sales for Store "+str((i+1))+" :"))
	sales=int(sales/100)
	for count in range(sales):
		ast= ast + "*"
	ast= ast + "\n"
print(ast)
