# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class answerItem(scrapy.Item):
    table_name = scrapy.Field()
    question_id=scrapy.Field()#问题编号
    content = scrapy.Field()#评论
    created_time = scrapy.Field()#创建（发布）时间
    author_id=scrapy.Field()#作者编号
    answer_id = scrapy.Field()#答案编号
    voteup_count = scrapy.Field()#点赞人数
    comment_count = scrapy.Field()#评论人数
    updated_time = scrapy.Field()#更新（编辑）时间
    url=scrapy.Field()

class userItem(scrapy.Item):
    table_name=scrapy.Field()
    avatar_url_template = scrapy.Field()
    badge = scrapy.Field()
    type = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    gender = scrapy.Field()
    user_type = scrapy.Field()
    is_advertiser = scrapy.Field()
    avatar_url = scrapy.Field()
    is_org = scrapy.Field()
    headline = scrapy.Field()
    follower_count = scrapy.Field()
    url_token = scrapy.Field()
    id = scrapy.Field()


class questionItem(scrapy.Item):
    table_name = scrapy.Field()
    id=scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    keywords=scrapy.Field()
    answerCount=scrapy.Field()
    commentCount=scrapy.Field()
    dateCreated=scrapy.Field()
    dateModified=scrapy.Field()
    followerCount=scrapy.Field()
