#!/bin/bash
#
# run scrapy on doktorka.cz
###########################
scrapy crawl vitalion -a maxpages=3 -a start_url=https://diskuse.vitalion.cz/74/
scrapy crawl vitalion -a maxpages=2 -a start_url=https://diskuse.vitalion.cz/bulka-na-prirozeni-585/
scrapy crawl vitalion -a maxpages=5 -a start_url=https://diskuse.vitalion.cz/bulka-na-prsu-295/
scrapy crawl vitalion -a maxpages=1 -a start_url=https://diskuse.vitalion.cz/54/

# output everything into doktorka.in
python flush_comments.py 'diskuse.vitalion.cz' vitalion.in
