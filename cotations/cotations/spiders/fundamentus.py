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
        
        name = response.xpath('//td[2]/span/text()').extract_first()
        cotation = response.xpath('//td[@class="data destaque w3"]/span/text()').extract_first()
        p_vp = response.xpath('/html/body/div[1]/div[2]/table[3]/tbody/tr[2]/td[4]/span/text()').extract_first()
        dividend_yeld = response.xpath('//tbody/tr[9]/td[4]/span/text()').extract_first()
        
        yield {
            "name": name,
            "cotation" : cotation,
            "p_vp" : p_vp,
            "dividend_yeld": dividend_yeld
        }       

   
        #print ( " cotation: {cotation} / p/vp: {p_vp}")
        

