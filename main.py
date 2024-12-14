import random

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
random_string = ""
x = int(input("Mau berapa password?"))
for i in range(x):
    random_string += random.choice(chars)
print(random_string)
