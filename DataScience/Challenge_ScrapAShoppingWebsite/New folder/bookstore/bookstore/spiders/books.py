import scrapy
import os

class Book(scrapy.Spider):
    name = 'books'
    
    def start_requests(self):
        urls = ['http://books.toscrape.com/catalogue/page-1.html']
        
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
            
            
    def parse(self,response):
    
        books = response.css('article.product_pod')        
        columns = ['image_url','book_title','product_price']
        
        
        with open('books2.csv','a',encoding='utf-8') as f:
            
        
            #header_string = ','.join(columns)
            #f.write(header_string)
            for book in books:
                
                url = book.css('img::attr(src)').get()
                title = book.css('h3 a::text').get()
                title = title.replace(',','').replace('"','')
                price = book.css('p.price_color::text').get()
            
                book_string = '\n' + url + ',' + title + ',' + price + '\n'
                f.write(book_string)
                
        
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)