#!/usr/bin/env bash

# Create virtual environment
virtualenv ~/.virtualenv/web1200

# Install required python modules
~/.virtualenv/web1200/bin/pip install flask
~/.virtualenv/web1200/bin/pip install requests
~/.virtualenv/web1200/bin/pip install bs4
