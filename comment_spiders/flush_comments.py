# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb

# some variables
dbhost = "localhost"
dbname = "cnc_comments"
dbuser = "cnc_user"
dbpass = "cnc_pass"
db = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpass, db=dbname)
cur = db.cursor()

# process user input
if (len(sys.argv) > 2):
    domain = sys.argv[1]
    outfile = sys.argv[2]
else:
    sys.exit("Usage: python flush_comments <domain> <outfile>")

# get all comments from the db for a domain
comments = []
query = "SELECT name, date, text FROM comments WHERE domain = '%s'" % domain
cur.execute(query)
if cur.rowcount == 0:
    sys.exit("Cant find comments from %s" % domain)
else:
    for row in cur.fetchall():
        name = str(row[0])
        date = str(row[1])
        text = str(row[2])
        comments.append([name,date,text])
db.close()

# print all the comments into a file
f = file(outfile, 'w')
for comment in comments:
    f.write("%s %s %s\n" % (comment[0], comment[1], comment[2]))
f.close()
