import scrapy
#https://thepythonscrapyplaybook.com/freecodecamp-beginner-course/freecodecamp-scrapy-beginners-course-part-4-first-scraper/#creating-our-scrapy-spider


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            yield{
                "name": book.css('h3 a::text').get(),
                "Price":book.css('.product_price .price_color::text').get(),
                "URL":  book.css('h3 a').attrib['href']
            }
        next_page = response.css('li.next a ::attr(href)').get()
        
        if next_page is not None:
            if "catalogue/" in next_page:
                next_page_url = "http://books.toscrape.com/"+next_page
            else:
                next_page_url = "http://books.toscrape.com/catalogue/"+next_page
            yield response.follow(next_page_url , callback=self._parse)