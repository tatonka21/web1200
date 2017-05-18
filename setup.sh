#!/usr/bin/env bash

# Create virtual environment
virtualenv ~/.virtualenvs/web1200

# Install required python modules
~/.virtualenvs/web1200/bin/pip install pelican markdown beautifulsoup4 requests
