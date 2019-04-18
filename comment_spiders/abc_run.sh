#!/bin/bash
#
# run scrapy on abecedazdravi.cz
################################
# search keyword: rakovin
scrapy crawl abc_spider -a maxpages=36 -a start_url=http://www.abecedazdravi.cz/diskuse/zdravotni-potize-nemoci/zkusenosti-s-lecitely-u-rakoviny -L ERROR
scrapy crawl abc_spider -a maxpages=323 -a start_url=http://abecedazdravi.cz/diskuse/zdravotni-potize-nemoci/rakovina-slinivky-brisni -L ERROR
scrapy crawl abc_spider -a maxpages=7 -a start_url=http://abecedazdravi.cz/diskuse/zdravotni-potize-nemoci/rakovina-a-cervena-repa -L ERROR
scrapy crawl abc_spider -a maxpages=14 -a start_url=http://abecedazdravi.cz/diskuse/zdravotni-potize-nemoci/rakovina-mocoveho-mechyre -L ERROR
scrapy crawl abc_spider -a maxpages=9 -a start_url=http://abecedazdravi.cz/diskuse/zdravotni-potize-nemoci/rakovina-jater -L ERROR
scrapy crawl abc_spider -a maxpages=3 -a start_url=http://www.abecedazdravi.cz/diskuse/alternativni-metody-lecby/jak-na-rakovinu -L ERROR
scrapy crawl abc_spider -a maxpages=3 -a start_url=http://www.abecedazdravi.cz/diskuse/zdravotni-potize-nemoci/rakovina-strev -L ERROR
scrapy crawl abc_spider -a maxpages=5 -a start_url=http://abecedazdravi.cz/diskuse/zdravotni-potize-nemoci/masaz-prostaty-prevence-rakoviny -L ERROR
scrapy crawl abc_spider -a maxpages=3 -a start_url=http://abecedazdravi.cz/diskuse/zdravotni-potize-nemoci/rakovina-oka -L ERROR
scrapy crawl abc_spider -a maxpages=2 -a start_url=http://abecedazdravi.cz/diskuse/alternativni-metody-lecby/rakovina-7-5-2013-13-39 -L ERROR

# output everything into doktorka.in
python flush_comments.py -d abecedazdravi.cz abc.in
