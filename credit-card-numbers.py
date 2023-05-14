#https://www.hackerrank.com/challenges/validating-credit-card-number/problem

'''
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

cardNumber = int(input())
#cardNumber = 1

for i in range(cardNumber):
    card = input()
    #card = "4144-4467-8912-3456"

    if not re.fullmatch("^[4,5,6][0-9]{3}-{0,1}[0-9]{4}-{0,1}[0-9]{4}-{0,1}[0-9]{4}$", card):
        print("Invalid")
        continue
    else:
        card = card.replace('-', '')
        
        match = re.search("(\\d)\\1{3,}", card)
        if match:
            print("Invalid")
            continue
     
    print("Valid")