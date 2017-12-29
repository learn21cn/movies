import webbrowser

class Movie():
    '''This is a class which can store movies information '''
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youku):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_url = trailer_youku

    def show_trailer(self):
        webbrowser.open(self.trailer_url) 

# self 并不是 python 关键字。我们之前错误地称之为关键字。如果你将 media.py 文件中的所有单词“self”改成另一个单词，例如“udacity”，代码依然能运行