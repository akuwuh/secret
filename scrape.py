from requests_html import HTMLSession

session = HTMLSession()

url = 'https://uwflow.com/explore'

class Data:
    def __init__(self, course, name, ratings, useful, easy, liked):
        self.course = course
        self.name = name
        self.ratings = ratings
        self.useful = useful
        self.easy = easy
        self.liked = liked

def 
r = session.get(url)

r.html.render(sleep=1, keep_page=True, scrolldown=1) #654

rows = r.html.find("div[role='row']")

rows.pop(0)

for i, item in enumerate(rows):
    cells = item.find("div[role='cell']") #array of each cells
    data = {
        
    }