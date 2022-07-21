from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from animals.spiders.wiki import WikiSpider

if __name__ == '__main__':
    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    runner.crawl(WikiSpider)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()