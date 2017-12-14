import pymysql,pymysql.cursors
from zhihu.items import questionItem,answerItem,userItem
from zhihu.mysqlpipelines.SQL import SQL
from twisted.enterprise import adbapi
from zhihu import settings

class pipelines(object):
    def __init__(self):
        self.dbpool=adbapi.ConnectionPool('pymysql',
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DATABASE,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWORD,
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True)


    def process_item(self,item,spider):
        if isinstance(item,answerItem):
            self.dbpool.runInteraction(SQL.insert_Item,item)

            # SQL.insert_Item(table_name,item)

        if isinstance(item, userItem):
            self.dbpool.runInteraction(SQL.insert_Item, item)
            # SQL.insert_Item(table_name,item)

        if isinstance(item, questionItem):
            self.dbpool.runInteraction(SQL.insert_Item, item)
            # SQL.insert_Item(table_name,item)


    def insert_Item(self,cursor,item):
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