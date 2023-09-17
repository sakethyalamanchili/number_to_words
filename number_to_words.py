n = input("Enter the Number : ")
intn = int(n)

ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
ten_power = ['hundred', 'thousand']

# QUIT IF MORE THAN 4 DIGITS
if len(n) > 4:
    print("Number can not exceed more than 4 digits.")
    quit()
    
# 4-DIGITS
if len(n) == 4:
    value_one = ord(n[-4]) - 48
    value_ten_power = ten_power[-1]
    value_tens_tens = ord(n[-2])- 48
    value_tens = ord(n[-2])- 48 + (ord(n[-1]) - 48)
    
    if n[-3] == '0':
        if n[-2] == '1':
            print(ones[value_one], value_ten_power, tens[value_tens])
        elif n[-2] != '1' and n[-1] == '0':
            print(ones[value_one], value_ten_power, tens_tens[value_tens_tens])
        elif n[-1] != '0':
            print(ones[value_one], value_ten_power, tens_tens[value_tens_tens], ones[ord(n[-1]) - 48])
    elif n[-3] != '0':
        if n[-2] == '1':
            print(ones[value_one], value_ten_power, ones[ord(n[-3]) - 48], ten_power[-2], tens[value_tens])
        elif n[-2] != '1' and n[-1] == '0':
            print(ones[value_one], value_ten_power, ones[ord(n[-3]) - 48], ten_power[-2], tens_tens[value_tens_tens])
        elif n[-1] != '0':
            print(ones[value_one], value_ten_power, ones[ord(n[-3]) - 48], ten_power[-2], tens_tens[value_tens_tens], ones[ord(n[-1]) - 48])
            
# 3-DIGITS
if len(n) == 3:
    value_one = ord(n[-3]) - 48
    value_ten_power = ten_power[-2]
    value_tens_tens = ord(n[-2])- 48
    value_tens = ord(n[-2])- 48 + (ord(n[-1]) - 48)
    
    if n[-2] == '1':
        print(ones[value_one], value_ten_power, tens[value_tens])
    elif n[-2] != '1' and n[-1] == '0':
        print(ones[value_one], value_ten_power, tens_tens[value_tens_tens])
    elif n[-1] != '0':
        print(ones[value_one], value_ten_power, tens_tens[value_tens_tens], ones[ord(n[-1]) - 48])

# 2-DIGITS (20 to 99)
if len(n) == 2 and (intn>=20 and intn<100):
    value_tens_tens = ord(n[-2])- 48
    if (ord(n[-1])-48) == 0:
        print(tens_tens[value_tens_tens])
    else:
        value_one = ord(n[-1]) - 48
        print(tens_tens[value_tens_tens],ones[value_one])
    
# 2-DIGITS (10 to 19)
if len(n)==2 and intn<20:
    value_tens = ord(n[-1])- 48 + (ord(n[-2]) - 48)
    print(tens[value_tens]) 
   
# 1-DIGIT 
if len(n)==1 and intn<10:
    value_one = ord(n[-1]) - 48
    print(ones[value_one])