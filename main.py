from typing import List
import config
import TGDL

def main() -> None:
	
	key_words_input:List[str] = input("Введите через запятую ключевые слова.\nПример:\n>anime,films,music,bass-music\n> ").split(',')
	#key_words_split:List[str] = key_words_input.split(',')

	while True:
		file_type = input("Какие файлы загружать?\n1.Изображения/GIF\n2.Видео/Аудио\n3.Документы\n4.Всё вместе\nВведите 1,2,3 или 4 > ")

		if file_type in ['1','2','3','4']: 
			break
		else:
			print("Ошибка, повторите ввод")
			continue

	name_dir = input("Введите имя новой папки для загрузки.\n> ")
	tgdl = TGDL.TelegraphDownloader()
	links:List[str] = tgdl.check_access_link(config.date_postfix, key_words_split)

	print("Создан список действующих ссылок.\n")

	if file_type == '1':
		tgdl.download_file(links, config.FileTypesImg)

	elif file_type == '2':
		tgdl.download_file(links, config.FileTypesVideoAudio)

	elif file_type == '3': 
		tgdl.download_file(links, config.FileTypesText)

	elif file_type == '4':
		tgdl.download_file(links, config.FileTypesImg+','+config.FileTypesVideoAudio+','+config.FileTypesText)
	
	print("Загрузка файлов завешена.\nИдет процесс переименования файлов.")

	tgdl.rename_files(name_dir)
	print(f"Всё готово, файлы находятся в photos/full/{name_dir}")

main()