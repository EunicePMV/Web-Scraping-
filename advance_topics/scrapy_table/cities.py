import scrapy


class CitiesSpider(scrapy.Spider):
    name = 'cities'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_cities_and_municipalities_in_the_Philippines']

    def parse(self, response):
        table = response.xpath("//*[contains(@class, 'wikitable sortable')]")
        rows = table.xpath(".//tbody//tr")[1:-1]
        for row in rows:
            city = row.xpath(".//*[@scope='row']/a/text()").get()
            population = row.xpath(".//td/text()")[0].get().strip()
            brgy = row.xpath(".//td/text()")[3].get().strip()
            province = row.xpath(".//td/a/text()").get()

            yield {'Municipality': city,
                   'Population': population,
                   'Barangays': brgy,
                   'Province': province}
