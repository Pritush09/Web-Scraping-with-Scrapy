import scrapy
#https://thepythonscrapyplaybook.com/freecodecamp-beginner-course/freecodecamp-scrapy-beginners-course-part-9-rotating-proxies/#how-to-use-rotatingbackconnect-proxiesfrom bookscraper.items import BookItem
#import random
from items import BookItem


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    #custom_settings = {
     #   'FEEDS': { 'data.csv': { 'format': 'csv',}}
      #  }

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # this will be changing user agent which will be hard for the bot detecter of website to detect if we are scraping there data
    #This works but it has 2 drawbacks:

     # * We need to manage a list of user-agents ourselves.
     # * We would need to implement this into every spider, which isn't ideal.
     
     #A better approach would be to use a Scrapy middleware to manage our user-agents for us.
    
    #user_agent_list = [
     #   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
      #  'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
       # 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
       # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
       # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
    #]
    

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            books_url = book.css('h3 a::attr(href)').get()
        
        
            if "catalogue/" in books_url:
                books_url_full = "http://books.toscrape.com/"+books_url
            else:
                books_url_full = "http://books.toscrape.com/catalogue/"+books_url
            yield response.follow(books_url_full , callback=self.parse_book_page)
                                # just add this line inside the response .follow() function 
                                  #headers={"User-Agent": self.user_agent_list[random.randint(0, len(self.user_agent_list)-1)]})
            
        
        
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
