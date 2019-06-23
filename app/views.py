from flask import render_template
from app import app
from .request import get_news



# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    general_news = get_news('us')
    print(general_news)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,general = general_news)
@app.route('/article/<int:article_id>')
def article(article_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('article.html',id = article_id)