import re
import sys

import argparse

__author__ = 'sif.baksh@gmail.com'

parser = argparse.ArgumentParser(description='RPZ Syslog Parser')
parser.add_argument('-i', '--input', help='Input file name', required=True)
parser.add_argument('-o', '--output', help='Output file name', required=True)
args = parser.parse_args()

f = open(str(args.input))
n = 0
r = open(str(args.output), "w")
for line in iter(f):
    m = re.search('(?<=\s\[A\]\svia\s)(\S*)(?=\"\"\"$)', line)
    if m:
        n = n + 1
        print m.group(1)
        r.write(m.group(1))
        r.write("\n")

print "[+] Found %s domains in : %s" % (n, str(args.input))
print "[+] Please check %s for the output!" % str(args.output)

# # show values ##
print ("Input file: %s" % args.input )
print ("Output file: %s" % args.output )

r.close()
f.close()