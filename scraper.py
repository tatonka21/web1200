# -*- coding: utf-8 -*-
#
#    web1200 - Github and Odoo project scraper
#    Copyright (C) 2017 May
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

from config import *
import time
from bs4 import BeautifulSoup
from security import safe_requests


def do_request(url, method='', header=None):
    request_url = url + method
    r = safe_requests.get(request_url, headers=header)

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
        print("Tag %s not found on Odoo projects website" % search_tag)
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


if __name__ == '__main__':
    odoo_rst = """
Our Odoo Modules
================

:date: 2017-05-16 22:00
:modified: """ + time.strftime("%Y-%m-%d %H:%M") + """
:tags: odoo, python
:category: Odoo
:slug: our-odoo-modules
:authors: Lennart Jongeneel
:summary: Overview of our Odoo modules
:language: nl

"""
    projects = get_odoo_projects()
    count_odoo = 0
    for project in projects:
        odoo_rst += "* `%s <%s>`_ - %s\n" % (project['title'], project['link'], project['description'])
        count_odoo += 1

    if count_odoo:
        with open(DEFAULT_DOCDIR + 'odoo.rst', 'w') as f:
            f.write(odoo_rst)
        print("%d odoo projects imported" % count_odoo)

    repo_rst = """
Our Github Repositories
=======================

:date: 2017-05-16 22:06
:modified: """ + time.strftime("%Y-%m-%d %H:%M") + """
:tags: github, python, bitcoin, bitcoinlib
:category: Github
:slug: our-github-projects
:authors: Lennart Jongeneel
:summary: Overview of our projects on Github
:language: nl

"""
    repos = get_repositories()
    count_repo = 0
    for repo in repos:
        if repo['title'] and repo['link'] and repo['description']:
            repo_rst += "* `%s <%s>`_ - %s\n" % (repo['title'], repo['link'], repo['description'])
            count_repo += 1

    if count_repo:
        with open(DEFAULT_DOCDIR + 'github.rst', 'w') as f:
            f.write(repo_rst)
        print("%d links imported" % count_repo)
