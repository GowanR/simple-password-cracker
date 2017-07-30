#############################################################
# `hash.py` is a very simple hashing script. Hash a word    #
# in any of python's hash algorithms provided by hashlib.   #
#                                                           #
# Usage:                                                    #
# $ python hash.py <hash algorithm> <word>                  #
# $ python hash.py md5 password123                          #
#                                                           #
# Written by GowanR (Jul 30 2017)                           #
#############################################################

import sys
import hashlib

help_text = """
--help -h       prints help menu (you're looking at it)

Usage:
python hash.py <hash option> <word>
python hash.py md5 password

Hash options:
md5
sha1
sha224
sha256
sha512
"""
# make sure that the first arguent is given
try:
    sys.argv[1]
except IndexError:
    print help_text
    exit(0)
# check for help needed
if sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print help_text
# check for second argument
try:
    sys.argv[2]
except IndexError:
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

print hash_function(sys.argv[2]).digest()
