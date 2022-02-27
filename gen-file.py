import sys

raw_name = sys.argv[1]
arr = raw_name.lower().split(" ")
name = "-".join(arr) + ".py"

f = open(name, 'w')
f.close()