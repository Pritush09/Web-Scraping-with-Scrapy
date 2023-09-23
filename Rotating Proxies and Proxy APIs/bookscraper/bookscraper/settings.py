# Scrapy settings for bookscraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "bookscraper"

SPIDER_MODULES = ["bookscraper.spiders"]
NEWSPIDER_MODULE = "bookscraper.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "bookscraper (+http://www.yourdomain.com)"

# we can simply provide a user agent like this to our spider but it will be static and not be changing 
#USER_AGENT = 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'



# Obey robots.txt rules
ROBOTSTXT_OBEY = True 
# this is simply for the spider to see the website 's robots.txt file where the rules are specified whether to scrape this page or not and
#  will make your spider to stop working 
# we should set this parameter false when we are scraping complex website which has high quality bot conttrol system



# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "bookscraper.middlewares.BookscraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "bookscraper.middlewares.BookscraperDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html


#ITEM_PIPELINES = {
#    "bookscraper.pipelines.BookscraperPipeline": 300,
#    "bookscraper.pipelines.SaveToMySQLPipeline": 400 # the no. denotes the order of precedence lower the no. higher the preference
#}



# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

#FEEDS = {
 #   'data.csv': {'format': 'csv','overwrite' :True}
#}


SCRAPEOPS_API_KEY = '90680d83-0ed2-4fd2-8759-1cc06bb325cd'
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'http://headers.scrapeops.io/v1/user-agents?'
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 5




## Insert Your List of Proxies Here
ROTATING_PROXY_LIST = [
    '5.252.179.222:32109',
    '168.228.51.197:41037',
    '106.242.5.206:4145',
]

# if we have all our proxies in a file we can simply do this 
# ROTATING_PROXY_LIST_PATH = '/my/path/proxies.txt'


## Enable The Proxy Middleware In Your Downloader Middlewares
DOWNLOADER_MIDDLEWARES = {
    'bookscraper.middlewares.ScrapeOpsFakeUserAgentMiddleware': 400,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

#SINGLE ENDPOINT PROXY
#When using a single proxy endpoint, you shouldn't use a rotating proxy middleware like the scrapy-rotating-proxies 
# middleware as it could interfere with the correct functioning of the proxy.