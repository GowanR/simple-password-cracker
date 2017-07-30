import md5
import sys

print md5.new(sys.argv[1]).digest()
