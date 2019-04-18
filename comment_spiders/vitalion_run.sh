#!/bin/bash
#
# run scrapy on vitalion.cz
###########################
# search keyword: rakovin
scrapy crawl vitalion -a maxpages=1 -a start_url=https://diskuse.vitalion.cz/rakovina-dutiny-ustni-701 -L ERROR
scrapy crawl vitalion -a maxpages=2 -a start_url=https://diskuse.vitalion.cz/71 -L ERROR
scrapy crawl vitalion -a maxpages=2 -a start_url=https://diskuse.vitalion.cz/72 -L ERROR
scrapy crawl vitalion -a maxpages=3 -a start_url=https://diskuse.vitalion.cz/74 -L ERROR
scrapy crawl vitalion -a maxpages=3 -a start_url=https://diskuse.vitalion.cz/75 -L ERROR
scrapy crawl vitalion -a maxpages=3 -a start_url=https://diskuse.vitalion.cz/223 -L ERROR
scrapy crawl vitalion -a maxpages=1 -a start_url=https://diskuse.vitalion.cz/224 -L ERROR
scrapy crawl vitalion -a maxpages=3 -a start_url=https://diskuse.vitalion.cz/rakovina-delozniho-cipku-407 -L ERROR
# search keyword: nador
scrapy crawl vitalion -a maxpages=4 -a start_url=https://diskuse.vitalion.cz/operace-nadoru-na-mozku-836 -L ERROR
scrapy crawl vitalion -a maxpages=1 -a start_url=https://diskuse.vitalion.cz/54 -L ERROR
# rest
scrapy crawl vitalion -a maxpages=2 -a start_url=https://diskuse.vitalion.cz/bulka-na-prirozeni-585 -L ERROR
scrapy crawl vitalion -a maxpages=5 -a start_url=https://diskuse.vitalion.cz/bulka-na-prsu-295 -L ERROR

# output everything into doktorka.in
python flush_comments.py 'diskuse.vitalion.cz' vitalion.in
