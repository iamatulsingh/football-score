import scrapy
import time
import os
from subprocess import call

class TableSpider(scrapy.Spider):
	name = "table"

	def start_requests(self):
		urls = ["https://www.premierleague.com/tables"]
		for url in urls:
			yield scrapy.Request(url=url, dont_filter=True, callback=self.parse)

	def parse(self,response):
		for i in range(0,10):
			rank = "Rank\t :   %s" %response.xpath("//tr/td[2]/span[contains(@class,'value')]/text()").extract()[i]
			team = "Team\t :   %s" %response.xpath("//span[contains(@class,'long')]/text()").extract()[i]
			team_name = "Team:   %s" %response.xpath("//span[contains(@class,'long')]/text()").extract()[i]
			played = "Played\t :   %s" %response.xpath("//tr/td[4]/text()").extract()[i]
			win = "Win\t :   %s" %response.xpath("//tr/td[5]/text()").extract()[i]
			drawn = "Drawn\t :   %s" %response.xpath("//tr/td[6]/text()").extract()[i]
			lost = "Lost\t :   %s" %response.xpath("//tr/td[7]/text()").extract()[i]
			gf = "GF \t :   %s" %response.xpath("//tr/td[8]/text()").extract()[i]
			ga = "GA \t :   %s" %response.xpath("//tr/td[9]/text()").extract()[i]
			gd = "GD\t :   %s" %response.xpath("//tr/td[10]/text()").extract()[i]

			notificationString = rank + "\n" + played + "\n" + win + "\n" + drawn + "\n" + lost + "\n" + gf + "\n" + ga + "\n" + gd
			print("[#] sending notification for %s" %team_name)
			self.notify(notificationString, team_name)
			time.sleep(10)

	def notify(self,msg, team):
		icon = os.getcwd() + '/PNG/' + team[8:] + '.png'
		call(['notify-send', '-t', '7000', '-i', icon, team[8:], msg])
