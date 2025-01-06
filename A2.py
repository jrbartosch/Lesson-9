units = int(input('Please Enter the Number of Units Consumed: '))
if(units < 50):
    amount = units * 0.03
    tax = 0.29
elif (units <= 100):
    amount = 2.19 + ((units - 50) * 0.038)
    tax = 0.41
elif (units <= 200):
    amount = 2.19 + 4.21 + ((units - 100) + 0.061)
    tax = 0.52
else:
    amount = 2.19 + 4.21 + 12.72 + ((units - 200) * 0.099)
    tax = 0.87
total = amount + tax
print ('\nElectricity Bill = $%.2f' %total)