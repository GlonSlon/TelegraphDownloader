from typing import *
import check_access
import download_files
import rename_files
import config

class TelegraphDownloader:

	@staticmethod
	def check(key_words:List[str]) -> List[str]:

		return check_access.CheckURL.check_access_link(config.date_postfix , key_words)

	@staticmethod
	def download(urls:List[str], type_file:str) -> None:

		download_files.DownloadFiles.download_file(urls, type_file)

	@staticmethod
	def rename(name_new_dir:str) -> None:

		rename_files.Rename.rename_files(name_new_dir)


def main() -> None:
	
	print("""Введите через запятую ключевые слова.\nПример:\n>anime,films,music,bass-music""")
	key_words_input:str = input("> ")
	key_words_split:List[str] = key_words_input.split(',')
	print("""Какие файлы загружать?\n1.Изображения/GIF\n2.Видео/Аудио\n3.Документы\n4.Всё вместе""")

	while True:
		
		file_type:str = input("Введите 1,2,3 или 4 > ")

		if file_type in ['1','2','3','4']: 
			break

		else:
			print("Ошибка, повторите ввод")
			continue

	print("""Введите имя новой папки для загрузки.""")
	name_dir:str = input("> ")

	links:List[str] = TelegraphDownloader.check(key_words_split)

	print("Создан список действующих ссылок.\n")

	if file_type == '1':
		TelegraphDownloader.download(links, config.FileTypesImg)

	elif file_type == '2':
		TelegraphDownloader.download(links, config.FileTypesVideoAudio)

	elif file_type == '3':
		TelegraphDownloader.download(links, config.FileTypesText)

	elif file_type == '4':
		TelegraphDownloader.download(links, config.FileTypesImg+','+config.FileTypesVideoAudio+','+config.FileTypesText)
	
	print("Загрузка файлов завешена.\nИдет процесс переименования файлов.")

	TelegraphDownloader.rename(name_dir)

main()

