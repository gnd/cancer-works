## About
This is a collection of web spiders written in Scrapy that collects data from cancer-related discussions on several Czech health and medical forums.
The forums are:
    - diskuse.doktorka.cz
    - abecedazdravi.cz/diskuse
    - diskuse.vitalion.cz

## Usage
1. Install scrapy and requirements
2. Install and/or start mysql server, and create a table for data. The table structure can be found in pipelines.py
3. Copy settings_python.orig to setting_python and add mysql credentials
4. Run the bash scripts in the main folder:
    - doktorka_run.sh
    - abc_run.sh
    - vitalion_run.sk
5. Use flush_comments.py to extract all the comments into one file (usage: `python flush_comments <domain> <outfile>` where domain is one of (diskuse.doktorka.cz, abecedazdravi.cz, diskuse.vitalion.cz))

## Notes
In functions.py currently only a few functions are found for some kind of low-level input regularisation. These could be extended.
