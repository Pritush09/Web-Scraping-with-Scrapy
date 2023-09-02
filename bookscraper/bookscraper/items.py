# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Scrapy Items are a predefined data structure that holds your data. Instead of yielding your scraped data in the form of a dictionary for 
# example, you define a Item schema beforehand in your items.py file and use this schema when scraping data. This enables you to quickly and 
# easily check what structured data you are collecting in your project, it will raise exceptions if you try and create incorrect data with
#  your Item.



# we can also use a serializer if something that was not read by the spyder while saving data to the file to convert it to a proper manner 
# we wanted 

def serialize_price(val):
    return f'£ {str(val)}'





class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    price_excl_tax = scrapy.Field()# as an argument inside (#serializer = serialize_price)
    price_incl_tax = scrapy.Field()
    tax = scrapy.Field()
    availability = scrapy.Field()
    num_reviews = scrapy.Field()
    stars = scrapy.Field()
    category = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    pass
