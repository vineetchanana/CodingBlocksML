import scrapy

class Book(scrapy.Spider):
    name = 'book'
    
    def start_requests(self):
        urls = ['http://books.toscrape.com/']
        
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
            
            
    def parse(self,response):
        
        books = response.css('article.product_pod')
        book = books[0]
        url = book.css('img::attr(src)').get()
        title = book.css('h3 a::text').get()
        price = book.css('p.price_color::text').get()
        
        columns = ['image_url','product_title','book_price']
        with open('book.csv','w',encoding='utf-8') as f:
            #write headers
            header_string = ','.join(columns) + '\n'
            f.write(header_string)
            
            book_string = url + ',' + title + ',' + price + '\n'
            f.write(book_string)
        