import scrapy
import json
from scrapy.http import request,Request
from zhihu.items import questionItem,userItem,answerItem


class zhihu(scrapy.Spider):
    name = 'zhihu'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        # 'host':'sugar.zhihu.com'
        'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
        'x-udid': 'ACBC4wJauwyPTiJJeCC1fhetCR3v773F44w ='
    }


    def post_login(self,response):
        pass

    def start_requests(self):
        # for page in range(5,195,5):
        #     yield Request('https://www.zhihu.com/node/ExploreAnswerListV2?params=%7B%22offset%22%3A'
        #                 +str(page)
        #                 +'%2C%22type%22%3A%22day%22%7D',self.explore_list,headers=self.header)
        yield Request('https://www.zhihu.com/api/v4/questions/21867327/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=43&sort_by=default',self.answer_detail_json,headers=self.header)
    def explore_list(self,response):
        pass

    def question_detail(self,response):
        question_name=response.xpath('//*[@id="root"]/div/main/div/meta[1]/@content').extract()[0]
        question_url=response.xpath('//*[@id="root"]/div/main/div/meta[2]/@content').extract()[0]
        question_keywords = response.xpath('//*[@id="root"]/div/main/div/meta[3]/@content').extract()[0]
        question_answerCount = response.xpath('//*[@id="root"]/div/main/div/meta[4]/@content').extract()[0]
        question_commentCount = response.xpath('//*[@id="root"]/div/main/div/meta[5]/@content').extract()[0]
        question_dateCreated = response.xpath('//*[@id="root"]/div/main/div/meta[6]/@content').extract()[0]
        question_dateModified = response.xpath('//*[@id="root"]/div/main/div/meta[7]/@content').extract()[0]
        # question_visitsCount = response.xpath('//*[@id="root"]/div/main/div/meta[8]/@content').extract()[0]
        question_followerCount = response.xpath('//*[@id="root"]/div/main/div/meta[9]/@content').extract()[0]
        print(question_title)

    def answer_detail_json(self,response):
        answer_list=json.loads(response.text)

        for answer_detail in  answer_list['data']:
            answer=answerItem()
            author=userItem()
            answer['content']=answer_detail['content']
            answer['answer_id'] = answer_detail['id']
            answer['created_time'] = answer_detail['created_time']
            answer['voteup_count'] = answer_detail['voteup_count']
            answer['comment_count'] = answer_detail['comment_count']
            answer['updated_time'] = answer_detail['updated_time']
            answer['question_id']=answer_detail['question']['id']
            answer['author_id']=answer_detail['author']['id']
            answer['url'] = answer_detail['url']

            author['avatar_url_template']=answer_detail['author']['avatar_url_template']
            author['badge'] = answer_detail['author']['badge']
            author['type'] = answer_detail['author']['type']
            author['name'] = answer_detail['author']['name']
            author['url'] = answer_detail['author']['url']
            author['gender'] = answer_detail['author']['gender']
            author['user_type'] = answer_detail['author']['user_type']
            author['is_advertiser'] = answer_detail['author']['is_advertiser']
            author['avatar_url'] = answer_detail['author']['avatar_url']
            author['is_org'] = answer_detail['author']['is_org']
            author['headline'] = answer_detail['author']['headline']
            author['follower_count'] = answer_detail['author']['follower_count']
            author['url_token'] = answer_detail['author']['url_token']
            author['id'] = answer_detail['author']['id']
            yield answer
            yield author



