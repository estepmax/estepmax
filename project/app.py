import sys,markdown,pygments,time

import os

from flask import Flask, render_template_string
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)

REPO_NAME = ""  # Used for FREEZER_BASE_URL
DEBUG = True

APP_DIR = os.path.dirname(os.path.abspath(__file__))

def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(APP_DIR)

def renderer(text):
	rendered_body = render_template_string(text)
	pygmented_body = markdown.markdown(rendered_body,extensions=['codehilite','fenced_code'])
	return pygmented_body

app.config.update({
	'FLATPAGES_EXTENSION':['.md','.markdown'],
	'FLATPAGES_MARKDOWN_EXTENSIONS':['codehilite','fenced_code'],
	'FLATPAGES_HTML_RENDERER': renderer,
	'FREEZER_DESTINATION':PROJECT_ROOT,
	'FREEZER_BASE_URL':"http://localhost/{0}".format(REPO_NAME),
	'FREEZER_REMOVE_EXTRA_FILES': False,
	'FLATPAGES_ROOT': os.path.join(APP_DIR, 'pages')
})

pages = FlatPages(app)
freezer = Freezer(app)
