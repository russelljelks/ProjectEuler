"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# assuming the best method to factor a number N is to count up a list of primes from 2 to sqrt(N) and test each

########################################################################################
#         YES I KNOW that the Seive of Eratosthenes is inefficient in this case.       #
# I ALSO KNOW that I probably didn't code it right anyway, since I did it from memory. #
#                              BUT IT WORKS - Eventually.                              #
########################################################################################

#N = 1000000001
N = 600851475143
NN = int (N**0.5)
# print (N, NN)

def primeList (N):
    list = []
    for i in range (2 ,NN + 1):
        list.append (i)
    
    for i in range (len (list)):
        if list [i]:
            print (i, list [i])
            for j in range (i+1, len (list)):
                if ((list[j] / list [i]) == int (list[j] / list [i])):
                    # print ('setting', list [j], 'to zero')
                    list [j] = 0

    finalList = []

    for each in list:
        if each: finalList.append (each)

    return finalList
                

listOfPrimes = primeList (N)
# print (listOfPrimes)

listOfFactors = []

for each in listOfPrimes:
    if not (N%each):
        listOfFactors.append (each)
        # print (each)

# print (listOfFactors)    ###############
print (listOfFactors [-1]) # answer 6857 #
                           ###############