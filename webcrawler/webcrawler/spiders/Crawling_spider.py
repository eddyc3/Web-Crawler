from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    name = "crawler40k"
    allowed_domains = ["warhammer.com"]
    start_urls = ["https://www.warhammer.com/en-GB/shop/warhammer-40000"]

    rules = (
        Rule(LinkExtractor(deny = "gaming-rules" "ways-to-play" "gameplay-accessories")),
        Rule(LinkExtractor(allow="warhammer-40000"), callback="parse_item"),
    )


    def parse_item(self, response):
        yield {
            "title": response.css("data-testid ="titlebar-product-name" h2::text").get(),
        }