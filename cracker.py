#####################################################################
# `cracker.py` is a very simple password cracking script.           #
# With a md5 hash, it will go through a wordlist, and               #
# check if the hashed password matches with the wordlist            #
# password's hash. If so, you cracked the password.                 #
#                                                                   #
# Usage:                                                            #
# $ python cracker.py <hash option> <password file> <wordlist file> #
# $ python cracker.py md5 pswd.txt rockyou.txt                      #
#                                                                   #
# Written by GowanR (Jul 30 2017)                                   #
#####################################################################

import hashlib
import sys
import timeit
import time

help_text = """
-h --help       prints help menu (you're looking at it)

Usage:
python cracker.py <hash option> <password file> <wordlist file>
python cracker.py md5 pswd.txt rockyou.txt

Hash Options:
md5
sha1
sha224
sha256
sha512
"""
try:
    sys.argv[1]
except IndexError:
    print help_text
    exit(0)

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print help_text
    exit(0)

try:
    sys.argv[2]
    sys.argv[3]
except IndexError:
    print "Not enough arguments."
    print help_text
    exit(0)

hash_function = hashlib.md5
func_name = sys.argv[1]
if func_name == "md5":
    hash_function = hashlib.md5
elif func_name == "sha1":
    hash_function = hashlib.sha1
elif func_name == "sha224":
    hash_function = hashlib.sha224
elif func_name == "sha256":
    hash_function = hashlib.sha256
elif func_name == "sha512":
    hash_function = hashlib.sha512
else:
    print("Unknown hash given.")
    exit(0)

def simple_hash(value):
    return hash_function(value).digest()

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
        
with open(sys.argv[2], 'r') as f:
    data = f.read()
data = data.rstrip("\r\n") # strip out new line char

with open(sys.argv[3], 'r') as f:
    password_list = f.read()

password_list = password_list.split("\n")
n_pass = len(password_list)

print "Cracking..."
start = time.time()
for test in password_list:
    if simple_hash(test) == data:
        print "Found password: ", test
        break
taken_time, time_unit = est_time_converter(time.time()-start)
print "Completed in ", taken_time, time_unit
print "Done."
