# -*- coding: utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import argparse
import ConfigParser

# TODO - remove ", change ev. into ev change napr. into napr

# process user input
parser = argparse.ArgumentParser(description='Output all questions from infile into outfile.')
parser.add_argument('-a', '--answers', action='store_true', help='output also the (presumed) answers')
parser.add_argument('-d', '--debug', action='store_true', help='output full versions of the comments')
parser.add_argument('infile', help='name of the infile')
parser.add_argument('outfile', help='name of the outfile')
args = parser.parse_args()

# extract all lines with ?
tmp_questions = []
tmp_answers = []
f = file(args.infile, 'r')
arr = f.readlines()
for i in range(len(arr)):
    if ('?' in arr[i]):
        # replace multiple ? with one
        tmp_questions.append(re.sub('\?+','?', arr[i]))
        # also add potential answer
        if (i+1 < len(arr)):
            a = re.sub('\?+','?', arr[i+1])
            a = re.sub('\.+','.', a)
            tmp_answers.append(re.sub('\?','.', a))
        else:
            a = re.sub('\?+','?', arr[i])
            a = re.sub('\!+','!', a)
            a = re.sub('\.+','.', a)
            tmp_answers.append(re.sub('\?','.', a))
f.close()

# extract questions from q
questions = []
questions_full = []
answers = []
answers_full = []
q_index = 0
for q in tmp_questions:
    q = q.strip()
    index = q.find('?')
    qs_found = 0
    while (index > -1):
        for i in reversed(range(index)):
            if (i == 0):
                question = q[0:index].strip() + ' ?'
                questions.append(question.strip().capitalize())
                questions_full.append(q)
                qs_found+=1
                break
            elif ((q[i].isupper() & ((q[i-1] == '(') | (q[i-1] == ')') | (q[i-1] == '/') | (q[i-1] == '.') | (q[i-1] == '!') | (q[i-1] == '?')))
                | ((q[i] == ' ') & ((q[i-1] == '(') | (q[i-1] == ')') | (q[i-1] == '/') | (q[i-1] == '.') | (q[i-1] == '!') | (q[i-1] == '?')))
                | (q[i] == '.')
                | (i == 0)):
                question = q[i:index].strip() + ' ?'
                questions.append(question.strip().capitalize())
                questions_full.append(q)
                qs_found+=1
                break
        index = q.find('?', index+1)
    # shall we also look for answers ?
    if (args.answers):
        # if we found some questions
        if (qs_found > 0):
            a = tmp_answers[q_index].strip()
            cap_found = False
            beg = 0
            end = 0
            # search for a capital letter denoting a sentence start
            for i in range(len(a)):
                if (a[i].isupper()):
                    beg = i
                    cap_found = True
                    break
            # now find the end of the sentence
            if (cap_found):
                for i in range(beg+1,len(a)):
                    if (a[i] == '.'):
                        end = i
                        break
                    if (a[i] == '!'):
                        end = i
                        break
                    if (a[i].isupper() & ((a[i-1] == '.') | (a[i-1] == '!') | (a[i-1] == '?'))):
                        end = i
                        break
                    if ((a[i] == ' ') & ((a[i-1] == '.') | (a[i-1] == '!') | (a[i-1] == '?'))):
                        end = i
                        break
                answer = a[beg:end].strip() + '.'
            # if we dont have a capital letter
            else:
                for i in range(0,len(a)):
                    for i in range(beg,len(a)):
                        if (a[i] == '.'):
                            end = i
                            break
                        if (a[i].isupper() & ((a[i-1] == '.') | (a[i-1] == '!') | (a[i-1] == '?'))):
                            end = i
                            break
                        if ((a[i] == ' ') & ((a[i-1] == '.') | (a[i-1] == '!') | (a[i-1] == '?'))):
                            end = i
                            break
                    answer = a[0:end].strip() + '.'
        # this is a bit of a hack but lets append the same answer even if we got more questions
        for _ in range(qs_found):
            answers.append(answer.strip().capitalize())
            answers_full.append(a)
    q_index+=1


# output the questions
f = file(args.outfile, 'w')
if (args.debug):
    for i in range(len(questions)):
        if (args.answers):
            f.write("Q: %s\n" % questions[i])
            f.write("Q full (%s)\n\n" % questions_full[i])
            f.write("A: %s\n" % answers[i])
            f.write("A full (%s)\n\n" % answers_full[i])
        else:
            f.write("%s\n" % questions[i])
            f.write("full (%s)\n\n" % questions_full[i])
else:
    if (args.answers):
        for i in range(len(questions)):
            f.write("Q: %s\n" % questions[i])
            f.write("A: %s\n\n" % answers[i])
    else:
        for q in questions:
            f.write("%s\n" % q)
f.close()
