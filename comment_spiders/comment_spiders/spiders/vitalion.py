# -*- coding: utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
import MySQLdb

class VitalionSpider(scrapy.Spider):
    name = 'vitalion'
    curr_page = 0
    domain = 'http://diskuse.vitalion.cz'
    start_url = ''

    def __init__(self, maxpages=0, start_url="", delay=1.0, *args, **kwargs):
        super(VitalionSpider, self).__init__(*args, **kwargs)
        self.start_url = start_url
        self.maxpages = int(maxpages)
        self.dbhost = "localhost"
        self.dbname = "cnc_comments"
        self.dbuser = "cnc_user"
        self.dbpass = "cnc_pass"
        self.db = MySQLdb.connect(host=self.dbhost, user=self.dbuser, passwd=self.dbpass, db=self.dbname)
        self.cur = self.db.cursor()

    def start_requests(self):
        for i in range(self.maxpages):
            print "------ SCRAPING: %s/strankovani/%d" % (self.start_url, i+1)
            yield scrapy.Request("%s/strankovani/%d" % (self.start_url, i+1), callback=self.parse)

    def clean_text(self, text):
        text = text.replace('<br>',' ').replace('\n',' ').replace('\r',' ')
        text = text.replace(' , ', ', ')
        text = text.replace(' ,',', ')
        text = text.replace('.  ','. ')
        text = text.replace(',', ', ').replace(',  ', ', ')
        text = text.replace('  ',' ')
        text = text.replace(' .','. ')
        return text

    def strip_accents(self, text):
        try:
            text = unicode(text, 'utf-8')
        except (TypeError, NameError): # unicode is a default on python 3
            pass
        text = unicodedata.normalize('NFD', text)
        text = text.encode('ascii', 'ignore')
        text = text.decode("utf-8")
        return str(text)

    def parse(self, response):
        texts = response.xpath('//div[@class="emojione-output"]').extract()
        names = response.xpath('//div[@class="user_in"]').extract()
        tmp_dates = response.xpath('//span[@class="date"]').extract()
        dates = []
        for date in tmp_dates:
            if ('vky') not in date:
                dates.append(date)

        for i in range(len(texts)):
            text = texts[i].encode('utf8').replace('<div class="emojione-output">\n\t\t\t\n<p>','').replace('</p>\n\n\t\t</div>','')
            text = self.clean_text(text)
            text = self.strip_accents(text)
            if ('komunita' in names[i]):
                name = re.sub('<[^<]+?>', '', names[i].encode('utf8').replace('<div class="user_in">\n \t \n\t\t\t<b>',''))
            else:
                name = names[i].encode('utf8').replace('<div class="user_in">\n \t            \n\t\t\t<b>','').split('<a name=')[0]
            date = dates[i].encode('utf8').replace('<span class="date"><span> ','').replace('</span></span>','')

            # add to db
            yield {
            'domain': self.domain,
            'url': self.start_url,
            'text': text,
            'date': date,
            'name': name
            }
