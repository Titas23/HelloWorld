"""
Start by getting the street number 

If the street number is even, display eastbound

if it is not even, display westbound

finish program
"""


def calculate_street(street):
    print("Divide: ", street / 2)
    print("Modulus: ", street % 2 == 0)
    if street % 2 != 0:
        # If number is even dislplay eastbound
        print("The street number is Eastbound")
    else:
        # If number is odd display westbound
        print("The street number is Westbound")

calculate_street(35)