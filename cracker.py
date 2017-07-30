#############################################################
# `cracker.py` is a very simple password cracking script.   #
# With a md5 hash, it will go through a wordlist, and       #
# check if the hashed password matches with the wordlist    #
# password's hash. If so, you cracked the password.         #
#                                                           #
# Usage:                                                    #
# $ python cracker.py <password file> <wordlist file>       #
# $ python cracker.py pswd.txt rockyou.txt                  #
#                                                           #
# Written by GowanR (Jul 30 2017)                           #
#############################################################

import md5
import sys
import os
import timeit
import time

def simple_hash(value):
    return md5.new(value).digest()

def clear():
    os.system("clear")

def est_time_converter(value):
    # value in seconds
    unit = "seconds"
    if value > 60:
        value /= 60 # now value in minutes
        unit = "minutes"
        if value > 60:
            value /= 60 # now value in hours
            unit = "hours"
            if value > 24:
                value /= 24 # now value in days
                unit = "days"
                if value > 360:
                    value /= 360 # now in years
                    unit = "years"
    return value, unit
        
with open(sys.argv[1], 'r') as f:
    data = f.read()
data = data.rstrip("\r\n") # strip out new line char

with open(sys.argv[2], 'r') as f:
    password_list = f.read()

password_list = password_list.split("\n")
n_pass = len(password_list)

clear()
print "Cracking..."
start = time.time()
for test in password_list:
    if simple_hash(test) == data:
        print "Found password: ", test
        break
taken_time, time_unit = est_time_converter(time.time()-start)
print "Completed in ", taken_time, time_unit
print "Done."
