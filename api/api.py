import time
import requests
import json
from bs4 import BeautifulSoup
from flask import Flask, request

app = Flask(__name__)


@app.route('/test')
def getChapterList():
    url = "https://light-novelpub.com/ajax/chapter-archive?novelId=the-beginning-after-the-end"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    chapContainer = soup.find("div", class_="panel-body")
    chapters = []
    for row in chapContainer:
        if row != "\n":
            for col in row:
                if col != "\n":
                    for li in col.contents[1]:
                        if li != "\n":
                            chapters.append(li.text.strip())
    return json.dumps(chapters)


@app.route('/test2')
def getChapter10():
    url = "https://light-novelpub.com/lightnovelpub/the-beginning-after-the-end/chapter-2"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.find(id="chr-content")
    return text.text

def get_current_time():
    return {'time': time.time()}


@app.route('/search')
def getNovel():
    title = request.args.get('title')
    url = "https://light-novelpub.com/ajax/search-novel?keyword="+title

    searchResults = "https://light-novelpub.com/ajax/search-novel?keyword="

    return '''<h1>The language value is: {}</h1>'''.format(title)
