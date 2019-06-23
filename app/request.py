from app import app
import urllib.request,json
from .models import news
from .models import sources
News = news.News
Sources = sources.Sources

# Getting api key
apiKey = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]
source_url = app.config["SOURCES_API_BASE_URL"]
def get_news(country):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(country,apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results
def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt= news_item.get('publishedAt')
        content = news_item.get('content')
        

        if urlToImage:
            news_object = News(id,name,author,title,description,url,urlToImage,publishedAt,content)
            news_results.append(news_object)

    return news_results
def get_sources(language):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = source_url.format(language,apiKey)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_source(source_results_list)
    
    return source_results
    

def process_source(source_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    source_results = []
    for source in source_list:
        
        id = source.get('id')
        sname = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        language = source.get('language')
        country = source.get('country')


        if url:
            source_object = Sources(id,name,description,url,category,language,country)
            source_results.append(source_object)

    return source_results
