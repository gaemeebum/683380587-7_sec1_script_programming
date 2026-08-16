import my_utils
import math
import random

my_utils.greet("Alice")

print("Is 7 prime?", my_utils.is_prime(7))
print("Is 10 prime?", my_utils.is_prime(10))

number = 25
result = math.sqrt(number)
print("Square root of", number, "is", result)

random_number = random.randint(1, 100)
print("Random number:", random_number)