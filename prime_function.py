"""A function that generates prime numbers in for a given range"""

def prime_num(num):

    numbers = [] #list of prime numbers
    if not isinstance(num, int):
        raise TypeError

    if num <= 0:
        print ("Zero and numbers less than zero are not accepted!")

    elif num == 1:
        print ("1 is not a prime number")

    else:
        for i in range(2, num+1):
            for j in range(2, i):
                if (i%j == 0):
                    break
            else:
                numbers.append(i)

    return numbers

num = prime_num(70)
print(num)
