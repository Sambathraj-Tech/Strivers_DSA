n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
============================================================================================================================================
import math
def prime_number(n):
    count = 0  # Count remains 0 then its prime
    if n <= 1 :                                   # n less than 1 , 0 or negative_integers so its not prime
        print(f"{n} is not a prime number.")
        return                                    # we return and stop the pgm
    elif n > 1:                                   # if its greater than 1 then executes
        for i in range(2, int(math.sqrt(n)) + 1): # remember math.sqrt change into (int)
            if n % i == 0:                        # It checks the remainder is zero if its count = 1
                count += 1
                if (n / i) != i:                  # It avoids the same number see the mathematical observation for better understanding
                    count +=1  
    if count == 0:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
prime_number(int(input("Enter a number: ")))
