#!/bin/bash
#
# run scrapy on abecedazdravi.cz
################################
scrapy crawl abc_spider -a maxpages=322 -a start_url=http://abecedazdravi.cz/diskuse/zdravotni-potize-nemoci/rakovina-slinivky-brisni
scrapy crawl abc_spider -a maxpages=2 -a start_url=http://abecedazdravi.cz/diskuse/alternativni-metody-lecby/rakovina-7-5-2013-13-39
scrapy crawl abc_spider -a maxpages=8 -a start_url=http://abecedazdravi.cz/diskuse/zdravotni-potize-nemoci/rakovina-jater
scrapy crawl abc_spider -a maxpages=13 -a start_url=http://abecedazdravi.cz/diskuse/zdravotni-potize-nemoci/rakovina-mocoveho-mechyre

# output everything into doktorka.in
python flush_comments.py 'http://www.abecedazdravi.cz/diskuse' abc.in
