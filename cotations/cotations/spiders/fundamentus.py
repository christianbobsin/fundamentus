import scrapy
import time

ignore_tickets = ['ALLL11', 'ALBA3', 'AGIN3', 'AGEN33', 'AGEI3',  'AFLU5', 'AFLU3', 'AELP3', 'AESL3', 'AEDU3', 'AEDU11', 'DHBI4',  'AESL4',
                  'WSON3',  'WMBY3', 'WIZS3', 'WISA4',  'WEGE4',  'VVAX4', 'VVAX3'  'ENER3', 'ELUM4', 'ELPL6', 'ELPL5', 'ELPL4', 'ELEV3',
                  'CCPR3', 'CCIM3', 'CCIH4', 'CCHI3', 'CBMA4', 'CBMA3', 'ALLL4', 'ETER4', 'WSON33', 'WISA3', 'VVAX3', 'VVAR3', 'VULC4',
                  'RCTB42', 'RCTB41', 'RCTB33', 'RCTB31', 'PTQS4', 'PTPA4',  'PTPA3',  'PTIP4', 'PTBL4', 'PRVI3', 'PRTX3', 'PRML3', 
                  'DFVA4', 'DMFN3', 'DHBI3', 'DFVA3', 'DAYC4', 'DAYC3', 'DAGB33', 'CZLT33', 'CTWR3', 'CTPC4', 'CTPC3', 'CTIP3', 'CSTB4',
                  'VTLM3', 'VPTA4', 'VPTA3', 'VPSC4', 'VPSC3', 'VIVO4', 'VIVO3', 'VINE5', 'VINE3', 'VIGR3', 'VCPA4', 'VALE5', 'VAGV3', 'VAGV4',
                  'IMBI4', 'IMBI3', 'ILMD4', 'ILMD3', 'ILLS4', 'IGUA6', 'IGUA5', 'IGUA3', 'IMCH3', 'IENG3', 'IENG5', 'IDVL11', 'ICPI3',
                  'ABRE3', 'ABYA3', 'ACES3', 'AMBV3', 'AMBV4', 'AMPI3', 'AMIL3', 'ARCZ3', 'ARCE3', 'ARLA4', 'ARPS3', 'ARPS4', 'ARTE3'
                  'ALLL3', 'PARC3', 'VNET3', 'VGOR4', 'VGOR3', 'VAGR3', 'UOLL4', 'UGPA4', 'UCOP4', 'UBBR3', 'UBBR4', 'UBBR11', 'TUPY4',
                  'FGUI4', 'FGUI3', 'FFTL4', 'FFTL3', 'FLCL6', 'FLCL5', 'FLCL3', 'FJTA4', 'FJTA3', 'FTRX3', 'FTRX4', 'GALO3', 'GAFP4',
                  'ABCB3', 'ACES4', 'AORE3', 'ARCZ6', 'ARLA3', 'ASSM3', 'ASSM4', 'ASTA4', 'AURA32', 'AUTM3', 'AVIL3', 'BAHI11', 'BAHI4'
                  'TSPP3', 'TSPP4', 'TSEP3', 'TSEP4', 'TROR3', 'TROR4', 'TRFO3', 'TRFO4', 'TPRC3', 'TNLP4', 'TNLP3', 'TNEP4', 'TNEP3',
                  'TNCP4', 'TNCP3', 'TMGC7', 'TMGC3', 'TMGC13', 'TMGC12', 'TMGC11', 'TMCP4', 'TMCP3', 'TMAR6', 'TMAR5', 'TMAR3', 'TLCP3',
                  'TLCP4', 'ARTE3', 'ARTE4', 'ARTR3', 'BAHI5', 'BBTG11', 'BBTG12', 'BBTG13', 'BCAL6', 'BECE3', 'BECE4', 'BELG3', 'BELG4',
                  'BEMA3', 'TIBR5', 'TIBR6', 'TPRC6', 'TIBR3', 'TENE7', 'TENE5', 'TEMP3', 'TEFC11', 'TDBH3', 'TDBH4', 'TCSL4', 'TCOC4',
                  'BAHI4', 'BBRK3', 'BERG3', 'BESP3', 'BESP4', 'BFIT3', 'BFIT4', 'BICB4', 'BICB3', 'BHGR3', 'BKBR3', 'BISA3', 'BIOM4',
                  'TCOC3', 'TBLE3', 'TBLE6', 'TARP11', 'TANC4', 'TAMM3', 'SWET3', 'SUZB5', 'SUZB6', 'SUZA4', 'SULT4', 'SULT3', 'STRP4',
                  'TAMM4', 'SEMP3', 'SGAS4', 'SDIA4', 'ROMI4', 'PRGA4', 'PMET6', 'PORP4', 'PCAR5', 'ODER3', 'PALF11', 'NATU3', 'MLPA4',
                  'SSBR3', 'TBLE5', 'SZPQ4', 'STLB3', 'STBP11', 'SNSL3', 'SMLE3', 'SJOS4', 'SJSO3', 'SLCP3', 'SGEN3', 'SGAS3', 'SEBB4',
                  'SEBB3'
                  ]


valid_tickets = [ "AALR3", "ALPK3", "ALPA4", "ALPA3", "AHEB6", "AHEB5", "ALLD3", "AHEB3", "AGXY3", "AFLT3", "AGRO3", "AESB3", "AERI3", "ZAMP3", 
"YDUQ3", "WLMM4", "WLMM3", "WIZC3", "WHRL4", "WHRL3", "WEST3", "WEGE3", "VVEO3", "VVAR4", "VVAR11","VULC3", "VSPT4", "VSTE3", "VSPT3", "VIVT4", 
"VLID3", "VIVT3", "VIVR3", "VIVA3", "VITT3", "VIIA3", "VBBR3", "VAMO3", "VALE3", "USIM6", "USIM5", "UNIP6", "USIM3", "UNIP5", "UNIP3", "UGPA3", 
"UCAS3", "TXRX4", "TXRX3", "TUPY3", "TTEN3", "TRPN3", "TRPL3", "TRPL4", "TRIS3", "TRAD3", "TOYB4", "TPIS3", "TOYB3", "TOTS3", "TKNO4", "TIMS3", 
"TIET4", "TIET3", "TIET11","TGMA3", "TESA3", "TFCO4", "TEND3", "TELB4", "TELB3", "TEKA4", "TECN3", "TEKA3", "TCSA3", "TCNO4", "TCNO3", "TASA4", 
"TASA3", "TAEE3", "TAEE11","TAEE4", "SYNE3", "SUZB3", "SULA4", "SULA3", "SULA11","STBP3", "SQIA3", "SPRI5", "SPRI3", "SPRI6", "SOND6", "SOND3", 
"SOND5", "SOJA3", "SOMA3", "SNSY5", "SMTO3", "SMLS3", "SMFT3", "SLED4", "SLED3", "SLCE3", "SIMH3", "SHOW3", "SHUL4", "SGPS3", "SEER3", "SEQL3", 
"SEDU3", "SCAR3", "SBFG3", "SBSP3", "SAPR4", "SAPR11","SAPR3", "SANB4", "SANB3", "SANB11","RSUL4", "RSID3", "RRRP3", "RPMG3", "RPAD6", "RPAD5", 
"RPAD3", "ROMI3", "RNEW3", "RNEW4", "RNEW11","RLOG3", "RENT3", "REDE3", "RECV3", "RDNI3", "RDOR3", "RCSL3", "RCSL4", "RAPT4", "RANI4", "RAPT3", 
"RANI3", "RAIZ4", "RAIL3", "RADL3", "QGEP3", "QUAL3", "PTNT4", "PTNT3", "PTBL3", "PSSA3", "PRNR3", "PRIO3", "POWE3", "POSI3", "PORT3", "POMO4", 
"POMO3", "PNVL3", "PNVL4", "PMAM3", "PLPL3", "PLAS3", "PINE4", "PINE3", "PFRM3", "PGMN3", "PETR4", "PETZ3", "PETR3", "PEAB3", "PEAB4", "PDGR3", 
"PDTC3", "PCAR4", "PCAR3", "PATI4", "PATI3", "PARD3", "ORVR3", "OSXB3", "OPCT3", "ONCO3", "OMGE3", "OIBR4", "OGXP3", "OIBR3", "OFSA3", "ODPV3", 
"ODER4", "NUTR3", "NORD3", "NTCO3", "NGRD3", "NINJ3", "NEXP3", "NEOE3", "NAFG3", "NAFG4", "MWET4", "MYPK3", "MWET3", "MULT3", "MTSA4", "MTIG4", 
"MTRE3", "MTIG3", "MSPA4", "MSPA3", "MRVE3", "MRSA6B","MRSA5B","MRSA3B","MRFG3", "MPLU3", "MOVI3", "MODL4", "MOSI3", "MODL3", "MODL11","MOAR3", 
"MNPR3", "MNDL3", "MMXM3", "MMAQ4", "MMAQ3", "MLAS3", "MILS3", "MGLU3", "MGEL4", "MGEL3", "MERC4", "MERC3", "MELK3", "MEGA3", "MEAL3", "MDNE3", 
"MDIA3", "MBLY3", "MATD3", "MAPT4", "MAPT3", "MAGG3", "LWSA3", "LVTC3", "LUXM4", "LUXM3", "LREN3", "LUPA3", "LPSB3", "LOGN3", "LOGG3", "LJQQ3", 
"LIPR3", "LIGT3", "LINX3", "LEVE3", "LCAM3", "LAVV3", "LAND3", "LAME3", "KRSA3", "KLBN4", "KLBN3", "KEPL3", "KLBN11","JSLG3", "JOPA3", "JOPA4", 
"AMER3", "JHSF3", "JFEN3", "JBSS3", "JALL3", "ITUB4", "ITSA4", "ITUB3", "ITSA3", "ITEC3", "IRBR3", "INTB3", "INEP4", "INEP3", "IGTI3", "IGTI11",
"IGTA3", "IGBR3", "IFCM3", "IDVL4", "IDVL3", "HYPE3", "HOOT4", "HGTX3", "HETA4", "HETA3", "HBTS5", "HBSA3", "HBRE3", "HBOR3", "HAPV3", "HAGA4", 
"HAGA3", "GUAR4", "GUAR3", "GSHP3", "GRND3", "GPIV33","GPAR3", "GOLL4", "GOAU4", "GOAU3", "GNDI3", "GMAT3", "GGPS3", "GGBR4", "GGBR3", "GETT4", 
"GFSA3", "GETT3", "GEPA4", "GEPA3", "GBIO33","FRTA3", "FRIO3", "FRAS3", "FNCN3", "FLRY3", "FIQE3", "FIGE3", "FIGE4", "FIEI3", "FIBR3", "FHER3", 
"FESA4", "FESA3", "FBMC4", "FBMC3", "EZTC3", "EVEN3", "EUCA3", "EUCA4", "ETER3", "ESTR4", "ESTR3", "ESPA3", "EQTL3", "EQPA7", "EQPA6", "EQPA5", 
"EQPA3", "EPAR3", "ENMT4", "ENMT3", "ENGI4", "ENJU3", "ENGI3", "ENGI11","ENEV3", "ENBR3", "ENAT3", "EMBR3", "EMAE4", "ELPL3", "ELMD3", "ELET6", 
"ELET5", "ELET3", "ELEK4", "ELEK3", "EKTR3", "EKTR4", "EGIE3", "EEEL4", "EEEL3", "ECPR4", "ECPR3", "ECOR3", "EALT4", "EALT3", "DXCO3", "DTCY3", 
"DOTZ3", "DOHL4", "DOHL3", "DMVF3", "DMMO3", "DIRR3", "DEXP4", "DEXP3", "DESK3", "DASA3", "CYRE3", "CXSE3", "CURY3", "CVCB3", "CTSA8", "CTSA4", 
"CTSA3", "CTNM4", "CTNM3", "CTKA4", "CTKA3", "CSUD3", "CSRN6", "CSRN5", "CSRN3", "CSNA3", "CSMG3", "CSED3", "CSAN3", "CSAB4", "CSAB3", "CRPG6", 
"CRPG5", "CRPG3", "CRIV4", "CRIV3", "CRFB3", "CREM3", "CPRE3", "CPLE6", "CPLE5", "CPLE3", "CPLE11","CPFE3", "CORR4", "CORR3", "COGN3", "COCE6", 
"COCE5", "COCE3", "CMIG4", "CMIN3", "CMIG3", "CLSC4", "CLSA3", "CLSC3", "CIEL3", "CGRA4", "CGRA3", "CGAS5", "CGAS3", "CESP6", "CESP5", "CESP3", 
"CEPE6", "CEPE5", "CEPE3", "CEGR3", "CEED4", "CEED3", "CEEB5", "CEEB3", "CEDO4", "CEDO3", "CEBR6", "CEBR5", "CEBR3", "CEAB3", "CCXC3", "CCRO3", 
"CBEE3", "CBAV3", "CASN3", "CASH3", "CAML3", "CAMB4", "CAMB3", "CALI3", "CALI4", "BSLI4", "BSLI3", "BSEV3", "BRSR6", "BRSR5", "BRPR3", "BRSR3", 
"BRML3", "BRKM6", "BRKM3", "BRKM5", "BRIV3", "BRIV4", "BRIT3", "BRIN3", "BRGE7", "BRGE8", "BRGE6", "BRGE5", "BRGE3", "BRGE12","BRGE11","BRFS3", 
"BRBI11","BRAP4", "BRAP3", "BPHA3", "BPAT33","BPAR3", "BPAN4", "BPAC5", "BPAC3", "BPAC11","BOBR4", "BOBR3", "BOAS3", "BNBR3", "BMOB3", "BMKS3", 
"BMIN4", "BMIN3", "BMGB4", "BMEB4", "BMEB3", "BLUT4", "BLUT3", "BLAU3", "BIOM3", "BIDI4", "BIDI3", "BIDI11","BGIP4", "BGIP3", "BEES4", "BEES3", 
"BEEF3", "BDLL4", "BDLL3", "BBSE3", "BBDC4", "BBAS3", "BBDC3", "BAZA3", "BAUH4", "BALM3", "BALM4", "BAHI3", "B3SA3", "AZUL4", "AZEV4", "AZEV3", 
"AVLL3", "AURE3", "AURA33","ATOM3", "ATMP3", "ARZZ3", "ASAI3", "ARML3", "APTI4", "APER3", "ANIM3", "AMER3", "AMBP3", "AMAR3", "ALUP4", "ALUP3", 
"ALUP11","ALSO3", "ALSC3", "ADHM3", "ABEV3", "ABCB4", ]


class FundamentusSpider(scrapy.Spider):
    
    name = "fundamentus"

    #allowed_domains = ["www.fundamentus.com.br"]
    #start_urls = ["http://www.fundamentus.com.br/"]
    #start_urls = ["https://www.fundamentus.com.br/detalhes.php?papel="]
    start_urls = ["https://www.statusinvest.com.br"]

    def parse(self, response):
        #pass
        self.log('SCRPAPING UNIVERSEEEEE')
        #table = response.xpath("/html/body/div[1]/div[2]/div/div/table/tbody")
        #rows = table.xpath(".//tr")

        count = 0
        for ticket in valid_tickets:
            #value = row.xpath(".//td[1]/a/text()").extract_first()
     
            count += 1

            #if  ((count % 60 ) == 0):   
            #    self.log('SLEEP...')             
            #    time.sleep(25)

            #if value.strip() in valid_tickets:
            self.log('REQUEST %s' % ticket)
            yield scrapy.Request(
                #url='http://www.fundamentus.com.br/detalhes.php?papel=%s' % value.strip(),
                url='https://statusinvest.com.br/acoes/%s' % ticket,
                callback= self.parse_detail,                
            ) 


        # yield {
        #  "ticket" : value 
        # }

    def parse_detail(self, response):
        
        if response.status == 200:
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
        else:
            yield {
                "request": response.request,
                "status" : response.status
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



