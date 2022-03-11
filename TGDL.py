from typing import List
from requests import get, Response
from time import sleep
from random import choice
from subprocess import run, check_output
import config

class TelegraphDownloader:

	def check_access_link(self, date_file:List[str], input_words:List[str]) -> List[str]:
		listw:List[str] = []

		for key_word in input_words:
			for date in date_file:

				triger = "<Response 200>"
				test:Response = get("http://telegra.ph/"+key_word+date, headers = choice(config.UserAgentM))

				if str(test) == triger:					
					listw.append(str("http://telegra.ph/"+key_word+date))
					
				else:
					open("error_links.log",'a').write(str("http://telegra.ph/"+key_word+date))
				sleep(3)

		return listw

	def download_file(self, url_ls:List[str], file_types:str) -> None:

		for url in url_ls:

			dir_downloads:str = 'photos/sort'
			run(['wget', '-nd', '-r', '-P', dir_downloads,'-A', file_types, url])
			sleep(7)

	@staticmethod
	def ls_files() -> List[str]: 
		dir_downloads:str = "photos/sort"
		text_output:str = check_output(["ls", "-1", dir_downloads], universal_newlines=True)

		return text_output.split('\n')[:-1]

	def rename_files(self, name_new_dir:str) -> None:
		s = 0
		files:List[str] = TelegraphDownloader.ls_files()
		
		run(["mkdir","photos/full/"+name_new_dir])

		sorted_dir = 'photos/full/'+name_new_dir+"/file"+str(s+1) 

		for i in range(len(files)):

			if files[i][-4] == '.': 
				run([ 'mv', "photos/sort/"+files[i], sorted_dir + files[i][-4:] ])

			else: 
				run([ 'mv', "photos/sort/"+files[i], sorted_dir + files[i][-5:] ])

tgdl = TelegraphDownloader()