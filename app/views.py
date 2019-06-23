from flask import render_template
from app import app
from .request import get_news
from .request import get_sources
from .request import get_articles 



# Views
@app.route('/index')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    general_news = get_news('us')
    print(general_news)
    title = 'Top Headlines'
    return render_template('index.html', name='Top Headlines', title = title,news = general_news)
@app.route('/')
def article():

    sources = get_sources('en')
    
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('article.html', title = title,sources = sources)
@app.route('/sources/<source_id>&<int:per_page>')
def articles(source_id,per_page):
    '''
    Function that returns articles based on their sources
    '''
    # print(source_id)
    # per_page = 40
    news_source = get_articles(source_id,per_page)
    title = f'{source_id} | All Articles'
    return render_template('sources.html', title = title, name = source_id, news = news_source)
