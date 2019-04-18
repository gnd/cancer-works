# -*- coding: utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
import functions
import unicodedata

class VitalionSpider(scrapy.Spider):
    name = 'vitalion'
    curr_page = 0
    domain = 'diskuse.vitalion.cz'
    start_url = ''

    def __init__(self, maxpages=0, start_url="", delay=1.0, *args, **kwargs):
        super(VitalionSpider, self).__init__(*args, **kwargs)
        self.start_url = start_url
        self.maxpages = int(maxpages)

    def start_requests(self):
        # paging is <1, n>
        for i in range(self.maxpages):
            print "------ SCRAPING: %s/strankovani/%d" % (self.start_url, i+1)
            yield scrapy.Request("%s/strankovani/%d" % (self.start_url, i+1), callback=self.parse)

    def parse(self, response):
        texts = response.xpath('//div[@class="emojione-output"]').extract()
        names = response.xpath('//div[@class="user_in"]').extract()
        tmp_dates = response.xpath('//span[@class="date"]').extract()
        dates = []
        for date in tmp_dates:
            if ('přís' not in date):
                dates.append(date)

        for i in range(len(texts)):
            text = texts[i].encode('utf8').replace('<div class="emojione-output">\n\t\t\t\n<p>','').replace('</p>\n\n\t\t</div>','')
            text = functions.clean_text(text)
            text = functions.strip_accents(text)
            if ('komunita' in names[i]):
                name = re.sub('<[^<]+?>', '', names[i].encode('utf8').replace('<div class="user_in">\n \t \n\t\t\t<b>',''))
                name = name.split('\n')[0]
                name = functions.strip_accents(name)
            else:
                name = names[i].encode('utf8').replace('<div class="user_in">','').replace('<b>','').split('<a name=')[0].strip()
                name = functions.strip_accents(name)
            date = functions.process_date_vitalion(dates[i].encode('utf8').replace('<span class="date"><span> ','').replace('</span></span>',''))

            # add to db
            yield {
            'domain': self.domain,
            'url': self.start_url,
            'text': text,
            'date': date,
            'name': name
            }
