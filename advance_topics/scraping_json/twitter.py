import scrapy
import json

class TwitterSpider(scrapy.Spider):
    name = 'twitter'
    allowed_domains = ['thetrumparchive.com']
    start_urls = ['file:///home/NAME/Desktop/trumptweets.json']

    def parse(self, response):
        json_response = json.loads(response.body)

        for tweet in json_response:
            yield{'date': tweet['date'],
                  'favorites': tweet['favorites'],
                  'id': tweet['id'],
                  'isRetweet': tweet['isRetweet'],
                  'retweets': tweet['retweets'],
                  'text': tweet['text']}