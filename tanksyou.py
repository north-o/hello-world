my_name = "North"

import time

my_age = 12

your_name = input("What is your name? ")

print ("Your name is", your_name)

your_age = input("What is your age? ")

print("================")
print("Your name is", your_name, "and your are", your_age, "years old.")
print("================")
print("My name is", my_name, "and I am", my_age, "years old.")
print("================")

meow = 5

print("================")
print("Meow is", meow)
print("================")
time.sleep(1)

meow = meow+1

print("Meow + 1 =", meow)
print("================")

time.sleep(1)

meow = meow+my_age

print("Meow + My Age =", meow)
print("================")