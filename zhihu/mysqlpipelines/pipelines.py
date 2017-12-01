from zhihu.items import questionItem,answerItem,userItem
from zhihu.mysqlpipelines.SQL import SQL

class pipelines(object):
    def process_item(self,item,spider):
        if isinstance(item,answerItem):
            table_name = 'answer_detail'
            SQL.insert_Item(table_name,item)

        if isinstance(item, userItem):
            table_name = 'user_detail'
            SQL.insert_Item(table_name,item)

