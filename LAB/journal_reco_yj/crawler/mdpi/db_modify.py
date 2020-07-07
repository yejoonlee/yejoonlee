import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='imlab506',
                             db='wb_db',
                             charset='utf8')
cursor = connection.cursor()

#cursor.execute("set innodb_lock_wait_timeout = 100000;")
cursor.execute("set innodb_lock_wait_timeout = 50000;")
cursor.execute("set autocommit = false;")
cursor.execute("set tx_isolation = 'READ-COMMITTED';")
connection.commit()
cursor.execute("select doi from representative_document where doi is not null")
rows = cursor.fetchall()
print(rows)
i = 0

for doi in rows:
    cursor.execute("update representative_document set publisher = 'mdpi' where doi = '%s'"%doi)
    cursor.commit()
    print(i)
    i+=1

connection.close()