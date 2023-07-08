#!/usr/bin/env python3

def happy_new_year():
    for i in range(10,0,-1):
        print(f"{i}")
    print("Happy New Year!")

def square_integers(int_list):
    numbers = []
    for num in int_list:
        number = num * num
        numbers.append(number)
    return numbers

def fizzbuzz():
    for i in range(1,101):
        if (i%3 == 0 and i%5 == 0):
            print ("FizzBuzz")
        elif(i%3 == 0):
            print("Fizz")
        elif (i%5 == 0):
            print("Buzz")
        else:    
            print(i)
