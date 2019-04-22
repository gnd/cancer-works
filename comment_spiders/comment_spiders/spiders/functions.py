import re
import unicodedata

def clean_text(text):
    text = text.replace('<br>',' ').replace('\n',' ').replace('\r',' ') # remove linebreaks
    text = re.sub('\.+','.', text)                                      # many dots > one dot
    text = re.sub('\!+','!', text)                                      # many ! > one !
    text = re.sub('\?+','?', text)                                      # many ? > one ?
    text = re.sub('\,+',',', text)                                      # many , > one ,
    text = re.sub('\*+','*', text)                                      # many * > one *
    # remove all links
    text = re.sub('<[^<]+?>', '', text)                                 # Remove HTML tags
    text = re.sub('http.*?( |$)',', ', text)                            # Remove http - starting addresses
    text = re.sub('www.*?( |$)',', ', text)                             # Remove www - starting addresses
    text = re.sub('[a-zA-Z]*\.(.*)\.php(\?)?.*?( |$)','', text)         # Remove .php containing links
    text = re.sub('[a-zA-Z]*\.(.*)\.html(\?)?.*?( |$)','', text)        # Remove .php containing links
    # dots
    text = re.sub('([a-zA-Z]?)\.([a-zA-Z]+)', "\\1. \\2", text)         # Fix . at end of sentence
    text = text.replace('.  ','. ')
    text = text.replace(' .','. ')
    # exclamatio marks
    text = re.sub('([a-zA-Z]?)\!([a-zA-Z]+)', "\\1! \\2", text)         # Fix ! at end of sentence
    text = text.replace('!  ','! ')
    text = text.replace(' !','! ')
    # question marks
    text = re.sub('([a-zA-Z]?)\?([a-zA-Z]+)', "\\1? \\2", text)         # Fix ? at end of sentence
    text = text.replace('?  ','? ')
    text = text.replace(' ?','? ')
    # commas
    text = re.sub('([a-zA-Z]?)\,([a-zA-Z]+)', "\\1, \\2", text)         # Fix , at end of sentence
    text = text.replace(',  ',', ')
    text = text.replace(' ,',', ')
    # spaces
    text = re.sub('\ +',' ', text)                                      # many ' ' > one ' '
    # remove various bordel
    text = text.replace('"','')                                         # remove double quotes
    text = text.replace("'",'')                                         # remove single quotes
    return text

def simple_clean_text(text):
    text = text.replace('<br>',' ').replace('\n',' ').replace('\r',' ') # remove linebreaks
    text = re.sub('\.+','.', text)                                      # many dots > one dot
    text = re.sub('\!+','!', text)                                      # many ! > one !
    text = re.sub('\?+','?', text)                                      # many ? > one ?
    text = re.sub('\,+',',', text)                                      # many , > one ,
    text = re.sub('\*+','*', text)                                      # many * > one *
    text = re.sub('\ +',' ', text)                                      # many ' ' > one ' '
    # remove various bordel
    text = text.replace('"','')                                         # remove double quotes
    text = text.replace("'",'')                                         # remove single quotes
    text = re.sub('<[^<]+?>', '', text)                                 # Remove HTML tags
    text = re.sub('http.*? ',', ', text)                               # Remove http - starting addresses
    text = re.sub('www.*? ',', ', text)                                # Remove www - starting addresses
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
    date = re.sub('<[^<]+?>', '', date)
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

def process_date_vitalion(date):
    date = date.split()[0]
    date_arr = date.split('.')
    return "%02d/%02d/20%s" % (int(date_arr[0]), int(date_arr[1]), date_arr[2])

def process_date_dama(date):
    date_arr = date.split('.')
    return "%02d/%02d/%s" % (int(date_arr[0]), int(date_arr[1]), date_arr[2])

def process_date_emimino(date):
    date_arr = date.split('.')
    return "%02d/%02d/%s" % (int(date_arr[0]), int(date_arr[1]), date_arr[2])
