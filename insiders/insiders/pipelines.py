# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime


class InsidersPipeline:
    def __init__(self):
        self.fp = None
        self.item = None

    def open_spider(self, spider):
        self.fp = open('./insiders.csv', 'a')
        #header = 'date,dba,dbt,dsa,dst,wba,wbt,wsa,wst,mba,mbt,msa,mst,qba,qbt,qsa,qst,yba,ybt,ysa,yst,y2ba,y2bt,y2sa,y2st\n'


    def process_item(self, item, spider):

        self.item = item
        return item

    def close_spider(self, spider):
        today = datetime.today().strftime('%Y%m%d')
        data = [today, self.item['dba'], self.item['dbt'], self.item['dsa'], self.item['dst'], self.item['wba'], self.item['wbt'], self.item['wsa'], self.item['wst'], self.item['mba'], self.item['mbt'], self.item['msa'], self.item['mst'], self.item['qba'], self.item['qbt'], self.item['qsa'], self.item['qst'], self.item['yba'], self.item['ybt'], self.item['ysa'], self.item['yst'], self.item['y2ba'], self.item['y2bt'], self.item['y2sa'], self.item['y2st']]
        line = ','.join(data)
        self.fp.write(line + '\n')
        self.fp.close()
