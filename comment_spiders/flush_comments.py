# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb
import ConfigParser

def output_date(date):
    months =   {'Leden': '01',
                'Unor': '02',
                'Brezen': '03',
                'Duben': '04',
                'Kveten': '05',
                'Cerven': '06',
                'Cervenec': '07',
                'Srpen': '08',
                'Zari': '09',
                'Rijen': '10',
                'Listopad': '11',
                'Prosinec': '12'}
    date_arr = date.split('/')
    for name, num in months.items():
        date_arr[1] = date_arr[1].replace( num, name )
    return "%02d. %s %s" % (int(date_arr[0].strip('.')), date_arr[1], date_arr[2])

### load config
settings_file = 'comment_spiders/settings_python'
config = ConfigParser.ConfigParser()
config.readfp(open(settings_file))
dbhost = config.get('database', 'DB_HOST')
dbuser = config.get('database', 'DB_USER')
dbpass = config.get('database', 'DB_PASS')
dbname = config.get('database', 'DB_NAME')
dbtable = config.get('database', 'DB_TABLE')
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
query = "SELECT name, date, text FROM %s WHERE domain = '%s'" % (dbtable, domain)
cur.execute(query)
if cur.rowcount == 0:
    sys.exit("Cant find comments from %s" % domain)
else:
    for row in cur.fetchall():
        name = str(row[0])
        date = str(output_date(row[1]))
        text = str(row[2])
        comments.append([name,date,text])
db.close()

# print all the comments into a file
f = file(outfile, 'w')
for comment in comments:
    f.write("%s %s %s\n" % (comment[0], comment[1], comment[2]))
f.close()
