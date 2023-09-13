import scrapy



class FundamentusSpider(scrapy.Spider):
    
    name = "fundamentus"
    
    #allowed_domains = ["www.fundamentus.com.br"]
    #start_urls = ["http://www.fundamentus.com.br/"]
    start_urls = ["https://www.fundamentus.com.br/detalhes.php?papel="]

    def parse(self, response):
        #pass
        self.log('SCRPAPING UNIVERSEEEEE')
        table = response.xpath("/html/body/div[1]/div[2]/div/div/table/tbody")
        rows = table.xpath(".//tr")

        for row in rows:
            value = row.xpath(".//td[1]/a/text()").extract_first()
     
            #print(value)

            yield scrapy.Request(
                url='http://www.fundamentus.com.br/detalhes.php?papel=%s' % value.strip(),
                callback= self.parse_detail
            )            

        # yield {
        #  "ticket" : value 
        # }

    def parse_detail(self, response):
        cotation = response.xpath('//td[@class="data destaque w3"]/span/text()').extract_first()
        p_vp = response.xpath('//table[3]/tbody/tr[3]/td[4]/text()').extract_first()

        yield {
            "cotation" : cotation,
            "p_vp" : p_vp
        }

        #print ( " cotation: {cotation} / p/vp: {p_vp}")
        

