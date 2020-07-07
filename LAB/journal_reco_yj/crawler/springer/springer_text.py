from bs4 import BeautifulSoup
import requests
import csv
from html.parser import HTMLParser
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='imlab506',
                             db='wb_db',
                             charset='utf8')
cursor = connection.cursor()


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def open_url(url):
    if url=='':
        return -1
    r = requests.get(url)
    soup1 = BeautifulSoup(r.text, "html.parser")
    return soup1

def bring_page(url):
    r = requests.get(url)
    soup1 = BeautifulSoup(r.text, "html.parser")
    link=[]
    journals = soup1.find_all("a", class_="title")
    for i in journals:
        link.append(i.get('href'))

    articles_page=[]
    for i in link:
        url = "https://link.springer.com" + i
        r = requests.get(url)
        soup2 = BeautifulSoup(r.text, "html.parser")
        articles_all = soup2.find_all("div", class_="show-all")
        for i in articles_all:
            articles = i.find("a").get('href')
            articles_page.append(articles)

    article_page=[]
    for i in articles_page:
        apage_num = 1
        id = i.split("=")[-1]
        while apage_num < 2:
            url = "https://link.springer.com/search/page/"+str(apage_num)+"?facet-content-type=Article&facet-journal-id="+id+"&sortOrder=newestFirst"
            r = requests.get(url)
            soup3 = BeautifulSoup(r.text, "html.parser")
            article_all = soup3.find_all("a", class_="title")
            apage_num += 1
            for i in article_all:
                article = i.get("href")
                article_page.append(article)

    return article_page

def bring_text(url):
    dic = {}
    html_text = open_url(url)
    abstract = str(html_text.find('section', class_='Abstract')).replace('Abstract', 'Abstract ').replace('Background',
                                                                                                          'Background ').replace(
        'Aims', 'Aims ').replace('Methods', 'Methods ').replace('Results', 'Results ').replace('Conclusions',
                                                                                               'Conclusions ')
    title = getTitle(url)
    keywords = getKeywords(url)
    history = getHistory(url)
    abstract = strip_tags(abstract)
    if title == None:
        dic["title"] = "None"
    else:
        dic.update(title)
    if keywords == None:
        dic["keywords"] = "None"
    else:
        dic.update(keywords)
    if history == None:
        dic["history"] = "None"
    else:
        dic.update(history)

    dic["abstract"] = strip_tags(abstract)

    return dic

def getTitle(url):
    r = requests.get(url)
    bsObj = BeautifulSoup(r.text, "html.parser")
    jtitle_tag = bsObj.find("img", class_="test-cover-image")
    atitle_tag = bsObj.find("meta", property="og:title")
    if jtitle_tag != None:
        jtitle = jtitle_tag.get("alt")
    if atitle_tag != None:
        atitle = atitle_tag.get("content")
    return [jtitle, atitle]

def getKeywords(url):
    combined_keywords = []
    r = requests.get(url)
    bsObj = BeautifulSoup(r.text, "html.parser")
    keywords = bsObj.find_all("span", class_="Keyword")
    for key in keywords:
        if key == None:
            continue
        combined_keywords.append(key.string)
    return combined_keywords

def getHistory(url):
    history = []
    r = requests.get(url)
    bsObj = BeautifulSoup(r.text, "html.parser")
    timedata = bsObj.find_all("time")
    for i in timedata:
        history.append(i.get("datetime"))
    return history

def csv_writer(dic, param):
    f = open(param, 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    for key,value in dic.items():
        wr.writerow([key,value])
    f.close()


    pass


#1-173
jpage_num = 1
while jpage_num <= 2 :
    spage = str(jpage_num)
    journals_page = 'https://link.springer.com/search/page/%s?facet-content-type="Journal"' %spage
    articles_link = bring_page(journals_page)
    #a=1
    for i in articles_link:
        url = "https://link.springer.com"+i
        bring_text(url)
        #a+=1
        #if a>3:
        #    break
    jpage_num += 1