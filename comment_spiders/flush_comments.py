# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb
import argparse
import ConfigParser

def clean(text):
    isok = True
    if ('maravilhosa' in text) isok = False
    if ('affiliate' in text) isok = False
    if ('onipeng' in text) isok = False
    if ('zLZstatek' in text) isok = False
    if ('cnoimg' in text) isok = False
    if ('mediterranei' in text) isok = False
    if ('zpracovanfd' in text) isok = False
    if ('huebdnedk' in text) isok = False
    if ('Nightworku' in text) isok = False
    if ('raseekmpzena' in text) isok = False
    if ('medicamento' in text) isok = False
    if ('zanahoria' in text) isok = False
    if ('pLedepedLe' in text) isok = False
    if ('coteolersl' in text) isok = False
    if ('psrapola' in text) isok = False
    if ('calientito' in text) isok = False
    if ('publikace' in text) isok = False
    if ('babydust' in text) isok = False
    if ('neaptli' in text) isok = False
    if ('famc3adlia' in text) isok = False
    if ('de9magogique' in text) isok = False
    if ('windsurfing' in text) isok = False
    if ('archdeacon' in text) isok = False
    if ('Pedobabo' in text) isok = False
    if ('Vykupujeme' in text) isok = False
    return isok

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
parser = argparse.ArgumentParser(description='Output scraped data from domain into outfile.')
parser.add_argument('-b', '--bare', action='store_true', help='dont output date and nickname')
parser.add_argument('-d', '--domain', default='all', help='the domain where the data was scraped from (default: all)')
parser.add_argument('outfile', help='name of the outfile')
args = parser.parse_args()

# get all comments from the db for a domain
comments = []
if (args.domain == 'all'):
    query = "SELECT name, date, text FROM %s" % (dbtable)
else:
    query = "SELECT name, date, text FROM %s WHERE domain = '%s'" % (dbtable, args.domain)
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
f = file(args.outfile, 'w')
for comment in comments:
    if clean(comment2):
        if args.bare:
            f.write("%s\n" % (comment[2]))
        else:
            f.write("%s %s %s\n" % (comment[0], comment[1], comment[2]))
f.close()
