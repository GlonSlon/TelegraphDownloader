from subprocess import check_output, run
from typing	import List

class Rename:

	@staticmethod
	def ls_files() -> List[str]: #Составление списка файлов для переименования

		dir_downloads:str = "photos/sort"
		text_output:str = check_output(["ls", "-1", dir_downloads], universal_newlines=True)

		return text_output.split('\n')[:-1]

	@staticmethod
	def rename_files(name_new_dir:str) -> None: #Переименование файлов

		s:int = 0
		files:List[str] = Rename.ls_files()
		
		run(["mkdir","photos/full/"+name_new_dir])#Создаем новую директорию для переименнованных файлов 

		for i in range(len(files)):

			if files[i][-4] == '.': 
				run([ 'mv', "photos/sort/"+files[i], 'photos/full/'+name_new_dir+"/file"+str(s+1) + files[i][-4:] ])

			else: 
				run([ 'mv', "photos/sort/"+files[i], 'photos/full/'+name_new_dir+"/file"+str(s+1) + files[i][-5:] ])