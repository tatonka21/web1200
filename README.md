# Website Generator

Scrape websites or read Github repositories and automatically create a portfolio website. 
Used to create http://1200wd.com/ but the code is easily adaptable to suit your own needs.

## Install
Requires pip installer and virtualenv
```bash
$ sudo apt-get install python-pip
$ pip install virtualenv
```

Run setup file to create a virtual environment and install Flask, requests and Beautiful Soup (bs4) 
```bash
$ setup.py
```

In a production environment you can use the wsgi file to run the script throught an Apache server.
The built in server from Flask is not recommended for use in a production environment.

To update website run refresh.py or add refresh.py to cron.
