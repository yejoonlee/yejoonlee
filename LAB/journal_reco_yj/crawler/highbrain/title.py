from bs4 import BeautifulSoup
# from selenium import webdriver
import  csv
import requests

# browser = webdriver.Chrome("/Users/nezmi/Downloads/chromedriver") #nezmi컴에서 돌릴 때

# numPage = 8
f = open("url.csv",'w')
w = csv.writer(f)
for numPage in range(32):
    if numPage == 0 :
        continue
    r =requests.get("https://www.hibrain.net/braincafe/cafes/40/posts/103/articles?pagenav=FIRST&pagekey=000338466992&page=%d&pagingno=1&pagingkey=900000007999&listType=TOTAL&pagesize=10&sortType=RDT&limit=25&displayType=QNA&siteid=1"%numPage)
    soup = BeautifulSoup(r.text, "html.parser")
    titles = soup.find_all("span", class_='td_title listTypeArticleAlias')
    for title in titles:
        url = title.find('a')
        url = ["https://www.hibrain.net/"+url.get("href")]
        cut = url[0].split("/")
        try:
            if cut[11] == "replies":
                print(cut[11])
                continue
        except:
            print(url)
        w.writerow(url)
f.close()
