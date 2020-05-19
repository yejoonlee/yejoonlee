# host: str
# user: str
# password: str
# db: str
#
# DB에 접근하여 컨트롤할 수 있는 cursor를 만들어주는 함수.
# 어렵지 않아서 굳이 함수로 만들필요가 없긴한데 매번 여러줄 쓰는게 귀찮아서 그냥 만듦
# cursor의 사용법은 구글링으로 알아보기

def get_connection(host,user,password,db):
    import pymysql.cursors
    connection = pymysql.connect(host='%s'%host,
                                 user='%s'%user,
                                 password='%s'%password,
                                 db='%s'%db)
    return connection

# driver: selenium driver
# inputbox_path: str
# keyword: str
# switch: 0 or 1
#
# selenium을 사용하여 크롤링할 때 inoutbox에 키워드를 입력해 검색하는 함수.
# selenium driver는 먼저 만들어서 입력해주어야 함
# inputbox_path도 해당 페이지마다 다르므로 페이지검사를 하여 xpath를 입력
# keyword는 여러개일 경우가 많으니 for문으로 리스트 돌려가면서 입력
#
def search(driver,inputbox_path,keyword,switch):
    inputbox = driver.find_element_by_xpath(inputbox_path)
    inputbox.send_keys(keyword)
    if switch == 0:
        return
    inputbox.submit()
    return



