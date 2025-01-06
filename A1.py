sick = input('Were you sick at all during the school year? (Y/N): ')
attend = int(input('Please Enter Your Attendance: '))
if sick == 'Y':
    print ('Allowed.')
else:
    if attend >= 75:
        print ('Allowed.')
    else:
        print ('Not Allowed.')
