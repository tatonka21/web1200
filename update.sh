#!/usr/bin/env bash

WEBSITEDIR='/home/lennart/code/web1200'

source ~/.virtualenvs/web1200/bin/activate

/usr/bin/python $WEBSITEDIR/scraper.py

cd $WEBSITEDIR

pelican content

