# -*- coding: utf-8 -*-
#
#    web1200 github.py
#    Copyright (C) 2016 March 
#    1200 Web Development
#    http://1200wd.com/
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import requests
from bs4 import BeautifulSoup


GITHUB_URL = 'https://api.github.com'
VALID_TYPES = ['all', 'owner', 'public', 'private', 'member']
EXCLUDE_REPOS = ['project_category', '1200wd.github.io', 'odoo_toolbox_1200']

ODOOBASE_URL = 'https://www.odoo.com'
ODOO1200APPS_URL = ODOOBASE_URL + '/apps/modules/browse?author=1200%20Web%20Development'


def do_request(url, method='', header=None):
    request_url = url + method
    r = requests.get(request_url, headers=header)

    if not r or not r.status_code==200:
        raise RuntimeError("Connection error when connecting to %s. Response: %s" % (url, getattr(r, 'text', 'Unknown Response')))
    else:
        return r


def get_repositories():
    r = do_request(GITHUB_URL, '/orgs/1200wd/repos').json()
    repositories = []

    for repo in r:
        if not (repo['fork'] or repo['private']) and repo['name'] not in EXCLUDE_REPOS:
            repositories.append({
                'title': repo.get('name') or '',
                'link': repo.get('html_url') or '',
                'language': repo.get('language') or '',
                'pushed_at': repo.get('pushed_at') or '',
                'description': repo.get('description') or '',
            })

    repositories = sorted(repositories, key=lambda k: k['pushed_at'], reverse=True)
    return repositories


def get_odoo_projects():
    html_doc = do_request(ODOO1200APPS_URL).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    projects = []

    search_tag = "loempia_panel_short_desc"
    tags = soup.find_all('p', class_=search_tag)
    if not tags:
        print "Tag %s not found on Odoo projects website" % search_tag
    for tag in tags:
        title = tag.text.strip()
        link = ODOOBASE_URL + tag.parent.parent['href']
        description = tag.parent.parent.find_all('p')[0].text.strip()

        projects.append({
            'title': title,
            'link': link,
            'language': 'python',
            'pushed_at': '',
            'description': description,
        })

    return projects
