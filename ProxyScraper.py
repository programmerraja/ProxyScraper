import requests as r
from bs4 import BeautifulSoup as soup
import random ,time


class ProxyScraper():
	def __init__(self):
		#free proxy getting site 
		self.plink="https://free-proxy-list.net/"
		#which website we want to reach using proxy
		self.dlink="https://home-cash.work/?ref=5R8CHfUKd"
		#array used to store proxy detaills
		self.proxy_array=[]
		self.getProxy()
		self.scrapWebsite()

	def getProxy(self):
		html_code=r.get(self.plink)
		proxyscraper=soup(html_code.text,"html.parser")
		table = proxyscraper.find("table")
		table_body=  table.find("tbody")
		rows=table_body.find_all("tr")
		for row in rows:
			#getting proxy table 
			proxy=row.find_all("td")[0].text 
			#getting port number from table 
			port=row.find_all("td")[1].text
			#getting if it is  number from table 
			ishttps=row.find_all("td")[5].text
			#checking if it has https
			if(str(ishttps)=="yes"):
				self.proxy_array.append("https://"+proxy+":"+port)
			else:
				self.proxy_array.append("http://"+proxy+":"+port)

			
	
	def scrapWebsite(self):
		random .shuffle(self.proxy_array)  
		try:
			for i in range(0,10):
				if(i<=len(self.proxy_array)):
				  proxy=self.proxy_array[i]
				  #write you own code for scrap a website 
				  res=r.get(self.dlink,proxies={"http":proxy,"http":proxy})
				  print(res)
				  #sleep function to call after few sec
				  time.sleep(random.randint(0,10))
		except Exception as e:
			print(e)



ProxyScraper()