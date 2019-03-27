# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# create table comments(id int(11) primary key auto_increment, domain varchar(255), url varchar(255), text blob, name varchar(255), date varchar(255));
import MySQLdb

class CommentSpidersPipeline(object):
    def __init__(self):
        self.dbhost = "localhost"
        self.dbname = "cnc_comments"
        self.dbuser = "cnc_user"
        self.dbpass = "cnc_pass"

    def open_spider(self, spider):
        self.db = MySQLdb.connect(host=self.dbhost, user=self.dbuser, passwd=self.dbpass, db=self.dbname)
        self.cur = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        query = "INSERT INTO comments (domain, url, text, name, date) VALUES('%s', '%s', '%s', '%s', '%s')" % (item["domain"], item["url"], item["text"], item["name"], item["date"])
        self.cur.execute(query)
        self.db.commit()
        return item
