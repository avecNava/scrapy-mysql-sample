# -*- coding: utf-8 -*-

# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

import mysql.connector

class QuotesPipeline(object):

    conn = ''
    cursor = ''

    def __init__(self):

        self.conn = mysql.connector.connect(
                host = "192.168.10.10",
                user = "homestead",
                passwd = "secret",
                database = "test",
                # charset = "utf-8",
                use_unicode=True
            )
        
        self.cursor = self.conn.cursor()
        # self.create_tables()        

    #executes for every records in the item repository
    def process_item(self, item, spider):
        print('========================================================================================================')
        self.create_record(item)
        
        return item

    def create_record(self, item):    
        self.cursor.execute("""INSERT INTO tblquotes VALUES (%s, %s, %s)""", 
                        (   item['title'],
                            item['author'],
                            item['tag']
                        )
                    )   
        self.conn.commit() 

    #Read the documentation about making tables
    #https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html

    # def create_tables(self):
    #     self.cursor.execute("""DROP TABLE IF EXISTS tblquotes """)
    #     self.cursor.execute("""
    #         CREATE TABLE tblquotes (
    #             title text,
    #             author text,
    #             tag text
    #         )
    #     """)

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()