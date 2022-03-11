from typing import List
from requests import get, Response
from time import sleep
from random import choice
import config

class CheckURL:

	@staticmethod
	def check_access_link(date_file:List[str], input_words:List[str]) -> List[str]:#Проверка существования страницы http://telegra.ph/*

		listw:List[str] = []

		for key_word in input_words:
			for date in date_file:
				
				triger:str = "<Response [200]>"
				test:Response = get("http://telegra.ph/"+key_word+date, headers = choice(config.UserAgentM))

				if str(test) == triger: 
					
					listw.append(str("http://telegra.ph/"+key_word+date))

				sleep(3)

		return listw
