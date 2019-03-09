from flask import render_template
from .app import app,pages
import datetime

@app.route('/')
def index():
	articles = [p for p in pages]
	latest = sorted(articles,reverse=True,key= lambda p: p.meta['date'])
	return render_template('index.html',pages=latest)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.template_filter('dt')
def datetime_filter(date):
	return date.strftime('%B %d %Y')
	
