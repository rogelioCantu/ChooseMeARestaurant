import requests
from bs4 import BeautifulSoup

def parse(url):
    found = [];
    i = 0;
    req = requests.get(url)
    parsed = BeautifulSoup(req.content, "html.parser")
    for el in parsed.find_all(class_="list-view-item"):
        inside = []
        el = el.get_text().strip()
        el = el.replace("\n", " ")
        inside.append(el)
        found.append(inside)
      
    #found = parsed.find_all(class_="artist-info").get_text()
    #print(found)
    return found

def main():
    all_parsed = []
    x = 0
    urlList = ["https://thefillmore.com/calendar/", 
               "http://www.bottomofthehill.com/calendar.html#sthash.SjLaNJKm.dpbs",
               "https://slimspresents.com/great-american-music-hall/"]
    for i in urlList:
        all_parsed.append(parse(i))
    for z in all_parsed:
        print(z)
main()