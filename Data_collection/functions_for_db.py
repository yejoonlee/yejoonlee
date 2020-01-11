# host: str
# user: str
# password: str
# db: str
#
# DB에 접근하여 컨트롤할 수 있는 cursor를 만들어주는 함수.
# 어렵지 않아서 굳이 함수로 만들필요가 없긴한데 매번 여러줄 쓰는게 귀찮아서 그냥 만듦
# cursor의 사용법은 구글링으로 알아보기
#
def get_connection(host,user,password,db):
    import pymysql.cursors
    connection = pymysql.connect(host='%s'%host,
                                 user='%s'%user,
                                 password='%s'%password,
                                 db='%s'%db,
                                 use_unicode=True)
    return connection

# connection: sql connection
# s_table: str
# d_table: str
# data_name1: str
# s_key: str
# d_key: str
#
# db에서 이쪽 테이블의 데이터를 저쪽 테이블로 옮길때 사용
# 데이터 여러개를 옮기게 할수도 있는데 필요한 사람이 수정해서 쓰면될듯..

def data_move(connection, s_table, d_table, s_data_name,d_data_name, s_key,d_key):
    print('Maybe takes some time..')
    cursor = connection.cursor()
    cursor.execute("select %s, %s from %s where %s is not null"%(s_key,s_data_name,s_table,s_data_name))
    data = cursor.fetchall()
    data_num = len(list(data))
    print("%d of data will move"%data_num)

    cursor.execute("select %s from %s"%(d_key,d_table))
    keys = cursor.fetchall()
    lKeys = []

    for key in keys:
        lKeys.append(key[0])

    for i,d in enumerate(list(data)):
        print(i)
        print(d[0])
        if d[0] not in lKeys:
            print("Not in")
            continue
        cursor.execute("update %s set %s = '%s' where %s = '%s'"%(d_table,d_data_name,d[1].replace("'","/"),d_key,d[0]))
        connection.commit()
    print("Data moved successfully")
    return

# connection: sql connection
# uncontains: 1 or 0
# 나머지: str

def check_exist_str(connection,db_key,table_name,data_name,key_word,uncontains):
    cursor = connection.cursor()
    cursor.execute("select %s,%s from %s where %s is not null"%(db_key,data_name,table_name,data_name))
    data = cursor.fetchall()
    key_word_contains_data = {}
    key_word_uncontains_data = {}
    for d in data:
        if key_word not in d[1]:
            key_word_uncontains_data[d[0]] = d[1]
        key_word_contains_data[d[0]]=d[1]

    if uncontains == 1:
        return len(key_word_uncontains_data.items())
    else:
        return len(key_word_contains_data.items())

