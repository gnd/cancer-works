# -*- coding: utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
import functions
import unicodedata

class EmiminoSpider(scrapy.Spider):
    name = 'emimino'
    curr_page = 0
    domain = 'emimino.cz'
    start_url = ''

    def __init__(self, maxpages=0, start_url="", delay=1.0, *args, **kwargs):
        super(EmiminoSpider, self).__init__(*args, **kwargs)
        self.start_url = start_url
        self.maxpages = int(maxpages)

    def start_requests(self):
        for i in range(self.maxpages):
            print "------ SCRAPING: %sstrankovani/%d/" % (self.start_url, i+1)
            yield scrapy.Request("%sstrankovani/%d/" % (self.start_url, i+1), callback=self.parse)

    def parse(self, response):
        texts = response.xpath('//div[@class="emojione-output"]').extract()
        names = response.xpath('//div[@class="user_in"]/b').extract()
        dates = response.xpath('//div[@class="user_in"]//span[@class="date"]/span/text()').extract()

        for i in range(len(texts)):
            text = re.sub('<blockquote>.*?<\/blockquote>', '', texts[i], flags=re.DOTALL)
            text = functions.strip_accents(text.strip())
            text = functions.clean_text(text)
            name = re.sub('<[^<]+?>', '', names[i])
            name = functions.strip_accents(name)
            date = functions.process_date_emimino(dates[i].strip().split()[0])

            # add to db
            yield {
            'domain': self.domain,
            'url': self.start_url,
            'text': text,
            'date': date,
            'name': name
            }
