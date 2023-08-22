import scrapy
import json

class QA(scrapy.Spider):
    name = 'qa_practice_api'
    start_urls=['https://jsonplaceholder.typicode.com/comments']

    def parse(self, response):
        data = json.loads(response.body) 
        # yield from data['layer1']['layer2'] sa ma duc ierahic pana in array-ul de obiecte
        
        yield from data

      

        # next_page = data['next_page']
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)