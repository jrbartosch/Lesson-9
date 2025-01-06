print ('Select Your Ride.')
print ('1. Motorcycle')
print ('2. Car')
ride = int(input('Please Enter the Number of Your Selected Ride: '))
if ride == 1:
    print ('What Type of Motorcycle?')
    print ('1. Scooter')
    print ('2. Sport Motorcycle')
    ridetype = int(input('Please Enter The Number of Your Selected Type: '))
    if ridetype == 1:
        print ('You Selected Scooter.')
    if ridetype == 2:
        print ('You Selected Sport Motorcycle.')
    else:
        print ('Invalid Input.')
elif ride == 2:
    print ('What Type of Car?')
    print ('1. Sedan')
    print ('2. SUV')
    ridetype = int(input('Please Enter The Number of Your Selected Type: '))
    if ridetype == 1:
        print ('You Selected Sedan.')
    if ridetype == 2:
        print ('You Selected SUV.')
    else:
        print ('Invalid Input.')
else:
    print ('Invalid Input.')