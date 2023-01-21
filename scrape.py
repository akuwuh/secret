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

    def print(self, counter):
        print("#" + str(counter + 1))
        print("Course: " + str(self.course))
        print("Name: " + str(self.name))
        print("Ratings: " + str(self.ratings))
        print("Useful: " + str(self.useful))
        print("Easy: " + str(self.easy))
        print("Liked: " + str(self.liked))


def scrape():
    r = session.get(url)
    r.html.render(sleep=1, keep_page=True, scrolldown=114) #654

    rows = r.html.find("div[role='row']")

    rows.pop(0)
    return rows

def print_data(rows):
    for i, item in enumerate(rows):
        cells = item.find("div[role='cell']") #array of each cells
        data = Data(cells[0].text, cells[1].text, int(cells[2].text), int(cells[3].text[:-1]), int(cells[4].text[:-1]), int(cells[5].text[:-1]))

        data.print(i)
        print()
        

if __name__ == '__main__':
    print("Scraping..")
    rows = scrape()

    print_data(rows)