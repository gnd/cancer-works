#!/bin/bash
#
# run scrapy on vitalion.cz
###########################
# search keyword: rakovin
scrapy crawl vitalion -a maxpages=1 -a start_url=https://diskuse.vitalion.cz/rakovina-dutiny-ustni-701
scrapy crawl vitalion -a maxpages=2 -a start_url=https://diskuse.vitalion.cz/71
scrapy crawl vitalion -a maxpages=2 -a start_url=https://diskuse.vitalion.cz/72
scrapy crawl vitalion -a maxpages=3 -a start_url=https://diskuse.vitalion.cz/74
scrapy crawl vitalion -a maxpages=3 -a start_url=https://diskuse.vitalion.cz/75
scrapy crawl vitalion -a maxpages=3 -a start_url=https://diskuse.vitalion.cz/223
scrapy crawl vitalion -a maxpages=1 -a start_url=https://diskuse.vitalion.cz/224
scrapy crawl vitalion -a maxpages=3 -a start_url=https://diskuse.vitalion.cz/rakovina-delozniho-cipku-407
# search keyword: nador
scrapy crawl vitalion -a maxpages=4 -a start_url=https://diskuse.vitalion.cz/operace-nadoru-na-mozku-836
scrapy crawl vitalion -a maxpages=1 -a start_url=https://diskuse.vitalion.cz/54
# rest
scrapy crawl vitalion -a maxpages=2 -a start_url=https://diskuse.vitalion.cz/bulka-na-prirozeni-585
scrapy crawl vitalion -a maxpages=5 -a start_url=https://diskuse.vitalion.cz/bulka-na-prsu-295

# output everything into doktorka.in
python flush_comments.py 'diskuse.vitalion.cz' vitalion.in
