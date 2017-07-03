from math import sqrt

def producePrimes(num):
    
    if isinstance(num, (int, float, complex)):
        if num >= 3:
            prime_list = []
            prime_list.append(2)
            nextPrime = 3
            while nextPrime < num:
                isPrime = True
                sqrt_value = sqrt(nextPrime)
                sample_range = [i for i in prime_list if i <= sqrt_value]
                for i in sample_range:
                    if nextPrime%i == 0:
                        isPrime = False
                        break
                if isPrime:
                    prime_list.append(nextPrime)
                nextPrime += 2
            return prime_list
        else:
            raise ValueError('Number must be greater than 2')
    else:
        raise TypeError('You can only insert a number')
