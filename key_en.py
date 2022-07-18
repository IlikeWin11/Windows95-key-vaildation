#! /usr/bin/python
# coding:UTF-8
import random
import sys
import os

if os.name == "nt":                                                                                        # Determine the clear screen command
    cls = "cls"                                                                                            # CLS clear screen under Windows
else:
    cls = "clear"                                                                                          # clear clear screen under Linux

def rule():                                                                                                # View Windows 95/NT 4.0/Office 95 Serial Number Validation Rules
    print("Retail key:\n")
    print("XXX-XXXXXXX")
    print("The first 3 digits cannot be 333, 444, 555, 666, 777, 888, 999, and the sum of the last 7 digits must be a multiple of 7.")
    asdf = input("Press any key to continue...")
    os.system(cls)
    main()

def mod7_check(number): 
    """
    Function: Check the last 7 digits\r\n
    number:last 7 digits.
    """
    number = str(int(number))
    a = 0                                                                                                 # Initialize the sum to 0
    for i in number:                                                                                      # Iterate over each number in the string                         
        a += int(i)                                                                                       # Accumulate numbers
    if a % 7 == 0:                                                                                        # Determine if the sum is a multiple of 7
        return 1
    else:
        return 0

def check3(number):                                                                                       # Check if the first 3 digits appear in the blacklist
    """
    Function: Check the first 3 digits\r\n
    number:first 3 digits.
    """
    number = str(number)
    if number == "333":
        return 0
    elif number == "444":
        return 0
    elif number == "555":
        return 0
    elif number == "666":
        return 0
    elif number == "777":
        return 0
    elif number == "888":
        return 0
    elif number == "999":
        return 0
    else:
        return 1

def check(key):
    """
    Key check process.\r\n
    key:The key to check, submit the parameter as a string (str).
    """
    key = str(key)
    key_list = key.split("-")
    try:
        if check3(key_list[0]) == 1 and mod7_check(key_list[1]) == 1:
            print("Valid key.")
            asdf = input("Press any key to continue...")
            os.system(cls)
            main()
        else:
            print("Invalid key.")
            asdf = input("Press any key to continue...")
            os.system(cls)
            main()
        asdf = input("Press any key to continue...")
    except:
        os.system(cls)
        main()

def gen(number = 1):
    """
    Generate serial number.
    number:The number of serial numbers, the default is 1, optional parameter.
    """
    for i in range(number):                                                                             # Repeat command with for loop
        a = random.randint(100,998)                                                                     # Generate a random number
        if number == "333":                                                                             # Check whether the generated number appears in the blacklist, repeat if there is, if not, continue.
            gen()
        elif number == "444":
            gen()
        elif number == "555":
            gen()
        elif number == "666":
            gen()
        elif number == "777":
            gen()
        elif number == "888":
            gen()
        elif number == "999":
            gen()
        else:
            b = random.randint(1000006, 9999999)
            c = 0
            for i in str(b):                                                                            # mod7_check checks
                c += int(i)
            if c % 7 == 0:
                print(str(a)+"-"+str(b))
                akdh = input("Press any key to continue...")
            else:
                gen()


def main():
    """Main interface"""
    print("Windows 95 Product Key")
    print("=" * 33 + "\n")
    print("1. Check the verification mechanism\n2. Verify the serial number\n3. Generate the serial number")
    try:
        p = int(input("Option:"))
    except:
        os.system(cls)
        main()
        
    if p == 1:
        os.system(cls)
        rule()
    elif p == 2:
        os.system(cls)
        check(str(input("Product Key：")))
    elif p == 3:
        os.system(cls)
        gen(int(input("How many serial numbers to generate?")))
    else:
        os.system(cls)
        main()

if __name__ == "__main__":
    """Determine whether to execute in the main parser"""
    try:
        main()
    except:
        print("Error.")
        shdi = input("Press any key to continue...")
        os.system(cls)
        main()
