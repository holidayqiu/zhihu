from zhihu import settings
from zhihu.items import questionItem,answerItem,userItem
import pymysql,pymysql.cursors
from twisted.enterprise import adbapi
mysql_host=settings.MYSQL_HOST
mysql_uesr=settings.MYSQL_USER
mysql_psd=settings.MYSQL_PASSWORD
mysql_db=settings.MYSQL_DATABASE

# db=pymysql.connect(mysql_host,mysql_uesr,mysql_psd,mysql_db)
# cursor=db.cursor()

class SQL():
    @classmethod
    def insert_Item(cls,cursor,item):
        table_name=item.pop('table_name')
        col_str = ''
        row_str = ''
        for key in item.keys():
            col_str = col_str + " " + key + ","
            row_str = "{}'{}',".format(row_str,
                                       str(item[key]) if "'" not in str(item[key]) else str(item[key]).replace("'",
                                                                                                               "\\'"))
            sql = "insert INTO {} ({}) VALUES ({}) ON DUPLICATE KEY UPDATE ".format(table_name, col_str[1:-1],
                                                                                    row_str[:-1])
        for (key, value) in item.items():
            sql += "{} = '{}', ".format(str(key),
                                        str(value) if "'" not in str(value) else str(value).replace("'", "\\'"))
        sql = sql[:-2]
        cursor.execute(sql)

