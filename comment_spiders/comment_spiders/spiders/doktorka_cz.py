# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
import MySQLdb

class DoktorkaCzSpider(scrapy.Spider):
    name = 'doktorka_cz'
    curr_page = 0
    domain = 'https://diskuse.doktorka.cz'
    start_url = ''

    def __init__(self, maxpages=0, start_url="", delay=1.0, *args, **kwargs):
        super(DoktorkaCzSpider, self).__init__(*args, **kwargs)
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
            print "------ SCRAPING: %s?page=%d" % (self.start_url, i+1)
            yield scrapy.Request("%s?page=%d" % (self.start_url, i+1), callback=self.parse)

    def parse(self, response):
        texts = response.xpath('//div[@class="field-item even"]').extract()
        names = response.xpath('//span[@class="username"]').extract()
        dates = response.xpath('//div[@class="small"]').extract()

        for i in range(len(texts)):
            text = texts[i].encode('utf8').replace('<div class="field-item even" property="content:encoded">','').replace('</div>','').replace('<br>',' ')
            name = names[i].encode('utf8').replace('<span class="username" xml:lang="" typeof="sioc:UserAccount" property="foaf:name" datatype="">','').replace('</span>','')
            date = dates[i].encode('utf8').replace('<div class="small"> ','').replace(' </div>','')

            # add to db
            yield {
            'domain': self.domain,
            'url': self.start_url,
            'text': text,
            'date': date,
            'name': name
            }
