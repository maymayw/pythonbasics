# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class EpubeePipeline:
    def __init__(self):
        self.fp = None
        self.item = None

    def open_spider(self, spider):
        pass
        #header = 'date,dba,dbt,dsa,dst,wba,wbt,wsa,wst,mba,mbt,msa,mst,qba,qbt,qsa,qst,yba,ybt,ysa,yst,y2ba,y2bt,y2sa,y2st\n'


    def process_item(self, item, spider):

        self.item = item
        #print(self.item['num'], self.request.url)
        self.fp = open('./downloads/' + self.item['num'], 'w', encoding='utf-8')
        self.fp.write(self.item['page'])
        self.fp.close()
        return item

    def close_spider(self, spider):
        pass


class epubeeImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        #print(item['src'])
        img_urls = item['srcs']
        for url in img_urls:
            yield scrapy.Request(url)

    def file_path(self, request, response=None, info=None):
        imgName = request.url.split('/')[-1]

        # in settings.py IMAGE_STORE = './downloads'
        return imgName

    def item_completed(self, results, item, info):
        return item