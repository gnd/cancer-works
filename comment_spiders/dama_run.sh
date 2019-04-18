#!/bin/bash
#
# run scrapy on dama.cz
###########################
# search keyword: rakovina
scrapy crawl dama_cz -a maxpages=6 -a start_url=http://diskuse.dama.cz/diskuse.php?d=15995
scrapy crawl dama_cz -a maxpages=17 -a start_url=http://diskuse.dama.cz/diskuse.php?d=9264
scrapy crawl dama_cz -a maxpages=3 -a start_url=http://diskuse.dama.cz/diskuse.php?d=12602
scrapy crawl dama_cz -a maxpages=4 -a start_url=http://diskuse.dama.cz/clanek.php?diskuse=3749
scrapy crawl dama_cz -a maxpages=5 -a start_url=http://diskuse.dama.cz/diskuse.php?d=20376

# output everything into doktorka.in
python flush_comments.py 'diskuse.dama.cz' dama.in
