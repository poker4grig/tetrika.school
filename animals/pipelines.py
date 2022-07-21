# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AnimalsPipeline:
    def process_item(self, item, spider):
        with open('animals.txt', 'a', encoding='UTF-8') as file:
            file.write(str(item['animals']))

        return item
