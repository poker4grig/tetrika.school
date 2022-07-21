import scrapy
from scrapy.http import HtmlResponse
from animals.items import AnimalsItem


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83']

    def parse(self, response: HtmlResponse, **kwargs):
        next_page = response.xpath("//div[@id='mw-pages']/a[text()='Следующая страница']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        animals = response.xpath("//div[@class='mw-category mw-category-columns']/div/ul/li/a/@title").getall()
        yield AnimalsItem(animals=animals)
