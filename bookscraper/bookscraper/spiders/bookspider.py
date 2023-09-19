import scrapy
#https://thepythonscrapyplaybook.com/freecodecamp-beginner-course/freecodecamp-scrapy-beginners-course-part-4-first-scraper/#creating-our-scrapy-spider
from bookscraper.items import BookItem

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    #custom_settings = {
     #   'FEEDS': { 'data.csv': { 'format': 'csv',}}
      #  }

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            books_url = book.css('h3 a::attr(href)').get()
        
        
            if "catalogue/" in books_url:
                books_url_full = "http://books.toscrape.com/"+books_url
            else:
                books_url_full = "http://books.toscrape.com/catalogue/"+books_url
            yield response.follow(books_url_full , callback=self.parse_book_page)
            
        
        
        next_page = response.css('li.next a ::attr(href)').get()
        
        if next_page is not None:
            if "catalogue/" in next_page:
                next_page_url = "http://books.toscrape.com/"+next_page
            else:
                next_page_url = "http://books.toscrape.com/catalogue/"+next_page
            yield response.follow(next_page_url , callback=self.parse)


    def parse_book_page(self,response):
        # for discription response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
        # category  response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get()

        book = response.css("div.product_main")[0]
        table_rows = response.css("table tr")

        # if we miss type any of the name here in the key par that might not go into the database and it futher might not be processed down
        # the line if we just  used yield{} to get our output

        book_item = BookItem()

        book_item['url'] = response.url
        book_item['title'] = book.css("h1 ::text").get()
        book_item['upc'] = table_rows[0].css("td ::text").get()
        book_item['product_type'] = table_rows[1].css("td ::text").get()
        book_item['price_excl_tax'] = table_rows[2].css("td ::text").get()
        book_item['price_incl_tax'] = table_rows[3].css("td ::text").get()
        book_item['tax'] = table_rows[4].css("td ::text").get()
        book_item['availability'] = table_rows[5].css("td ::text").get()
        book_item['num_reviews'] = table_rows[6].css("td ::text").get()
        book_item['stars'] = book.css("p.star-rating").attrib['class']
        book_item['category'] = book.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get()
        book_item['description'] = book.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
        book_item['price'] = book.css('p.price_color ::text').get()
        
        yield book_item
        # This gives our data more structure and allows us to more easily clean it in data pipelines.



# to get a output save to file 
# command -> scrapy crawl bookspider -O bookdata.csv
