import scrapy
import os

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import items


class PoEAffixSpider(scrapy.Spider):
    """Scrapy spider to extra item affix data from the PoE website
        """
    name = "poeaffix"
    allowed_domains = ["pathofexile.com"]
    start_urls = [
        #"https://www.pathofexile.com/item-data/weapon",
        "https://www.pathofexile.com/item-data/prefixmod",
        "https://www.pathofexile.com/item-data/suffixmod",
        #os.path.join("C:", "Users", "Brian", "Documents", "GitHub", "poe-django-site", "poe_site",
        #             "utils", "poe_data_retrieval", "item-data.html")
    ]

    def parse(self, response):
        item_affix_blocks = response.css('div.layoutBox1.layoutBoxFull.defaultTheme')
        filename = response.url.split('/')[-1] + '.tsv'
        with open(filename, 'w') as affix_file:
            affix_file.write("name\ttier_number\tilvl\tdescription\tvalue\n")
            for block in item_affix_blocks:
                # Get the affix type
                affix_block = items.PoEAffixBlock()
                #print "Created affix block"
                affix_type = block.css('h1.topBar.last.layoutBoxTitle::text').extract()[0]
                #print affix_type
                affix_block["affix_type"] = affix_type
                # Ignore first row of table, contains the headers
                affix_tier_data = block.xpath('.//div[@class="layoutBoxContent"]/table[@class="itemDataTable"]/tr')
                #affix_block["affix_data"] = \
                #self.extract_affix_tiers(affix_tier_data)
                affix_tiers = {}
                affix_tier = len(affix_tier_data)
                for tier in affix_tier_data[1:]:
                    tier_data = items.PoEAffixItem()
                    affix_name = tier.css('td.name::text').extract()[0]
                    tier_table_cells = tier.xpath('.//td')
                    affix_nr = str(affix_tier)
                    affix_ilvl = tier_table_cells[1].xpath('text()').extract()[0]
                    affix_description = tier_table_cells[2].xpath('text()').extract()[0]
                    affix_value = tier_table_cells[3].xpath('text()').extract()[0]
                    affix_tier -= 1
                    affix_file.write("{}\t{}\t{}\t{}\t{}\n".format(affix_name, affix_nr, affix_ilvl, affix_description, affix_value))

    def extract_affix_tiers(self, affix_tier_data):
        affix_tiers = {}
        affix_tier = len(affix_tier_data)
        for tier in affix_tier_data:
            tier_data = items.PoEAffixItem()
            affix_name = tier.css('td.name::text').extract()[0]
            tier_table_cells = tier.css('td').extract()
            affix_nr = str(affix_tier)
            affix_ilvl = tier_table_cells[1].xpath('text()').extract()[0]
            affix_description = tier_table_cells[2].xpath('text()').extract()[0]
            affix_value = tier_table_cells[3].xpath('text()').extract()[0]
            print "Tier info: {} - tiernr: {} - ilvl: {} - desc: {} - val: {}".format(affix_name, affix_nr, affix_ilvl, affix_description, affix_value)

        return affix_tiers
