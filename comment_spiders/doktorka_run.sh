#!/bin/bash
#
# run scrapy on doktorka.cz
###########################
scrapy crawl doktorka_cz -a maxpages=12 -a start_url=https://diskuse.doktorka.cz/zase-rakovina
scrapy crawl doktorka_cz -a maxpages=10 -a start_url=https://diskuse.doktorka.cz/rakovina-slinivky
scrapy crawl doktorka_cz -a maxpages=6 -a start_url=https://diskuse.doktorka.cz/rakovina-mam-rok-zivota
scrapy crawl doktorka_cz -a maxpages=3 -a start_url=https://diskuse.doktorka.cz/rakovina-delohy
scrapy crawl doktorka_cz -a maxpages=4 -a start_url=https://diskuse.doktorka.cz/rakovina-krku
scrapy crawl doktorka_cz -a maxpages=17 -a start_url=https://diskuse.doktorka.cz/rakovina-konecniku
scrapy crawl doktorka_cz -a maxpages=4 -a start_url=https://diskuse.doktorka.cz/rakovina-plic/43506
scrapy crawl doktorka_cz -a maxpages=23 -a start_url=https://diskuse.doktorka.cz/rakovina-delozniho-cipku
scrapy crawl doktorka_cz -a maxpages=15 -a start_url=https://diskuse.doktorka.cz/rakovina-varlat
scrapy crawl doktorka_cz -a maxpages=22 -a start_url=https://diskuse.doktorka.cz/rakovina-jater
scrapy crawl doktorka_cz -a maxpages=18 -a start_url=https://diskuse.doktorka.cz/rakovina-prsu/36324
scrapy crawl doktorka_cz -a maxpages=8 -a start_url=https://diskuse.doktorka.cz/rakovina

# output everything into doktorka.in
python flush_comments.py 'https://diskuse.doktorka.cz' doktorka.in
