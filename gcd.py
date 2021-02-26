def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        if (a % i == 0) and (b % i == 0):
            gcd = i
            
    return gcd

print(gcdIter(60,48))