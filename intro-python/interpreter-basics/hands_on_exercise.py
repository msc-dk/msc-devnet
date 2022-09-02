"""Python Interpreter and Basics Exercise.

Copyright (c) 2018-2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi

print(type(pi))
print(pi)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)

if i < 50:
	print("i is less than 50")
elif  i == 50:
	print("i is equal to 50")
else:
        print("i is greater than 50")


# TODO: Write a conditional that prints the color of the selected sportsball
picked_sportsball = random.choice(['tennis', 'basketball', 'golf'])

print("The picked ball is {}".format(picked_sportsball))



# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.

def multiply(a, b):
    result = a * b
    return result


# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",)
print(multiply(12, 96))


print("48 x 17 =",)
print(multiply(48, 17))

print("196523 x 87323 =",)
print(multiply(196523, 87323))
