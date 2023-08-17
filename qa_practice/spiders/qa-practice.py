import scrapy

class QA(scrapy.Spider):
    name = 'qa_practice'
    start_urls=['https://qa-practice.netlify.app/products_list']

    def parse(self, response):
        for products in response.css('.shop-item'):
            try:
                yield {
                    'name': products.css('.shop-item-title::text').get(),
                    'price': products.css('.shop-item-price::text').get().replace('$', '')
                }
            except:
                yield {
                'name': products.css('.shop-item-title::text').get(),
                'price': 'sold out'
                }    
        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)    
