#!/usr/bin/python3
'''Implement task for minimum operations project'''

def minOperations(n):
    '''Method that validate the minimum number of operations
       For reached a number of letters in a text file
       Iterate over keys array, and, add new keys to opened set
       Return True if all boxes opened, else False
    '''
    divisor = maxDivisor(n)
    myArray = ["H"]
    operations = 0
    if divisor == 1:
        operations = n - 1
    elif n <= 0:
        operations = 0
    else:
        while len(myArray) <= n:
            '''Paste operation'''
            while len(myArray) <= divisor:
                myArray.append("H")
                operations += 1
            dupArray = myArray
            i = 0
            while i <= ((n /divisor) - 1):
                myArray += dupArray
                operations += 1
                i += 1

    return operations

def maxDivisor(n):
    counter = 2
    divisor = 1
    while counter <= (n/2):
        if n % counter == 0:
            divisor = counter

        counter += 1
    return divisor