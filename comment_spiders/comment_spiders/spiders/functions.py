import re
import unicodedata

def clean_text(text):
    text = text.replace('<br>',' ').replace('\n',' ').replace('\r',' ')
    text = text.replace(' , ', ', ')
    text = text.replace(' ,',', ')
    text = text.replace('.  ','. ')
    text = text.replace(',', ', ').replace(',  ', ', ')
    text = text.replace('  ',' ')
    text = text.replace(' .','. ')
    text = re.sub('<[^<]+?>', '', text)
    return text

def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

def process_date_doktorka(date):
    date = strip_accents(date)
    date = date.split('-')[0].strip()
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
    date_arr = date.split()
    for name, num in months.items():
        date_arr[1] = date_arr[1].replace( name, num )
    return "%02d/%s/%s" % (int(date_arr[0].strip('.')), date_arr[1], date_arr[2])

def process_date_abc(date):
    date_arr = date.split('.')
    return "%02d/%02d/%s" % (int(date_arr[0]), int(date_arr[1]), date_arr[2])
