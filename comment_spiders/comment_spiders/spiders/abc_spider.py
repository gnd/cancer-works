# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
import functions
import unicodedata

class AbcSpider(scrapy.Spider):
    name = 'abc_spider'
    curr_page = 1
    domain = 'abecedazdravi.cz'
    start_url = ''

    def __init__(self, maxpages=0, start_url='', delay=1.0, *args, **kwargs):
        super(AbcSpider, self).__init__(*args, **kwargs)
        self.start_url = start_url
        self.maxpages = int(maxpages)

    def start_requests(self):
        # paging starts with page 1 here (unlike as in doktorka)
        for i in range(1, self.maxpages):
            print "------ SCRAPING: %s/%d" % (self.start_url, i)
            yield scrapy.Request("%s/%d" % (self.start_url, i), callback=self.parse)

    def parse(self, response):
        texts = response.xpath('//div[@class="diskuse-prispevek"]//div[@class="popis"]').extract()
        names = response.xpath('//div[@class="diskuse-prispevek"]//span[@class="jmeno"]').extract()
        dates = response.xpath('//div[@class="diskuse-prispevek"]//span[@class="datum"]').extract()

        for i in range(len(texts)):
            text = texts[i].encode('utf8').replace('<div class="popis">','').replace('</div>','')
            text = functions.clean_text(text)
            text = functions.strip_accents(text)
            name = names[i].encode('utf8').replace('<span class="jmeno">','').replace('</span>','')
            date = dates[i].encode('utf8').replace('<span class="datum">','').replace('</span>','').strip(',').strip().split()[0]
            date = functions.process_date_abc(date)

            # add to db
            yield {
            'domain': self.domain,
            'url': self.start_url,
            'text': text,
            'date': date,
            'name': name
            }
