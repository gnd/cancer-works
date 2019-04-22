# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb
import argparse
import ConfigParser

function clean(text):
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
    if ('laviATky' in text) isok = False
    if ('neipltouyvsi' in text) isok = False
    if ('zakomplexovanfdch' in text) isok = False
    if ('neskuteATned' in text) isok = False
    if ('teelvizy' in text) isok = False
    if ('cientedfica' in text) isok = False
    if ('ATme1ranice' in text) isok = False
    if ('mf3wiAcym' in text) isok = False
    if ('moATovfdm' in text) isok = False
    if ('puarictli' in text) isok = False
    if ('reafirmantes' in text) isok = False
    if ('bohuLlel' in text) isok = False
    if ('entornceuing' in text) isok = False
    if ('chocolatada' in text) isok = False
    if ('disappoint' in text) isok = False
    if ('attention-grabbing' in text) isok = False
    if ('beneLova' in text) isok = False
    if ('siaimlr' in text) isok = False
    if ('trigliceridos' in text) isok = False
    if ('vre1tila' in text) isok = False
    if ('le9kLZ' in text) isok = False
    if ('Ie2aall' in text) isok = False
    if ('mayonesase' in text) isok = False
    if ('poselstved' in text) isok = False
    if ('acltluay' in text) isok = False
    if ('tratamiento' in text) isok = False
    if ('csnlinuouoty' in text) isok = False
    if ('Vjerujem' in text) isok = False
    if ('odpovAAZ' in text) isok = False
    if ('mediterre2nea' in text) isok = False
    if ('te9rmino' in text) isok = False
    if ('obeavjstim' in text) isok = False
    if ('podobne9mu' in text) isok = False
    if ('liadspotu' in text) isok = False
    if ('prote1hl' in text) isok = False
    if ('econf3mico' in text) isok = False
    if ('keporkak' in text) isok = False
    if ('ove1lne93' in text) isok = False
    if ('chuletf3n' in text) isok = False
    if ('popraolvd' in text) isok = False
    if ('greenaATnA' in text) isok = False
    if ('pLedLtedm' in text) isok = False
    if ('nade1neda0a' in text) isok = False
    if ('faATinkLZ' in text) isok = False
    if ('LpanAlLtinA' in text) isok = False
    if ('vfdbAzedch' in text) isok = False
    if ('modeledny' in text) isok = False
    if ('nezaLlili' in text) isok = False
    if ('minsatreemove9' in text) isok = False
    if ('tambc3a9m' in text) isok = False
    if ('norme1lnA' in text) isok = False
    if ('nejLle1danAjLedch' in text) isok = False
    if ('klbuoboky' in text) isok = False
    if ('vyleylsmi' in text) isok = False
    if ('poijzues' in text) isok = False
    if ('deifintely' in text) isok = False
    if ('dpnirpog' in text) isok = False
    if ('dc3a1diva' in text) isok = False
    if ('ne1sledujedced' in text) isok = False
    if ('vyvste1ve1' in text) isok = False
    if ('mamc3a3e' in text) isok = False
    if ('oficie1lnedm' in text) isok = False
    if ('benc3a7ao' in text) isok = False
    if ('nezabedjened' in text) isok = False
    if ('enuoorms' in text) isok = False
    if ('piblush' in text) isok = False
    if ('lnoikog' in text) isok = False
    if ('zavedtal' in text) isok = False
    if ('vocc3aa' in text) isok = False
    if ('soasluhim' in text) isok = False
    if ('zvle1Ltnedm' in text) isok = False
    if ('saude1vel' in text) isok = False
    if ('prmeoblas' in text) isok = False
    if ('trlaspaantnci' in text) isok = False
    if ('itstrucnor' in text) isok = False
    if ('nerogs' in text) isok = False
    if ('ASIEstoy' in text) isok = False
    if ('ambetalinvnAjLed' in text) isok = False
    if ('telhne' in text) isok = False
    if ('volemanovfdch' in text) isok = False
    if ('f3timoo' in text) isok = False
    if ('campee3o' in text) isok = False
    if ('benc3a7ao' in text) isok = False
    if ('aweosme' in text) isok = False
    if ('ufLukanost' in text) isok = False
    if ('heelpd' in text) isok = False
    if ('infoarmtion' in text) isok = False
    if ('mildde' in text) isok = False
    if ('isndie' in text) isok = False
    if ('Knolwegde' in text) isok = False
    if ('tcriky' in text) isok = False
    if ('Callnig' in text) isok = False
    if ('jzaezd' in text) isok = False
    if ('tuhoght' in text) isok = False
    if ('Thgouht' in text) isok = False
    if ('Appearntly' in text) isok = False
    if ('aomunt' in text) isok = False
    if ('wspf3LpracA' in text) isok = False
    if ('inhsigt' in text) isok = False
    if ('Brtiish' in text) isok = False
    if ('parabc3a9ns' in text) isok = False
    if ('profedk' in text) isok = False
    if ('kolakui' in text) isok = False
    if ('kboaom' in text) isok = False
    if ('grac3a7a' in text) isok = False
    if ('crteavie' in text) isok = False
    if ('pozdravomVopred' in text) isok = False

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
