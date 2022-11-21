import time
import requests
import json
from bs4 import BeautifulSoup

title = "martial"
url = "https://light-novelpub.com/ajax/search-novel?keyword="+title
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
bodyContainer = soup.find("body")
titles = []
links = []
jsonList = []
output = "[\n"

for i in soup.find_all('a'):
    links.append(i.get('href'))


for item in bodyContainer:
    if item != "\n":
        titles.append(item.text)

for i, j in zip(titles, links):
    
    Dictionary={"Novel":i.strip(), "Link":j.strip()}
    json_string = json.dumps(Dictionary)
    #print(json_string)
    jsonList.append(json_string)               


print(jsonList)