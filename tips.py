TIP_OUT = .03 

totalSales = int(input('Enter total sales:'))

totalBeer = int(input('Enter total beer sales:'))

totalLiquor = int(input('Enter total liquor sales:'))

totalWine = int(input('Enter total wine sales:'))

totalDue = int(input('Enter total due:'))

totalAlchol = (totalBeer + totalLiquor + totalWine)

supportTip = (totalSales * TIP_OUT)

barTip = (totalAlchol * TIP_OUT)

tips = totalDue - (supportTip + barTip)

print (tips)
