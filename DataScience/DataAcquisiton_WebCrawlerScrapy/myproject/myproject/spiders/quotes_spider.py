import scrapy

#spiders are the classes that are used to scrape the data
#scrapy.Spider is a base class, you need to extract data from it

class QuotesSpider(scrapy.Spider):
    name = 'quotes_spider'
    
    def start_requests(self):
        #if many urls,use for loop
        urls = ['http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/'
               ]
        
        #Generator function
        for url in urls:
            #scrapy.Request is similar to api section
            #after getting response, we need to parse it
            yield scrapy.Request(url=url,callback = self.parse)
            
    def parse(self,response):
        #we got the response,need to know from which page response is coming
        page_id = response.url.split('/')[-2] #to get the page_id from url

        filename = "quotes-%s.html"%page_id  #quotes-1.html,quotes-2

        with open(filename,'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)