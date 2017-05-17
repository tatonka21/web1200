# Website Generator

Scrape websites or read Github repositories and automatically create a portfolio website. 
Used to create http://1200wd.com/ but the code is easily adaptable to suit your own needs.

## Install
Requires pip installer and virtualenv
```bash
$ sudo apt-get install python-pip
$ pip install virtualenv
```

Run setup file to create a virtual environment and install pelican, requests and Beautiful Soup (bs4) 
```bash
$ setup.py
```


## Usage

Generate content in 'content' directory with

 pelican content
 
To update website run scraper.py or add scraper.py to cron.
