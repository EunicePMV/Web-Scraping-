import scrapy

def table_data(response, data):
    return response.xpath(".//td")

class TableSpider(scrapy.Spider):
    name = 'table'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']

    def parse(self, response):
        table = response.xpath("//table[contains(@class, 'wikitable sortable')]")[0]
        rows = table.xpath(".//tr")[1:]
        for row in rows:
            rank = row.xpath(".//td/text()").get().strip()
            city = row.xpath(".//td//a//text()").get()
            state = row.xpath(".//td/span[@class='flagicon']/following-sibling::a/text()|"
                              ".//td/span[@class='flagicon']/following-sibling::text()").get().strip()
            
            yield{'rank': rank,
                  'city': city,
                  'state': state}




# After going to the table row, go to the table data 



