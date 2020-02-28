#!/usr/bin/python3
process_number=int(input("How many values should we process: "))
for i in range(1,process_number):
       number = int(input())
       if number%3 == 0  and number%5 == 0:
                    print("fizzBuzz")
       elif number%3 == 0:
              print("Fizz")
       elif number%5 == 0:
             print("Buzz")
       else:
            print(number)      