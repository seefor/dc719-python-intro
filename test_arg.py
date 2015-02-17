#!/usr/bin/python
import argparse
__author__ = 'Sif Baksh'
 
parser = argparse.ArgumentParser(description='This is a demo script by Sif Baksh.')
parser.add_argument('-i','--i',help='CIDR ie 10.10.10.', required=True)
args = parser.parse_args()
 
## show values ##
x=1
port=21
print (args.i + str(x), port)