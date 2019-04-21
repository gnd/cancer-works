# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
import functions
import unicodedata

class DoktorkaCzSpider(scrapy.Spider):
    name = 'doktorka_cz'
    curr_page = 0
    domain = 'diskuse.doktorka.cz'
    start_url = ''

    def __init__(self, maxpages=0, start_url="", delay=1.0, *args, **kwargs):
        super(DoktorkaCzSpider, self).__init__(*args, **kwargs)
        self.start_url = start_url
        self.maxpages = int(maxpages)

    def start_requests(self):
        for i in range(self.maxpages):
            print "------ SCRAPING: %s?page=%d" % (self.start_url, i)
            yield scrapy.Request("%s?page=%d" % (self.start_url, i), callback=self.parse)

    def parse(self, response):
        texts = response.xpath('//div[@class="field-item even"]').extract()
        names = response.xpath('//span[@class="username"]').extract()
        dates = response.xpath('//div[@class="small"]').extract()

        for i in range(len(texts)):
            if ('Isaac Asimov' not in texts[i].encode('utf8')):
                text = texts[i].encode('utf8').replace('<div class="field-item even" property="content:encoded">','').replace('</div>','')
                text = functions.strip_accents(text)
                text = functions.clean_text(text)
                text = text.strip("'")
                name = names[i].encode('utf8').replace('<span class="username" xml:lang="" typeof="sioc:UserAccount" property="foaf:name" datatype="">','').replace('</span>','')
                name = functions.strip_accents(name)
                date = dates[i].encode('utf8').replace('<div class="small"> ','').replace(' </div>','')
                date = functions.process_date_doktorka(date)

            # add to db
            yield {
            'domain': self.domain,
            'url': self.start_url,
            'text': text,
            'date': date,
            'name': name
            }
