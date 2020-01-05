"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
"""

i = 1
j = 2
total = 0

while i<4000000:
    # print (i)
    if (j/2 == int (j/2)):
        print (j)
        total = total + j
    k = i + j
    i = j
    j = k

print (total) # answer 4613732