# Created by: Nicholas Brean
# Created on: Nov 2017
# Created for: ICS3U
# This program formats someones address

def print_address(address, city, prov, postal,apartment = '' ):
    # print address
    if apartment == '':
        print(address)
        print(city + ', ' + prov)
        print(postal)
    else:
        print(apartment)
        print(address)
        print(city + ', ' + prov)
        print(postal)

street_address = raw_input("Enter your address: ")
city = raw_input("Enter your city: ")
province = raw_input("Enter your province: ")
postal_code = raw_input("Enter your postal code: ")
apartment_choice = raw_input("Do you have an apartment number?(y/n): ")
if apartment_choice == 'y':
    apartment_number = raw_input("Enter your appartment number: ")
    print_address( street_address, city, province, postal_code, apartment_number)
else:
    print_address(street_address, city, province, postal_code)
