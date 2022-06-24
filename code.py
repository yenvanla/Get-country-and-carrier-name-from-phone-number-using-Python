import os, sys
try:
    import phonenumbers
    import pycountry
    from phonenumbers.phonenumberutil import (
        region_code_for_country_code,
        region_code_for_number,
        NumberParseException,
    )
    from phonenumbers import carrier, format_number, parse
except ImportError:
    os.systemn('pip3 install phonenumbers')
    os.systemn('pip3 install pycountry')
    import phonenumbers
    import pycountry
    from phonenumbers.phonenumberutil import (
        region_code_for_country_code,
        region_code_for_number,
        NumberParseException,
    )
    from phonenumbers import carrier, format_number, parse
number = input("Enter your phone number: ")
# Check if the number is valid
try:
    number = parse(number, region=None)
    if number.country_code == 1:
        number = format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL)
        print(number)
    else:
        number = format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        print(number)
except NumberParseException:
    print("Invalid number!")
    exit()
# check if the number is valid
try:
    my_number = phonenumbers.parse(number)
    if not phonenumbers.is_valid_number(my_number):
        print("Invalid number!")
        exit()
except NumberParseException:
    print("Invalid number!")
    exit()
vung = region_code_for_country_code(my_number.country_code)
name = pycountry.countries.get(alpha_2=vung).name
print(my_number)
print(name)
print(carrier.name_for_number(my_number, vung))
