# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FileDownloader(scrapy.Item):
    """Scrapy Item Class defined for downloading files.
    
    Attributes:
        file_urls (scrapy.Field): campo que receberá a URL do arquivo
            a ser baixado.
        files (scrapy.Field): campo que registrará o status do arquivo
            a ser baixado.
    
    """
    file_urls = scrapy.Field() # Do not rename this!
    files = scrapy.Field() # Do not rename this!
