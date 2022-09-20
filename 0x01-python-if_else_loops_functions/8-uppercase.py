#!/usr/bin/python3
def uppercase(str):
    for i in str:
         if ord('a') <= ord(i) <= ord('z'):
             i = chr(ord(i) - 22) 
         print("{:c}".format(i), end='')
    print("")
