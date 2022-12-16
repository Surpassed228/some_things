from csv import*
from pickle import*
from random import*


#Словарь ниже создаю для дальнейшего испоьзования его в качестве некоторого контейнера, в который буду сохранять данные из файлов во внутренний модуль
main_dict = dict()
#Функция ниже - функция по загрузке данных из файлов csv,pickle,txt. В качестве аргументов она принимает 1)type - тип файла, который пользователь хочет загрузить (это может быть txt pickle или csv,)
#Если это не один один из этих фацлов вылезает ошибка ValueError("Неправильный тип файла"). Вторая переменная отвечает за путь,в ктором распологается нужный файл. Функция после загрузки данных файла 
# во внутр пямятьь добавляет их в список the_num = list() и в конце возращает этот список через return
def load_table (type, path):
	if type.strip() == "csv":
		the_num = list()
		with open(path,"r") as file:
			kk = reader(file)
			for n in kk:
				the_num.append(n)
		return the_num
	elif type.strip() == "txt":
		the_num = list()
		with open(path,"r") as file:
			for n in file:
				the_num.append(n.rstrip("\n")) # тут испольщую rstrip() чтобы при добавлении в список строк из тхт файла там не было \n переход на след строку
		return the_num
	elif type.strip() == "pickle":
		the_num = list()
		with open(path,"rb") as file:
			try:
				while True:
					the_num.append(load(file))
			except EOFError: #ошибка при которой в фале pickle заканчиваются данные но при этом пользователь все равно вызывает функция load()
				pass
		return the_num
	else:
		raise ValueError("Неправильный тип файла")





#Данная функция в зависимости от выбранного типа фала (types) сохраняет данные из одного файла (path1) в другой файл(path2) это сохранение из внутреннего представления модуля 
#Функция также сохраняет данные во внутренее представления модуля которое представленно в виде словаря 
#Для csv и txt файлов строки можно получить обратившись к ключам словаря "1 string","2 string","3 string" и тд. для pickle же к обектам можно получить достум обратившись к ключам словаря 
#"1 object", "2 object", "3 object" и тд.
#Если это не один один из фацлов csv pickle txt вылезает ошибка ValueError("Неправильный тип файла").
def save_table(types,path1,path2):
	if types.strip() == "csv":
		main_dict.clear()
		the_list1 = list()
		for n in range(len(load_table(types,path1))):
			main_dict[str(n+1) + " " + "string"] = load_table(types,path1)[n]
		for n in load_table(types,path1):
			the_list1.append(n)
		with open(path2,"w",newline = "\n") as file:
			cfile = writer(file)
			for n in the_list1:
				cfile.writerow(n)
	elif types.strip() == "pickle":
		main_dict.clear()
		the_list1 = list()
		for n in load_table(types,path1):
			the_list1.append(n)
		for n in range(len(the_list1)):
			main_dict[str(n+1) + " " + "object"] = the_list1[n]
		with open(path2,"wb") as file:
			for n in the_list1:
				for k in n:
					dump(k,file)
	elif types.strip() == "txt":
		main_dict.clear()
		the_list1 = list()
		for n in range(len(load_table(types,path1))):
			main_dict[str(n+1) + " " "string"] = load_table(types,path1)[n]
		for n in load_table(types,path1):
			the_list1.append(n)
		the_list2 = list(n + "\n" for n in the_list1)
		with open(path2,"w") as file:
			file.writelines(the_list2)
	else:
		raise ValueError("Неправильный тип файла")




#Данная функция возращает список из строк в таблице формата csv. С какой строки начать и на какой строке закончить выбирает пользователь. Если переменная stop не уточняется, то 
#фукция начинает с определенной строки start  и итерируется до конца
def get_rows_by_number(path,start, stop = None):
	main_list = list()
	the_list_of_rows = list()
	if stop == None:
		with open(path,"r") as file:
			csv = reader(file)
			for n in csv:
				the_list_of_rows.append(n)
			try:
				a = the_list_of_rows[start-1]
			except IndexError:
				print ("Строки с данным индексом нету в таблице!")
				return "NONE"
		try:
			main_list.append(the_list_of_rows[start-1:])
			return main_list[0]
		except IndexError:
			print ("Строки с данным индексом нету в таблице!")
	else:
		with open(path,"r") as file:
			csv = reader(file)
			for n in csv:
				the_list_of_rows.append(n)
			try:
				a = the_list_of_rows[stop-1]
			except IndexError:
				print ("Строки с данным индексом нету в таблице!")
				return "NONE"
		try:
			main_list.append(the_list_of_rows[start-1:stop])
			return main_list[0]
		except IndexError:
			print ("Строки с данным индексом нету в таблице!")






#Данная функция возращает все занчания таблицы вида csv в выбранной строке или в выбранном столбце
def get_rows_by_index(path,index = None,indexN = None):
	the_list_of_rows = list()
	with open(path) as file:
		csv = reader(file)
		for n in csv:
			the_list_of_rows.append(n)
	if indexN == None:
		try:
			return the_list_of_rows[index-1]
		except IndexError:
			print("У данной таблицы нету строки с таким индексом!")
		except TypeError:
			pass
	if index == None:
		another_one = list()
		try:
			for n in the_list_of_rows:
				another_one.append(n[indexN-1])
			return another_one
		except IndexError:
			print("У таблицы нету столбца с таким индексом!")
		except TypeError:
			pass
	if index == None and indexN == None:
		print("Вы должны ввести либо номер строки либо номер стобца, который вы хотите отобразить")
	if index != None and indexN != None:
		print('Вы должны выбрать либо строку либо стобец')




#Данная функция берет выбранный столбец из таблицы формата csv (столбец выбирает пользователь переменная column_num) и возращает словарь со всемы эелемнтами 
#из этого столбца в качестве ключей а в каестве значений у словаря это тип этих элементов (int,float,bool или str)
def get_column_types (path,column_num):
	the_main_list = list()
	with open(path,"r",newline = "\n") as file:
		sss = reader(file)
		for n in sss:
			the_main_list.append(n)
	new_list1 = list([] for n in range(len(the_main_list)))
	for n in the_main_list:
		for k in range(len(n)):
			try:
				zzz = int(n[k])
				new_list1[the_main_list.index(n)].append("int")
			except ValueError:
				try:
					zzz = float(n[k])
					new_list1[the_main_list.index(n)].append("float")
				except ValueError:
					if n[k].upper() == "true".upper() or n[k].upper() == "false".upper():
						new_list1[the_main_list.index(n)].append("bool")
					else:
						new_list1[the_main_list.index(n)].append('str')
	otvet = list()
	try:
		for n in new_list1:
			otvet.append(n[column_num-1])
	except IndexError:
		return print("У данной таблицы нету столбца с таким индексом!")

	otvet1 = list()
	try:
		for n in the_main_list:
			otvet1.append(n[column_num-1])
	except IndexError:
		return print("У данной таблицы нету столбца с таким индексом!")
	the_dict = dict(zip(otvet1,otvet))
	return the_dict




#Данная функция возращает типизированный по значнию столбец выбираемый пользователем.Функция возращает значапния из столбца БЕЗ названия самого столбца. считаю что название столбца
#это его первое значение
def get_values(path,column = 1):
	the_main_list = list()
	with open(path,"r", newline = "\n") as file:
		kkk = reader(file)
		for n in kkk:
			the_main_list.append(n)
	if type(column) == int:
		new_list = list()
		try:
			for n in the_main_list:
				new_list.append(n[column-1])
		except IndexError:
			return print("У данной таблицы нету столбца с таким индексом!")
		new_list1 = list(new_list[1:])
		if new_list[0].lower() == "str":
			otvet = list(n for n in new_list1)
			return otvet
		elif new_list[0].lower() == "int":
			otvet = list(int(n) for n in new_list1)
			return otvet
		elif new_list[0].lower() == "float":
			otvet = list(float(n) for n in new_list1)
			return otvet
		elif new_list[0].lower() == "bool":
			otvet = list(n.lower().title() for n in new_list1)
			otvet1 = list()
			for n in otvet:
				if n == "True":
					k = True
					otvet1.append(k)
				else:
					otvet1.append(False)
			return otvet1
	else:
		column_list = list()
		the_one = list(n.lower() for n in the_main_list[0])
		if column.lower() == "str":
			column_list.clear()
			for n in the_main_list:
				column_list.append(n[the_one.index("str")])
			rra = list(column_list[1:])
			return rra
		elif column.lower() == "int":
			column_list.clear()
			for n in the_main_list:
				column_list.append(n[the_one.index("int")])
			rra = list(column_list[1:])
			rra1 = list(int(n) for n in rra)
			return rra1
		elif column.lower() == "float":
			column_list.clear()
			for n in the_main_list:
				column_list.append(n[the_one.index("float")])
			rra = list(column_list[1:])
			rra1 = list(float(n) for n in rra)
			return rra1
		elif column.lower() == "bool":
			column_list.clear()
			for n in the_main_list:
				column_list.append(n[the_one.index("bool")])
			rra = list(column_list[1:])
			rra1 = list()
			for n in rra:
				if n.lower().title() == "True":
					rra1.append(True)
				else:
					rra1.append(False)
			return rra1


#Данная функция возращает типизированное значения из таблицы с одной стракой и с названиями значний 
def get_value(path,column):
	the_main_list = list()
	with open(path,"r",newline = "\n") as file:
		suck = reader(file)
		for n in suck:
			the_main_list.append(n)
	the_nec = list()
	try:
		for n in the_main_list:
			the_nec.append(n[column-1])
	except IndexError:
		print("Нету столбца с таким номером")
	if the_nec[0] == "float":
		return float(the_nec[1])
	elif the_nec[0] == "int":
		return int(the_nec[1])
	elif the_nec[0] == "str":
		return the_nec[1]
	elif the_nec[0] == "bool":
		if the_nec[1].lower().title() == "True":
			return True
		else:
			return False




#Данная функция печатает таблицу 
def print_table (path):
	the_main_list = list()
	with open(path,"r",newline = "\n") as file:
		sk = reader(file)
		for n in sk:
			the_main_list.append(n)
	for n in the_main_list:
		for k in range(len(n)):
			print(n[k],",",end = " ")
		print("\n")
	return " "


#Данная функция в качестве аргументов принимает a)values список изэлементов которые могут быть всех четырех типов  b)path аргумент отвечает за цсв таблицу с четырьмя столбцами 
#str int float bool(в этом порядке). функция берет список и добавляет соотыветсвующие элементы к соответсвующюм столбцами файла
def set_values(values,path):
	the_main_list = list()
	with open(path,"r",newline = "\n") as file:
		sk = reader(file)
		for n in sk:
			the_main_list.append(n)
	kk = list([] for n in range(len(the_main_list[0])))
	the_dictionary = dict(zip(the_main_list[0],kk))
	for n in the_dictionary.keys():
		n = n.lower()
	for n in values:
		if type(n) == str:
			the_dictionary["str"].append(n)
		elif type(n) == float:
			the_dictionary["float"].append(str(n))
		elif type(n) == int:
			the_dictionary["int"].append(str(n))
		elif type(n) == bool:
			the_dictionary["bool"].append(str(n))
	int_index = the_main_list[0].index("int") 
	float_index = the_main_list[0].index("float") 
	str_index = the_main_list[0].index("str") 
	bool_index = the_main_list[0].index("bool") 
	one = list()
	for m in the_dictionary.values():
		one.append(len(m))
	ama = max(one)
	for m in the_dictionary.values():
		while len(m)<ama:
			m.append("--")
	listlist = list([] for n in range(ama))
	for n in listlist:
		for k in range(4):
			n.append("+")

	for n in the_dictionary["str"]:
		a1 = the_dictionary["str"].index(n)
		listlist[the_dictionary["str"].index(n)].insert(str_index,n)
		del the_dictionary["str"][a1]
		the_dictionary["str"].insert(a1,0000000000000000)

	for n in the_dictionary["int"]:
		a1 = the_dictionary["int"].index(n)
		listlist[the_dictionary["int"].index(n)].insert(int_index,n)
		del the_dictionary["int"][a1]
		the_dictionary["int"].insert(a1,0000000000000000)


	for n in the_dictionary["float"]:
		a1 = the_dictionary["float"].index(n)
		listlist[the_dictionary["float"].index(n)].insert(float_index,n)
		del the_dictionary["float"][a1]
		the_dictionary["float"].insert(a1,0000000000000000)


	for n in the_dictionary["bool"]:
		a1 = the_dictionary["bool"].index(n)
		listlist[the_dictionary["bool"].index(n)].insert(bool_index,n)
		del the_dictionary["bool"][a1]
		the_dictionary["bool"].insert(a1,0000000000000000)

	for n in listlist:
		while "+" in n:
			n.remove("+")

	with open(path,"w",newline = "\n") as file:
		sss = writer(file)
		sss.writerow(the_main_list[0])
		sss.writerows(listlist)
	return "Alright, now check the table!"


#Данная функция в качестве аргументов принимает a)values одно значение тип bool str int float b)path аргумент отвечает за цсв таблицу с четырьмя столбцами 
#str int float bool(в этом порядке). функция берет значение и добавляет его к соответсвующему столбцу файла (str int float bool)(в таком порядке)
def set_value (value2,path):
	the_main_list = list()
	with open(path,"r",newline = "\n") as file:
		sss = reader(file)
		for n in sss:
			the_main_list.append(n)
	the_lower = list(n.lower() for n in the_main_list[0])

	if type(value2) == str:
		with open(path,"w",newline = "\n") as file:
			sss =  writer(file)
			sss.writerow(the_main_list[0])
			sss.writerow([value2,"--","--","--"])
	elif type(value2) == int:
		mmm = str(value2)
		with open(path,"w",newline = "\n") as file:
			sss =  writer(file)
			sss.writerow(the_main_list[0])
			sss.writerow(["--",mmm,"--","--"])
	elif type(value2) == float:
		mmm = str(value2)
		with open(path,"w",newline = "\n") as file:
			sss =  writer(file)
			sss.writerow(the_main_list[0])
			sss.writerow(["--","--",mmm,"--"])
	elif type(value2) == bool:
		mmm = str(value2).upper()
		with open(path,"w",newline = "\n") as file:
			sss =  writer(file)
			sss.writerow(the_main_list[0])
			sss.writerow(["--","--","--",mmm])
	return "Check the file"








#функция принимает в качестве аргусента словарь ключи которого это номера(номера должны быть типа int) интерисуемых столбцов в таблице (номера начинаются с 1,2,3,4.....)
#значения же словаря должны быть значения (int str float bool). Функция создает указанное количесво (num) рандомных обьектов нужного типа и пишет их в выбранные столбцы согласн  словарю
def set_column_types(path,dictr,num):
	lst_of_nums = list(n for n in dictr.keys())
	empty_lists = list([] for n in range(max(lst_of_nums)))
	a = lst_of_nums[0]
	for n in lst_of_nums:
		if dictr[n].lower() == "float":
			for k in range(num):
				empty_lists[n-1].append(round(uniform(1.1,9.9),3))
		elif dictr[n].lower() == "int":
			for k in range(num):
				empty_lists[n-1].append(randint(1,99))
		elif dictr[n].lower() == "bool":
			bols = [True,False]
			for k in range(num):
				empty_lists[n-1].append(str(choice(bols)))
		elif dictr[n].lower() == "str":
			letters = ["q","w","e","r","t","a","v","b","n","1","2","6","g","h","z"]
			for k in range(num):
				a = str()
				while len(a) < 4:
					a += choice(letters)
				empty_lists[n-1].append(a)
		else:
			print("Значения должны быть одним из четырех видов: 1)str 2)int 3)float 4)bool ")

	for n in empty_lists:
		if len(n) == 0:
			for k in range(num):
				n.append("---")


	with open(path,"w",newline = "\n") as file:
		sss = writer(file)
		for n in range(len(empty_lists[0])):
			samka = list()
			for k in empty_lists:
				samka.append(k[n])
			sss.writerow(samka)

	return "Check the table!"





#ДОПОЛНИТЕЛЬНЫОЕ ЗАДАНИЕ №7 (сложность 3)


#Во всех фнкциях ние first - первая колонка для сравнения , second - вторая колонка для сравненя

def eq (path,first,second):
	try:

		just_list = list()
		with open(path,"r",newline = "\n") as file:
			sss = reader(file)
			for n in sss:
				just_list.append(n)
		first_one = list(n[first-1] for n in just_list)
		second_one = list(n[second-1] for n in just_list)
		the_bool_list = list()
		ttt = dict()
		for n in range(len(first_one)):
			if len(first_one[n]) == len(second_one[n]):
				the_bool_list.append(True)
			else:
				the_bool_list.append(False)
		return the_bool_list
	except IndexError:
		print("Нету столбца с таким индексом. Индексация начинается с 1")
		return " "





def ne (path,first,second):
	try:

		just_list = list()
		with open(path,"r",newline = "\n") as file:
			sss = reader(file)
			for n in sss:
				just_list.append(n)
		first_one = list(n[first-1] for n in just_list)
		second_one = list(n[second-1] for n in just_list)
		the_bool_list = list()
		ttt = dict()
		for n in range(len(first_one)):
			if len(first_one[n]) != len(second_one[n]):
				the_bool_list.append(True)
			else:
				the_bool_list.append(False)
		return the_bool_list
	except IndexError:
		print("Нету столбца с таким индексом. Индексация начинается с 1")
		return " "




def gr (path,first,second):
	try:

		just_list = list()
		with open(path,"r",newline = "\n") as file:
			sss = reader(file)
			for n in sss:
				just_list.append(n)
		first_one = list(n[first-1] for n in just_list)
		second_one = list(n[second-1] for n in just_list)
		the_bool_list = list()
		ttt = dict()
		for n in range(len(first_one)):
			if len(first_one[n]) > len(second_one[n]):
				the_bool_list.append(True)
			else:
				the_bool_list.append(False)
		return the_bool_list
	except IndexError:
		print("Нету столбца с таким индексом. Индексация начинается с 1")
		return " "



def ls (path,first,second):
	try:

		just_list = list()
		with open(path,"r",newline = "\n") as file:
			sss = reader(file)
			for n in sss:
				just_list.append(n)
		first_one = list(n[first-1] for n in just_list)
		second_one = list(n[second-1] for n in just_list)
		the_bool_list = list()
		ttt = dict()
		for n in range(len(first_one)):
			if len(first_one[n]) < len(second_one[n]):
				the_bool_list.append(True)
			else:
				the_bool_list.append(False)
		return the_bool_list
	except IndexError:
		print("Нету столбца с таким индексом. Индексация начинается с 1")
		return " "






def ge (path,first,second):
	try:

		just_list = list()
		with open(path,"r",newline = "\n") as file:
			sss = reader(file)
			for n in sss:
				just_list.append(n)
		first_one = list(n[first-1] for n in just_list)
		second_one = list(n[second-1] for n in just_list)
		the_bool_list = list()
		ttt = dict()
		for n in range(len(first_one)):
			if len(first_one[n]) >= len(second_one[n]):
				the_bool_list.append(True)
			else:
				the_bool_list.append(False)
		return the_bool_list
	except IndexError:
		print("Нету столбца с таким индексом. Индексация начинается с 1")
		return " "



def le (path,first,second):
	try:

		just_list = list()
		with open(path,"r",newline = "\n") as file:
			sss = reader(file)
			for n in sss:
				just_list.append(n)
		first_one = list(n[first-1] for n in just_list)
		second_one = list(n[second-1] for n in just_list)
		the_bool_list = list()
		ttt = dict()
		for n in range(len(first_one)):
			if len(first_one[n]) <= len(second_one[n]):
				the_bool_list.append(True)
			else:
				the_bool_list.append(False)
		return the_bool_list
	except IndexError:
		print("Нету столбца с таким индексом. Индексация начинается с 1")
		return " "











save_table("csv","C:\\projects\\fuck.xlsx",)

















	
	
	

























































print(ge("D:\\Projects\\book.csv",1,4))














		











