from bs4 import BeautifulSoup
# from selenium import webdriver
import  csv
import requests

# browser = webdriver.Chrome("/Users/nezmi/Downloads/chromedriver") #nezmi컴에서 돌릴 때

# numPage = 8
f = open("url.csv",'r')
urls = csv.reader(f)
# f2 = open('contents.csv','w')
# w = csv.writer(f2)
f2 = open('contents.txt','w')
for i,url in enumerate(urls):
    # if i < 10 :
    #     continue
    r =requests.get(url[0])
    # print(url[0])
    soup = BeautifulSoup(r.text, "html.parser")
    try:
        lContent = soup.find_all('div',class_='content cke_editable content_')
    except:
        print(url[0])
        continue

    contents = []
    for c in lContent:
        pp = []
        wip = c.text.split("\n")
        for l in wip:
            if l == "\r":
                continue
            pp.append(l.replace('\r',''))
        contents.append(' '.join(pp))

    titles = []
    lTitle = soup.find_all('div', class_='left ')
    for t in lTitle:
        title = t.text.split("\n")
        titles.append(title[1])


    for i,c in enumerate(contents):
        for i2,t in enumerate(titles):
            if i != i2:
                continue
            print(c.replace(',',' ')+t)
            # w.writerow([t.replace(',',' ')+c.replace(',',' ')])
            f2.write(t+c+'\n')


    # soup = BeautifulSoup(r.text, "html.parser")
    # titles = soup.find_all("span", class_='td_title listTypeArticleAlias')
    # for title in titles:
    #     url = title.find('a')
    #     url = "https://www.hibrain.net/"+url.get("href")
    #     print(url)
    #     w.writerow(title.text)
f.close()
f2.close()