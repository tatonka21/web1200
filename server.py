#!/usr/bin/python

import os
from flask import Flask, render_template
import sqlite3
from contextlib import closing

from scraper import get_repositories, get_odoo_projects


app = Flask(__name__)
PRODUCTION = True

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'web1200.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)



def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    with closing(connect_db()) as db:
        # Import projects from GitHub
        repos = get_repositories()
        sql_repo_import = ""
        count_repo_start = 100
        count_repo = count_repo_start
        for repo in repos:
            sql_repo_import += "insert into links values (%d, 1, '%s', '%s', '%s');\n" % (count_repo, repo['title'], repo['link'], repo['description'])
            count_repo += 1

        # Import Odoo project
        projects = get_odoo_projects()
        sql_odoo_import = ""
        count_odoo_start = 200
        count_odoo = count_odoo_start
        for project in projects:
            sql_odoo_import += "insert into links values (%d, 2, '%s', '%s', '%s');\n" % (count_odoo, project['title'], project['link'], project['description'])
            count_odoo += 1

        if count_repo > count_repo_start and count_odoo > count_odoo_start:
            with app.open_resource('schema.sql', mode='r') as f:
                db.cursor().executescript(f.read())
            db.commit()
            print "Database initialized"

            db.cursor().executescript(sql_repo_import)
            db.commit()
            print "%d links imported" % (count_repo - count_repo_start)

            db.cursor().executescript(sql_odoo_import)
            db.commit()
            print "%d odoo projects imported" % (count_odoo - count_odoo_start)
        else:
            print "Empty list or error when processing import. Database not updated!"


@app.route('/')
def show_entries():
    db = connect_db()
    groups = db.execute('select id, title, text from linkgroup order by id asc').fetchall()
    links = db.execute('select linkgroupid, id, title, link, description from links order by id asc').fetchall()
    page = render_template('show_entries.html', groups=groups, links=links)
    if PRODUCTION:
        if page:
            f = open(os.path.join(app.root_path, 'public/index.html'), 'w')
            f.write(page)
    return page



if __name__ == '__main__':

    app.run()
