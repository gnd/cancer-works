# -*- coding: utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import argparse

# process user input
parser = argparse.ArgumentParser(description='Renumbers lines in metadata.csv')
parser.add_argument('start', help='Number to start with.')
parser.add_argument('end', help='Number to end with.')
parser.add_argument('infile', help='Name of the infile.')
parser.add_argument('outfile', help='Name of the outfile.')
args = parser.parse_args()

# read the infile
f = file(args.infile, 'r')
lines = f.readlines()
f.close()

# Renumber
index = 1
relines = []
for line in lines:
    if ('johana' not in line.split('|')[0]):
        arr = line.split('|')
        if ((int(arr[0]) >= int(args.start)) & (int(arr[0]) <= int(args.end))):
            relines.append("johana-3-{:02d}|{}|{}".format(index, arr[1], arr[2]))
            index+=1
        else:
            relines.append(line)
    else:
        relines.append(line)

# write the outfile
f = file(args.outfile, 'w')
for line in relines:
    f.write(line)
f.close()
