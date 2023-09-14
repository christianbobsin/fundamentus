import scrapy
import time



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

        count = 0
        for row in rows:
            value = row.xpath(".//td[1]/a/text()").extract_first()
     
            count += 1

            if  ((count % 5 ) == 0):
                time.sleep(1.4)

            yield scrapy.Request(
                #url='http://www.fundamentus.com.br/detalhes.php?papel=%s' % value.strip(),
                url='https://statusinvest.com.br/acoes/%s' % value.strip(),
                callback= self.parse_detail
            )            

        # yield {
        #  "ticket" : value 
        # }

    def parse_detail(self, response):
        
        name = response.xpath('/html/body/main/header/div[2]/div/div[1]/div/ol/li[3]/a/span/text()').extract_first()
        cotation = response.xpath('/html/body/main/div[2]/div/div[1]/div/div[1]/div/div[1]/strong/text()').extract_first()
        p_vp = response.xpath('/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[4]/div/div/strong/text()').extract_first()
        dividend_yeld = response.xpath('/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[1]/div/div/strong/text()').extract_first()
        
        yield {
            "name": name,
            "cotation" : cotation,
            "p_vp" : p_vp,
            "dividend_yeld": dividend_yeld
        }       

   
        #print ( " cotation: {cotation} / p/vp: {p_vp}")
        




#Status Invest

#name
#/html/body/main/header/div[2]/div/div[1]/div/ol/li[3]/a/span

#cotation
#/html/body/main/div[2]/div/div[1]/div/div[1]/div/div[1]/strong

#p_vp
#/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[4]/div/div/strong

#d_y
#/html/body/main/div[2]/div/div[8]/div[2]/div/div[1]/div/div[1]/div/div/strong



