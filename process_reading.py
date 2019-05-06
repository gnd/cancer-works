# -*- coding: utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import argparse

# process user input
parser = argparse.ArgumentParser(description='Processes a body of text into sentence metadata for Tacotron 2.')
parser.add_argument('infile', help='Name of the infile.')
parser.add_argument('outfile', help='Name of the outfile.', default='metadata.csv')
args = parser.parse_args()

# read the infile
f = file(args.infile, 'r')
lines = f.readlines()
f.close()

# process the data
text = ""
for line in lines:
    if line != '\n':
        text += line.replace('\n',' ')
text = text.replace('!“','.')
text = text.replace('?“','.')
text = text.replace('!','.')
text = text.replace('?','.')
text = text.replace('„','')
text = text.replace('“','')
text = text.replace("'",'')
text = text.replace(",",'')
text = text.replace("‘",'')
text = text.replace('…','')
text = text.replace(' — ',', ')
text = text.replace(' —, ',', ')
text = text.replace(' (',', ')
text = text.replace(') ',', ')
text = text.replace('  ',' ')

# find fake sentence ends (mostly in direct speech, the next letter after '. ' is not capitalized)
text_clean = ""
for i in range(len(text)):
    if i < len(text)-2:
        if ((text[i] == '.') & (text[i+1] == ' ') & (text[i+2].islower())):
            text_clean += ','
        else:
            text_clean += text[i]

# split the text into sentences
lines = text_clean.replace(':','.').split('. ')

# output the outfile
index = 1
f = file(args.outfile, 'w')
for line in lines:
    line_out = "{:02d}|{}|{}\n".format(index, line.strip().strip('.'), line.strip().strip('.'))
    f.write(line_out)
    index+=1
f.close()
