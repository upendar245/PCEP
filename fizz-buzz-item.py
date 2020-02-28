#!/usr/bin/env python3
number = int(input("Enter an integer value:"))
if number%3 == 0  and number%5 == 0:
                 print("fizzBuzz")
elif number%3 == 0:
      print("Fizz")
elif number%5 == 0:
      print("Buzz")
else:
    print(number)