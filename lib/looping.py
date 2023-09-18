#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    countdown = 10
    while countdown >= 1:
        print(countdown)
        countdown-=1
        if countdown < 1:
            print("Happy New Year!")
            break

def square_integers(int_list):
    # code goes here!
    return [integer**2 for integer in int_list]

def fizzbuzz():
    # code goes here!
    for n in range(1,101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
           
        else:
            print(n)

