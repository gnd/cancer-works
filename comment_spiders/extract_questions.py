# -*- coding: utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import argparse
import ConfigParser

# process user input
parser = argparse.ArgumentParser(description='Output all questions from infile into outfile.')
parser.add_argument('infile', help='name of the infile')
parser.add_argument('outfile', help='name of the outfile')
args = parser.parse_args()

# extract all lines with ?
tmp_questions = []
f = file(args.infile, 'r')
for line in f.readlines():
    if ('?' in line):
        # replace multiple ? with one
        tmp_questions.append(re.sub('\?+','?', line))
f.close()

# extract questions from q
questions = []
for q in tmp_questions:
    q = q.strip()
    index = q.find('?')
    while (index > -1):
        for i in reversed(range(index)):
            if (i == 0):
                question = q[0:index].strip() + ' ?'
                questions.append(question.strip().capitalize())
                break
            elif ((q[i].isupper() & ((q[i-1] == '(') | (q[i-1] == '/') | (q[i-1] == '.') | (q[i-1] == '!') | (q[i-1] == '?')))
                | ((q[i] == ' ') & ((q[i-1] == '(') | (q[i-1] == '/') | (q[i-1] == '.') | (q[i-1] == '!') | (q[i-1] == '?')))
                | (q[i] == '.')
                | (i == 0)):
                question = q[i:index].strip() + ' ?'
                questions.append(question.strip().capitalize())
                break
        index = q.find('?', index+1)

# output the questions
f = file(args.outfile, 'w')
for q in questions:
    f.write("%s\n" % q)
f.close()
