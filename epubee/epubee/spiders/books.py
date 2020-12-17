import scrapy
from lxml import html
from epubee.items import EpubeeItem

class BooksSpider(scrapy.Spider):
    name = 'books'
    #allowed_domains = ['www.eupubee.com']
    # link to book cover here
    start_urls = ['http://reader.epubee.com/books/mobile/4f/4f1cec5cbbadf48145bdf60949e28e73/']
    base_url = 'http://reader.epubee.com'
    num = 0



    def parse(self, response):
        # get the content page urls
        contents = response.xpath('/html/body/div[1]/div[3]/div//div//div/p')

        for chapter in contents:
            #print(chapter.xpath('//div/p/a/@href').extract())
            url = self.base_url+chapter.xpath('./a/@href').extract_first()
            title = chapter.xpath('./p/a/text()').extract_first()
            yield scrapy.Request(url = url, callback = self.parse_chapter)

    def parse_chapter(self, response):
        #print(response.url)
        page = response.xpath('/html/body/div[1]/div[4]/div')
        images = page.xpath('.//img/@src')
        srcs = []
        for img in images:
            src = self.start_urls[0]+img.extract()
            if src not in srcs:
                srcs.append(src)

        item = EpubeeItem()
        item['srcs'] = srcs
        item['page'] = page.extract()[0]
        item['num'] = response.url.split('/')[-1]

        # print(src)
        yield item

