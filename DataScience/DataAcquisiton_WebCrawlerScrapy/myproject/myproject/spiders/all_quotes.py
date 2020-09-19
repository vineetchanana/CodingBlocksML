import scrapy

class AllQuotes(scrapy.Spider):
    name = 'all_quotes'
    
    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1/'
              ]
        
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

            
    def parse(self,response):
        
        for q in response.css('div.quote'):
            text = q.css('span.text::text').get()
            author = q.css('small.author::text').get()
            tags = q.css('a.tag::text').getall()
            
            
            yield {
                'text' : text,
                'author' : author,
                'tags' : tags
            }
            
            
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)  #will make the complete url using relative url
            yield scrapy.Request(next_page,callback=self.parse)

