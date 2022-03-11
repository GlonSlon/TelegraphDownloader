from typing import Union, List
from subprocess import run
from time import sleep

class DownloadFiles:

	@staticmethod
	def download_file(url_ls:List[str], file_types:str) -> None: #Выгружаем файлы с сайта, указывая тип файла

		for url in url_ls:

			dir_downloads:str = 'photos/sort'
			
			run(['wget', '-nd', '-r', '-P', dir_downloads,'-A', file_types, url])
			sleep(7)