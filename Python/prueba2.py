#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    
    for x in range(n+1) :
        if(x%3==0 and x % 5 ==0):
            print("FizzBuzz")
        
        elif(x%5==0):
            print("Buzz")
        elif(x%3==0):
            print("Fizz")
        else:
            print(x)

def main(n):
    fizzBuzz(n)

main(15)