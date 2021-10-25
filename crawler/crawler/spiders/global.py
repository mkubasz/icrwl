import json

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tldextract import extract
from .config import DOMAIN
from .page import Page

class GlobalSpider(CrawlSpider):
    name = 'global_vol1'
    start_urls = ['http://globalapptesting.com/']
    rules = (
        Rule(LinkExtractor(allow_domains=DOMAIN, unique=False), callback='parse_item', follow=True),
        Rule(LinkExtractor(deny_domains=DOMAIN, unique=False), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        def extract_links(link_extractor: LinkExtractor):
            return [link.url for link in link_extractor.extract_links(response)]
        try:
            length = len(response.text)
        except:
            length = ''

        external_links = extract_links(LinkExtractor(allow=(), deny=DOMAIN))
        internal_links = extract_links(LinkExtractor(allow=(), allow_domains=DOMAIN))

        page = Page(
            domain=extract(response.url).domain,
            url=response.url,
            content_len=length,
            status=response.status,
            referer=str(response.request.headers.get('Referer', ''), 'utf-8'),
            external_links=external_links,
            internal_links=internal_links,
            externals_count=len(external_links),
            internals_count=len(internal_links),
        )
        return page.to_dict()