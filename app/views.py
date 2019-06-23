from flask import render_template
from app import app
from .request import get_news
from.request import get_sources



# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    general_news = get_news('us')
    print(general_news)
    title = 'Top Headlines'
    return render_template('index.html', name='Top Headlines', title = title,news = general_news)
@app.route('/article/')
def article():

    sources = get_sources('en')
    print(sources)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,sources = sources)