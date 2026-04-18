rent=int(input('enter your hostel/flat rent='))
food=int(input('enter the number of food ordered='))
electricity_bill=int(input('enter the total electricity spent='))
charge_per_unit=int(input('enter the charge spent per unit='))
persons=int(input('enter the number of persons living in a flat='))

total_bill=electricity_bill*charge_per_unit
output=(food+rent+total_bill)//persons
print('each persons will pay=',output)



####output
enter your hostel/flat rent=5000
enter the number of food ordered=2000
enter the total electricity spent=500
enter the charge spent per unit=10
enter the number of persons living in a flat=4
each persons will pay= 3000
