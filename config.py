# -*- coding: utf-8 -*-
#
#    web1200 - Github and Odoo project scraper
#    (C) 2017 May by 1200 Web Development <http://1200wd.com/>

import os

# Website settings
WEBSITE_DIR = '/home/lennart/code/web1200/'
DEFAULT_DOCDIR = WEBSITE_DIR + 'content/generated/'
if not os.path.exists(DEFAULT_DOCDIR):
    os.makedirs(DEFAULT_DOCDIR)

# Python virtual environment settings
VIRTUALENV = '/home/lennart/.virtualenvs/web1200/'

# Scrape Github projects settings
GITHUB_URL = 'https://api.github.com'
VALID_TYPES = ['all', 'owner', 'public', 'private', 'member']
EXCLUDE_REPOS = ['project_category', '1200wd.github.io', 'odoo_toolbox_1200', '1200wd_addons', 'ListLongNew']

# Scrape Odoo store projects settings
ODOOBASE_URL = 'https://www.odoo.com'
ODOO1200APPS_URL = ODOOBASE_URL + '/apps/modules/browse?author=1200%20Web%20Development'

