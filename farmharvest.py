#store world harvest in kg from each 5 fiels

field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110

 #calculate the avrage harvest

total = field1 + field2 + field3 + field4 + field5
average = total / 5

print("total harvest  :",total,"kg")
print("average per field  :",average,"kg")

# price per kg is 15 rupees-calulate total earning

price_per_kg = 15
earning = total * price_per_kg

print("total earnings   :Rs.", earning)

#total = 450 kg

bags = total//25
leftover = total % 25

print("full bags packed  :" , bags)
print("leftover grains   :" , leftover , "kg" )

last_year = 500

print("better than last year?  :",total > last_year)
print("same as last year ?  :",total == last_year)

