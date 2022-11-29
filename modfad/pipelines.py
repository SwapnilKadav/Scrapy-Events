# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class ModfadPipeline(object):
    
    def __init__(self):
        self.create_connection()
        self.create_table()
        pass
    
    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd= 'admin',
            database = 'scrapy',
            
        )
        self.curr = self.conn.cursor()
    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS scrapy_tb(
                        LINK VARCHAR(255),
                        NAME_OF_EVENT VARCHAR(255),
                        DATE VARCHAR(255)
            )""")
    def process_item(self, item, spider):
        self.store_db(item, spider)
        return item
    def store_db(self, items, spider):
        i = 0
        for link in items['LINK']:
            self.curr.execute("SELECT * FROM scrapy_tb WHERE LINK = '%s'"%(link))
            result = self.curr.fetchone()
        
            if result:
                spider.logger.warn(f"Item already in database: {link}")
            else:  
                self.curr.execute("INSERT INTO scrapy_tb VALUES(%s,%s,%s)", (link, items['NAME_OF_EVENT'][i], items['DATE'][i]))  
                self.conn.commit()
                i += 1
    
    def close_spider(self, spider):
        ## Close cursor & connection to database 
        self.curr.close()
        self.conn.close()
 