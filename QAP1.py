# Program for Edsel Car Rental Company to calculate costs
# for automobile rental

# Written by Kara Balsom
# Date Written: January 18, 2022

# Define Program Constants:
HST_RATE = 0.15
RENT_PER_DAY = 35.00
KILO_RATE = 0.10

# Gather Required Data from User:
CustName = input("Enter Customer Name: ")
PhoneNum = input("Enter Phone Number: ")
NumDays = int(input("Enter Number of Days Car was Rented: "))
StartMile = int(input("Enter the Mileage when Car was Rented: "))
ReturnMile = int(input("Enter the Mileage when Car was Returned: "))

# Perform the Required Calculations:
TotKilo = ReturnMile - StartMile
RentCost = (RENT_PER_DAY * NumDays) + (KILO_RATE * TotKilo)
HST = (RENT_PER_DAY * NumDays) * HST_RATE
TotRent = RentCost + HST

# Display Output Results for User:
print()
print("Customer Name:                 ",CustName)
print("Phone Number:                  ",PhoneNum)
print("Number of Days Car was Rented: ",NumDays)
print("Mileage when Car was Rented:    {:,}".format(StartMile))
print("Mileage when Car was Returned:  {:,}".format(ReturnMile))
print()
print("Total Kilometres Travelled:     {:,}".format(TotKilo))
print("Rental Cost:                  $ {:,.2f}".format(RentCost))
print("HST:                          $ {:,.2f}".format(HST))
print()
print("Total:                        $ {:,.2f}".format(TotRent))









