#!/usr/bin/env bash

# Create virtual environment
virtualenv ~/.virtualenv/web1200

# Install required python modules
~/.virtualenv/web1200/bin/pip install pelican markdown beautifulsoup4 requests
