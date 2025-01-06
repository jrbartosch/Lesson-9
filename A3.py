print ('Select Your Ride.')
print ('1. Motorcycle')
print ('2. Car')
ride = int(input('Please Enter the Number of Your Selected Ride: '))
if ride == 1:
    print ('What Type of Motorcycle?')
    print ('1. Cruiser')
    print ('2. Adventure')
    print ('3. Standard')
    print ('4. Sport')
    print ('5. Dual Sport')
    print ('6. Touring')
    print ('7. Off-Road')
    print ('8. Bobber')
    print ('9. Scooter')
    ridetype = int(input('Please Enter The Number of Your Selected Type: '))
    if ridetype == 1:
        print ('You Selected the Cruiser Motorcycle.')
    elif ridetype == 2:
        print ('You Selected the Adventure Motorcycle.')
    elif ridetype == 3:
        print ('You Selected the Standard Motorcycle.')
    elif ridetype == 4:
        print ('You Selected the Sport Motorcycle.')
    elif ridetype == 5:
        print ('You Selected the Dual Sport Motorcycle.')
    elif ridetype == 6:
        print ('You Selected the Touring Motorcycle.')
    elif ridetype == 7:
        print ('You Selected the Off-Road Motorcycle.')
    elif ridetype == 8:
        print ('You Selected the Bobber Motorcycle.')
    elif ridetype == 9:
        print ('You Selected the Scooter Motorcycle.')
    else:
        print ('Invalid Input.')
elif ride == 2:
    print ('What Type of Car?')
    print ('1. Convertible')
    print ('2. Coupe')
    print ('3. Sports Car')
    print ('4. Hatchback')
    print ('5. Sedan')
    print ('6. Station Wagon')
    print ('7. SUV')
    print ('8. Crossover')
    print ('9. Minivan')
    ridetype = int(input('Please Enter The Number of Your Selected Type: '))
    if ridetype == 1:
        print ('You Selected the Convertible.')
    elif ridetype == 2:
        print ('You Selected the Coupe.')
    elif ridetype == 3:
        print ('You Selected the Sports Car.')
    elif ridetype == 4:
        print ('You Selected The Hatchback.')
    elif ridetype == 5:
        print ('You Selected the Sedan.')
    elif ridetype == 6:
        print ('You Selected the Station Wagon.')
    elif ridetype == 7:
        print ('You Selected the SUV.')
    elif ridetype == 8:
        print ('You Selected the Crossover')
    elif ridetype == 9:
        print ('You Selected the Minivan.')
    else:
        print ('Invalid Input.')
else:
    print ('Invalid Input.')