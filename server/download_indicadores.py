"""
1) Os indicadores criminais do Estado do Rio Grande do Sul 
(https://www.ssp.rs.gov.br/indicadores-criminais), 
entre os anos de 2012 e 2022 foram disponibilizados em planilhas Excel. 
Uma empresa de segurança que irá atuar no RS precisa disponibilizar para 
seus consultores uma interface web por meio da qual possam fazer 
consultas sobre os dados disponibilizados. 
Alguns requisitos essenciais foram definidos:
"""

import httpx
from bs4 import BeautifulSoup as bs
from multiprocessing.pool import ThreadPool
import os

try:
	os.mkdir("indicadores")
	print("Diretório indicadores criado")
except FileExistsError:
	pass

def download_url(url):
	print("downloading: ",url)
	file_name_start_pos = url.rfind("/") + 1
	file_name = f"{os.getcwd()}/indicadores/{url[file_name_start_pos:]}"
	
	r = httpx.get(url)
	if r.status_code == httpx.codes.ok:
		with open(file_name, 'wb') as f:
			f.write(r.content)
	return url

class ParserIndicadores:
	
	"""
	<div class="artigo__texto">
	"""

	def __init__(self):
		self.url_root = 'https://www.ssp.rs.gov.br'
		self.url = 'https://www.ssp.rs.gov.br/indicadores-criminais' 
	
	def __parse(self,text):
		soup = bs(text,features="html.parser")
		artigo__texto = soup.find('div',{'class':'artigo__texto'})
		anos = artigo__texto.find_all('h2') 
		url_downloads = artigo__texto.find_all('a')

		files_links = []
		for url in url_downloads[:12]:
			if url.text:
				files_links.append(f"{self.url_root}{url.get('href')}")

		results = ThreadPool(5).imap_unordered(download_url, files_links)

		for _ in results:
			pass
	
	def __get(self, url):
		r = httpx.get(url)
		self.__parse(r.text)

	def get_indicadores(self):
		r = self.__get(self.url)

# if __name__ == '__main__':
# 	ParserIndicadores().get_indicadores()
