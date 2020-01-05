"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def isMult (x, y):
    result = False
    if (x/y == int (x/y)):
        result = True
    return result

total = 0
for i in range (1, 1000):
    # print (i)
    # print (3, isMult (i, 3), 5, isMult (i,5))
    if (isMult (i, 3) or isMult (i, 5)):
        # print ("Either")
        total = total + i

print (total) # answer 233168