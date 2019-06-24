import unittest
from models import news
News = news.News
class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("cbs-news","CBS News","Tre'Vaughn Howard",
       "Oregon Republicans go missing and Gov. Kate Brown sends police to find them - CBS News",
       "Officers can arrest the lawmakers if they refuse to willfully return and will each be fined $500 a day if they don't return Friday morning",
       "https://www.cbsnews.com/news/oregon-republicans-go-missing-to-avoid-climate-change-vote-governor-sends-police-after-them/",
       "https://cbsnews2.cbsistatic.com/hub/i/r/2019/06/21/b1e25913-9513-4da1-ba66-6b13461a6822/thumbnail/1200x630/37529e71d8d1c502567aa3e997c57bfb/oregon-republicans-walk-out-climate-change-vote.png",
       "2019-06-21T02:33:00Z",
       "Republicans in Oregon's state government have gone missing — and the governor is sending police to go find them. Gov. Kate Brown dispatched Oregon State Police to search for 11 Senate Republicans who walked off the job to avoid a vote for a climate change bil… [+1939 chars]"
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()
