import scrapy
from insiders.items import InsidersItem


class InsiderSpider(scrapy.Spider):
    name = 'insider'
    #allowed_domains = ['www.dataroma.com']
    start_urls = ['https://www.dataroma.com/m/ins/ins.php?t=d&am=0&sym=&o=fd&d=d']
    timeFrames = ['w', 'm', 'q', 'y', 'y2']
    baseUrl = 'https://www.dataroma.com/m/ins/ins.php?t={}&am=0&sym=&o=fd&d=d'
    item = InsidersItem()

    def parse(self, response):
        table = response.xpath('/html/body/div/div[3]/table[1]//td/text()')
        #print(table[5].extract())
        self.item['dbt'] = table[4].extract().replace('$', '').replace(',', '')
        self.item['dba'] = table[5].extract().replace('$', '').replace(',', '')
        self.item['dst'] = table[7].extract().replace('$', '').replace(',', '')
        self.item['dsa'] = table[8].extract().replace('$', '').replace(',', '')



        for t in self.timeFrames:
            myUrl = self.baseUrl.format(t)
            yield scrapy.Request(url=myUrl, callback=self.parse_tf, meta={'item':self.item, 'timeframe':t})

        yield self.item

    def parse_tf(self, response):
        table = response.xpath('/html/body/div/div[3]/table[1]//td/text()')
        timeFrame = response.meta['timeframe']
        self.item[timeFrame+'bt'] = table[4].extract().replace('$', '').replace(',', '')
        self.item[timeFrame+'ba'] = table[5].extract().replace('$', '').replace(',', '')
        self.item[timeFrame+'st'] = table[7].extract().replace('$', '').replace(',', '')
        self.item[timeFrame+'sa'] = table[8].extract().replace('$', '').replace(',', '')
        #yield self.item
