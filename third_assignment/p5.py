# example list of numbers
l = [1, 4, 6, 11, 15, 24, 19, 25, 27, 30, 17]

# create an empty list to store the squares of prime numbers
prime_squares = []

# iterate over each number in the list
for num in l:
    # assume the number is prime
    is_prime = True
    # check if the number is greater than 1 and is not divisible by any integer from 2 to the number itself
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    # if the number is prime, append its square to the prime_squares list
    if is_prime and num > 1:
        prime_squares.append(num ** 2)

# print the list of squares of prime numbers
print(prime_squares)
