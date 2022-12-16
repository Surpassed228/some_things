from random import*
from copy import*




#Создаем словарь на базе которого функция принт чесс будет печатать шахматную доскув
#в последствии словарь будет ментся в связи с чем и доска будет менятся 
main_string = "ABCDEFGH"
main_numbers = "12345678"
main_dict = dict()
for n in main_string:
	for k in range(8):
		main_dict[n+main_numbers[k]] = ["•",0]
for n in main_dict.keys():
	if n[1] == "2":
		main_dict[n][0] = "₽"
main_dict["A1"][0] = "R"
main_dict["H1"][0] = "R"
main_dict["B1"][0] = "N"
main_dict["G1"][0] = "N"
main_dict["C1"][0] = "B"
main_dict["F1"][0] = "B"
main_dict["D1"][0] = "Q"
main_dict["E1"][0] = "K"

for n in main_dict.keys():
	if n[1] == "7":
		main_dict[n][0] = "p"
main_dict["A8"][0] = "r"
main_dict["H8"][0] = "r"
main_dict["B8"][0] = "n"
main_dict["G8"][0] = "n"
main_dict["C8"][0] = "b"
main_dict["F8"][0] = "b"
main_dict["D8"][0] = "q"
main_dict["E8"][0] = "k" 

white_list = ["₽","R","N","B","Q","K"]
black_list = ["p","r","n","b","q","k"]





#Это функция принтчесс кторая в качкестве аргумента принимает словарь типа: {"координата фигуры" : [сама фигура,сколько раз фигура ходила]}
#она по данным словаря печатает шахматьную доску

def print_chess (dictionary):
	dic_keys = list()
	for n in dictionary.keys():
		dic_keys.append(n)
	print("\n\n")
	print("                         ------------------------------------")
	print("                                         WHITE               ")
	print("                         ------------------------------------")
	print("                            A   B   C   D   E   F   G   H")
	print("\n")
	print("                    1      ",end = " ")
	for n in dic_keys:
		if n[1] == "1":
			print(dictionary[n][0] + "  ",end = " ")
	print("    1",end = " ")
	print("\n")
	print("                    2      ",end = " ")
	for n in dic_keys:
		if n[1] == "2":
			print(dictionary[n][0] + "  ",end = " ")
	print("    2",end = " ")
	print("\n")
	print("                    3      ",end = " ")
	for n in dic_keys:
		if n[1] == "3":
			print(dictionary[n][0] + "  ",end = " ")
	print("    3",end = " ")
	print("\n")
	print("                    4      ",end = " ")
	for n in dic_keys:
		if n[1] == "4":
			print(dictionary[n][0] + "  ",end = " ")
	print("    4",end = " ")
	print("\n")
	print("                    5      ",end = " ")
	for n in dic_keys:
		if n[1] == "5":
			print(dictionary[n][0] + "  ",end = " ")
	print("    5",end = " ")
	print("\n")
	print("                    6      ",end = " ")
	for n in dic_keys:
		if n[1] == "6":
			print(dictionary[n][0] + "  ",end = " ")
	print("    6",end = " ")
	print("\n")
	print("                    7      ",end = " ")
	for n in dic_keys:
		if n[1] == "7":
			print(dictionary[n][0] + "  ",end = " ")
	print("    7",end = " ")
	print("\n")
	print("                    8      ",end = " ")
	for n in dic_keys:
		if n[1] == "8":
			print(dictionary[n][0] + "  ",end = " ")
	print("    8",end = " ")
	print("\n\n")
	print("                            A   B   C   D   E   F   G   H")
	print("                         ------------------------------------")
	print("                                         BLACK               ")
	print("                         ------------------------------------")






#для каждый фигуры я буду реализова=ыват свой тип функция которая будет в качестве аргумнта принимаеть словарь который будет изменятся 
#и координаты начальные (position) и конечныен (reposition)
#функция фозращает изменненый словарь кототрый в последсвтии блет печататься
def hod_peshki(dictionary,position,reposition):
	white_list = ["₽","R","N","B","Q","K"]
	black_list = ["p","r","n","b","q","k"]
	what = "ABCDEFGH"
	number = what.index(position[0])
	propriety = bool
	some_shit = [what[number - 1],what[number + 1]]


	try:
		if reposition[0] == what[number + 1] or reposition[0] == what[number - 1] or reposition[0] == position[0]:
			propriety = True
		else:
			propriety = False
	except IndexError:
		try:
			if reposition[0] == what[number + 1] or reposition[0] == position[0]:
				propriety = True
			else:
				propriety = False
		except IndexError:
			if reposition[0] == what[number - 1] or reposition[0] == position[0]:
				propriety = True
			else:
				propriety = False
	if propriety == False:
		return "Ваш ход некорректный.Сходите еще раз.", None
	else:
		if dictionary[position][0] == "₽" and reposition[0] == position[0]:
			if int(reposition[1]) < int(position[1]) or int(reposition[1]) == int(position[1]):
				return "Ваш ход некорректный.Сходите еще раз.", None

			initial_num = dictionary[position][1]
			hod_num = int(position[1])
			repos_num = int(reposition[1])
			if abs(hod_num - repos_num) > 2:
				return "Ваш ход некорректный.Сходите еще раз.", None
			elif abs(hod_num - repos_num) == 2:
				if initial_num != 0:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					if dictionary[reposition][0] == "•":
						dictionary[reposition] = copy(dictionary[position])
						dictionary[position] = ["•",0]
						dictionary[reposition][1] += 1
						return dictionary
					elif dictionary[reposition][0] in black_list or dictionary[reposition][0] in white_list:
						return "Ваш ход некорректный.Сходите еще раз.", None
			elif abs(hod_num - repos_num) == 1:
				if dictionary[reposition][0] == "•":
					dictionary[reposition] = copy(dictionary[position])
					dictionary[position] = ["•",0]
					dictionary[reposition][1] += 1
					return dictionary
				else:
					return "Ваш ход некорректный.Сходите еще раз.", None
		elif dictionary[position][0] == "₽" and reposition[0] in some_shit:
			if int(reposition[1]) < int(position[1]) or int(reposition[1]) == int(position[1]):
				return "Ваш ход некорректный.Сходите еще раз.", None

			hod_num = int(position[1])
			repos_num = int(reposition[1])
			if abs(hod_num - repos_num) != 1:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				if dictionary[reposition][0] in black_list:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
				else:
					return "Ваш ход некорректный.Сходите еще раз.", None
		elif dictionary[position][0] == "p" and reposition[0] == position[0]:
			if int(reposition[1]) > int(position[1]) or int(reposition[1]) == int(position[1]):
				return "Ваш ход некорректный.Сходите еще раз.", None

			initial_num = dictionary[position][1]
			hod_num = int(position[1])
			repos_num = int(reposition[1])
			if abs(hod_num - repos_num) > 2:
				return "Ваш ход некорректный.Сходите еще раз.", None
			elif abs(hod_num - repos_num) == 2:
				if initial_num != 0:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					if dictionary[reposition][0] == "•":
						dictionary[reposition] = copy(dictionary[position])
						dictionary[reposition][1] += 1
						dictionary[position] = ["•",0]
						return dictionary
					elif dictionary[reposition][0] in black_list or dictionary[reposition][0] in white_list:
						return "Ваш ход некорректный.Сходите еще раз.", None
			elif abs(hod_num - repos_num) == 1:
				if dictionary[reposition][0] == "•":
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
				else:
					return "Ваш ход некорректный.Сходите еще раз.", None
		elif dictionary[position][0] == "p" and reposition[0] in some_shit:
			if int(reposition[1]) > int(position[1]) or int(reposition[1]) == int(position[1]):
				return "Ваш ход некорректный.Сходите еще раз.", None

			hod_num = int(position[1])
			repos_num = int(reposition[1])
			if abs(hod_num - repos_num) != 1:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				if dictionary[reposition][0] in white_list:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
				else:
					return "Ваш ход некорректный.Сходите еще раз.", None






#данная фунгкция провсеряет не дошла ли вражаская пешка до посленей линнии посредством координат в лосаре
def proverka_peshki(dictionary):
	white_list = ["₽","R","N","B","Q","K"]
	black_list = ["p","r","n","b","q","k"]
	list_of_one = list()
	list_of_eight = list()
	the_ones = list()
	for n in dictionary.keys():
		if n[1] == "1":
			list_of_one.append(n)
	for n in dictionary.keys():
		if n[1] == "8":
			list_of_eight.append(n)
	for n in list_of_one:
		if "p" in dictionary[n]:
			the_ones.append(n)
	for n in list_of_eight:
		if "₽" in dictionary[n]:
			the_ones.append(n)
	if len(the_ones) == 0:
		return False
	else:
		return the_ones




#аналогичная функуия для хода фигуры только для ладь также возращает измененный словарь 
def hod_rook (dictionary,position,reposition):
	yammy1 = ["r","q"]
	yammy2 = ["R","Q"]
	white_list = ["₽","R","N","B","Q","K"]
	black_list = ["p","r","n","b","q","k"]
	main_string = "ABCDEFGH"
	main_numbers = "12345678"
	some_appropriate = list()
	for n in main_numbers:
		some_appropriate.append(position[0]+n)
	for n in main_string:
		some_appropriate.append(n+position[1])
	nick = copy(some_appropriate)
	first_half = nick[0:8]
	second_half = nick[8:]
	if reposition not in some_appropriate:
		return "Ваш ход некорректный.Сходите еще раз.", None
	else:
		
		if dictionary[position][0] in yammy2 and reposition in first_half:
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				if int(position[1]) == int(reposition[1]):
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					if abs(int(position[1]) - int(reposition[1])) == 1:
						dictionary[reposition] = copy(dictionary[position])
						dictionary[reposition][1] += 1
						dictionary[position] = ["•",0]
						return dictionary
					elif 1 < abs(int(position[1]) - int(reposition[1])) < 8:
						if int(position[1]) < int(reposition[1]):
							nums = list(n for n in range(int(position[1])+1,int(reposition[1])+1))
							nums_str = list()
							for n in nums:
								nums_str.append(str(n))
							str11 = list()
							for n in nums_str:
								str11.append(position[0]+n)
							if reposition in str11:
								del str11[str11.index(reposition)]
							indicator = 0
							for n in str11:
								if dictionary[n][0] == "•":
									indicator += 1
								else:
									indicator -= 100
							if indicator > 0:
								dictionary[reposition] = copy(dictionary[position])
								dictionary[reposition][1] += 1
								dictionary[position] = ["•",0]
								return dictionary
							else:
								return "Ваш ход некорректный.Сходите еще раз.", None
						elif int(position[1]) > int(reposition[1]):
							nums = list(n for n in range(int(reposition[1])+1,int(position[1])+1))
							nums_str = list()
							for n in nums:
								nums_str.append(str(n))
							str11 = list()
							for n in nums_str:
								str11.append(position[0]+n)
							if position in str11:
								del str11[str11.index(position)]
							indicator = 0
							for n in str11:
								if dictionary[n][0] == "•":
									indicator += 1
								else:
									indicator -= 100
							if indicator > 0:
								dictionary[reposition] = copy(dictionary[position])
								dictionary[reposition][1] += 1
								dictionary[position] = ["•",0]
								return dictionary
							else:
								return "Ваш ход некорректный.Сходите еще раз.", indicator,str11
		
		elif dictionary[position][0] in yammy2 and reposition in second_half:
			main_string = "ABCDEFGH"
			nec_dict = dict()
			a = 1
			for n in main_string:
				nec_dict[n] = a
				a += 1
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				if nec_dict[position[0]] == nec_dict[reposition[0]]:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					if abs(nec_dict[position[0]] - nec_dict[reposition[0]]) == 1:
						dictionary[reposition] = copy(dictionary[position])
						dictionary[reposition][1] += 1
						dictionary[position] = ["•",0]
						return dictionary
					elif 1 < abs(nec_dict[position[0]] - nec_dict[reposition[0]]) < 8:
						if nec_dict[reposition[0]] > nec_dict[position[0]]:
							num = list(n for n in range(nec_dict[position[0]]+1,nec_dict[reposition[0]]+1))
							sucky_list1 = list(nec_dict.keys())
							sucky_list2 = list()
							for n in num:
								sucky_list2.append(sucky_list1[n-1])
							sucky_list3 = list()
							for n in sucky_list2:
								sucky_list3.append(n+position[1])
							if reposition in sucky_list3:
								del sucky_list3[sucky_list3.index(reposition)] 
							indicator = 0
							for n in sucky_list3:
								if dictionary[n][0] == "•":
									indicator += 1
								else:
									indicator -= 100
							if indicator > 0:
								dictionary[reposition] = copy(dictionary[position])
								dictionary[reposition][1] += 1
								dictionary[position] = ["•",0]
								return dictionary
							else:
								return "Ваш ход некорректный.Сходите еще раз.", None
						elif nec_dict[position[0]] > nec_dict[reposition[0]]:

							num = list(n for n in range(nec_dict[reposition[0]]+1,nec_dict[position[0]]+1))
							sucky_list1 = list(nec_dict.keys())
							sucky_list2 = list()
							for n in num:
								sucky_list2.append(sucky_list1[n-1])
							sucky_list3 = list()
							for n in sucky_list2:
								sucky_list3.append(n+position[1])
							if position in sucky_list3:
								del sucky_list3[sucky_list3.index(position)] 
							indicator = 0
							for n in sucky_list3:
								if dictionary[n][0] == "•":
									indicator += 1
								else:
									indicator -= 100
							if indicator > 0:
								dictionary[reposition] = copy(dictionary[position])
								dictionary[reposition][1] += 1
								dictionary[position] = ["•",0]
								return dictionary
							else:
								return "Ваш ход некорректный.Сходите еще раз.", None
		
		elif dictionary[position][0] in yammy1 and reposition in first_half:
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				if int(position[1]) == int(reposition[1]):
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					if abs(int(position[1]) - int(reposition[1])) == 1:
						dictionary[reposition] = copy(dictionary[position])
						dictionary[reposition][1] += 1
						dictionary[position] = ["•",0]
						return dictionary
					elif 1 < abs(int(position[1]) - int(reposition[1])) < 8:
						if int(position[1]) < int(reposition[1]):
							nums = list(n for n in range(int(position[1])+1,int(reposition[1])+1))
							nums_str = list()
							for n in nums:
								nums_str.append(str(n))
							str11 = list()
							for n in nums_str:
								str11.append(position[0]+n)
							if reposition in str11:
								del str11[str11.index(reposition)]
							indicator = 0
							for n in str11:
								if dictionary[n][0] == "•":
									indicator += 1
								else:
									indicator -= 100
							if indicator > 0:
								dictionary[reposition] = copy(dictionary[position])
								dictionary[reposition][1] += 1
								dictionary[position] = ["•",0]
								return dictionary
							else:
								return "Ваш ход некорректный.Сходите еще раз.", None
						elif int(position[1]) > int(reposition[1]):
							nums = list(n for n in range(int(reposition[1])+1,int(position[1])+1))
							nums_str = list()
							for n in nums:
								nums_str.append(str(n))
							str11 = list()
							for n in nums_str:
								str11.append(position[0]+n)
							if position in str11:
								del str11[str11.index(position)]
							indicator = 0
							for n in str11:
								if dictionary[n][0] == "•":
									indicator += 1
								else:
									indicator -= 100
							if indicator > 0:
								dictionary[reposition] = copy(dictionary[position])
								dictionary[reposition][1] += 1
								dictionary[position] = ["•",0]
								return dictionary
							else:
								return "Ваш ход некорректный.Сходите еще раз.", indicator,str11
		
		elif dictionary[position][0] in yammy1 and reposition in second_half:
			main_string = "ABCDEFGH"
			nec_dict = dict()
			a = 1
			for n in main_string:
				nec_dict[n] = a
				a += 1
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				if nec_dict[position[0]] == nec_dict[reposition[0]]:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					if abs(nec_dict[position[0]] - nec_dict[reposition[0]]) == 1:
						dictionary[reposition] = copy(dictionary[position])
						dictionary[reposition][1] += 1
						dictionary[position] = ["•",0]
						return dictionary
					elif 1 < abs(nec_dict[position[0]] - nec_dict[reposition[0]]) < 8:
						if nec_dict[reposition[0]] > nec_dict[position[0]]:
							num = list(n for n in range(nec_dict[position[0]]+1,nec_dict[reposition[0]]+1))
							sucky_list1 = list(nec_dict.keys())
							sucky_list2 = list()
							for n in num:
								sucky_list2.append(sucky_list1[n-1])
							sucky_list3 = list()
							for n in sucky_list2:
								sucky_list3.append(n+position[1])
							if reposition in sucky_list3:
								del sucky_list3[sucky_list3.index(reposition)] 
							indicator = 0
							for n in sucky_list3:
								if dictionary[n][0] == "•":
									indicator += 1
								else:
									indicator -= 100
							if indicator > 0:
								dictionary[reposition] = copy(dictionary[position])
								dictionary[reposition][1] += 1
								dictionary[position] = ["•",0]
								return dictionary
							else:
								return "Ваш ход некорректный.Сходите еще раз.", None
						elif nec_dict[position[0]] > nec_dict[reposition[0]]:

							num = list(n for n in range(nec_dict[reposition[0]]+1,nec_dict[position[0]]+1))
							sucky_list1 = list(nec_dict.keys())
							sucky_list2 = list()
							for n in num:
								sucky_list2.append(sucky_list1[n-1])
							sucky_list3 = list()
							for n in sucky_list2:
								sucky_list3.append(n+position[1])
							if position in sucky_list3:
								del sucky_list3[sucky_list3.index(position)] 
							indicator = 0
							for n in sucky_list3:
								if dictionary[n][0] == "•":
									indicator += 1
								else:
									indicator -= 100
							if indicator > 0:
								dictionary[reposition] = copy(dictionary[position])
								dictionary[reposition][1] += 1
								dictionary[position] = ["•",0]
								return dictionary
							else:
								return "Ваш ход некорректный.Сходите еще раз.", None






#аналогичная функция только для knights
def hod_knight (dictionary,position,reposition):
	white_list = ["₽","R","N","B","Q","K"]
	black_list = ["p","r","n","b","q","k"]
	a = "ABCDEFGH"
	letters = list(n for n in a[2:6])
	letters1 = []
	nec_num = ["3","4","5","6"]
	nec_num1 = []
	if position[0] in letters and position[1] in nec_num:
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position[0] == "A" and position[1] in nec_num:
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index("A")+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index("A")+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index("A")+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index("A")+2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index("A")+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index("A")+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index("A")+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index("A")+2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position[0] == "H" and position[1] in nec_num:
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index("H")-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index("H")-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index("H")-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index("H")-2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index("H")-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index("H")-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index("H")-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index("H")-2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.1", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position[0] == "B" and position[1] in nec_num:
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index("B")-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index("B")-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index("B")+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index("B")+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index("B")+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index("B")+2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index("B")-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index("B")-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index("B")+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index("B")+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index("B")+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index("B")+2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary

	elif position[0] == "G" and position[1] in nec_num:
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index("G")+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index("G")+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index("G")-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index("G")-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index("G")-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index("G")-2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index("G")+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index("G")+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index("G")-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index("G")-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index("G")-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index("G")-2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position[0] in letters and position[1] == "1":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position[0] in letters and position[1] == "8":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position[0] in letters and position[1] == "2":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position[0] in letters and position[1] == "7":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position == "A8":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position == "H8":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position == "A1":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position == "H1":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position == "B8":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position == "G8":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary

	elif position == "B1":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position == "G1":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position == "A7":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position == "H7":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary



	elif position == "A2":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
	elif position == "H2":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary

	elif position == "B7":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary

		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary

	elif position == "G7":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary

		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])-2))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary



	elif position == "B2":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary

		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])+2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary

	elif position == "G2":
		if dictionary[position][0] == "N":
			if dictionary[reposition][0] in white_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary

		elif dictionary[position][0] == "n":
			if dictionary[reposition][0] in black_list:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dop_znach = list()
				dop_znach.append(a[a.index(position[0])+1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])-1] + str(int(position[1])+2))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])+1))
				dop_znach.append(a[a.index(position[0])-2] + str(int(position[1])-1))
				if reposition not in dop_znach:
					return "Ваш ход некорректный.Сходите еще раз.", None
				else:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary




#аналогичная функция для слонов
def hod_bishop(dictionary,position,reposition):
	white_list = ["₽","R","N","B","Q","K"]
	black_list = ["p","r","n","b","q","k"]




	first_diag = list([] for n in range(15))
	second_diag = list([] for n in range(15))
	first_diag[0].append("A8")
	first_diag[1].append("A7")
	first_diag[1].append("B8")
	mums2 = ["6","7","8"]
	mums3 = ["5","6","7","8"]
	mums4 = ["4","5","6","7","8"]
	mums5 = ["3","4","5","6","7","8"]
	mums6 = ["2","3","4","5","6","7","8"]
	mums7 = ["1","2","3","4","5","6","7","8"]
	mums8 = ["1","2","3","4","5","6","7"]
	mums9 = ["1","2","3","4","5","6"]
	mums10 = ["1","2","3","4","5"]
	mums11 = ["1","2","3","4"]
	mums12 = ["1","2","3"]
	mums13 = ["1","2"]
	mums14 = ["1"]
	let2 = "ABC"
	let3 = "ABCD"
	let4 = "ABCDE"
	let5 = "ABCDEF"
	let6 = "ABCDEFG"
	let7 = "ABCDEFGH"
	let8 = "BCDEFGH"
	let9 = "CDEFGH"
	let10 = "DEFGH"
	let11 = "EFGH"
	let12 = "FGH"
	let13 = "GH"
	let14 = "H"

	sucks2 = list()
	for n in range(len(let2)):
		sucks2.append(let2[n] + mums2[n])
	sucks3 = list()
	for n in range(len(let3)):
		sucks3.append(let3[n] + mums3[n])
	sucks4 = list()
	for n in range(len(let4)):
		sucks4.append(let4[n] + mums4[n])
	sucks5 = list()
	for n in range(len(let5)):
		sucks5.append(let5[n] + mums5[n])
	sucks6 = list()
	for n in range(len(let6)):
		sucks6.append(let6[n] + mums6[n])
	sucks7 = list()
	for n in range(len(let7)):
		sucks7.append(let7[n] + mums7[n])
	for n in sucks2:
		first_diag[2].append(n)
	for n in sucks3:
		first_diag[3].append(n)
	for n in sucks4:
		first_diag[4].append(n)
	for n in sucks5:
		first_diag[5].append(n)
	for n in sucks6:
		first_diag[6].append(n)
	for n in sucks7:
		first_diag[7].append(n)
	sucks8 = list()
	for n in range(len(let8)):
		sucks8.append(let8[n] + mums8[n])
	sucks9 = list()
	for n in range(len(let9)):
		sucks9.append(let9[n] + mums9[n])
	sucks10 = list()
	for n in range(len(let10)):
		sucks10.append(let10[n] + mums10[n])
	sucks11 = list()
	for n in range(len(let11)):
		sucks11.append(let11[n] + mums11[n])
	sucks12 = list()
	for n in range(len(let12)):
		sucks12.append(let12[n] + mums12[n])
	sucks13 = list()
	for n in range(len(let13)):
		sucks13.append(let13[n] + mums13[n])
	sucks14 = list()
	for n in range(len(let14)):
		sucks14.append(let14[n] + mums14[n])
	for n in sucks8:
		first_diag[8].append(n)
	for n in sucks9:
		first_diag[9].append(n)
	for n in sucks10:
		first_diag[10].append(n)
	for n in sucks11:
		first_diag[11].append(n)
	for n in sucks12:
		first_diag[12].append(n)
	for n in sucks13:
		first_diag[13].append(n)
	for n in sucks14:
		first_diag[14].append(n)
	second_diag[0].append("H8")
	second_diag[1].append("H7")
	second_diag[1].append("G8")
	fck2 = "HGF"
	fck3 = "HGFE"
	fck4 = "HGFED"
	fck5 = "HGFEDC"
	fck6 = "HGFEDCB"
	fck7 = "HGFEDCBA"
	fck8 = "GFEDCBA"
	fck9 = "FEDCBA"
	fck10 = "EDCBA"
	fck11 = "DCBA"
	fck12 = "CBA"
	fck13 = "BA"
	fck14 = "A"

	fucks2 = list()
	for n in range(len(fck2)):
		fucks2.append(fck2[n] + mums2[n])
	fucks3 = list()
	for n in range(len(fck3)):
		fucks3.append(fck3[n] + mums3[n])
	fucks4 = list()
	for n in range(len(fck4)):
		fucks4.append(fck4[n] + mums4[n])
	fucks5 = list()
	for n in range(len(fck5)):
		fucks5.append(fck5[n] + mums5[n])
	fucks6 = list()
	for n in range(len(fck6)):
		fucks6.append(fck6[n] + mums6[n])
	fucks7 = list()
	for n in range(len(fck7)):
		fucks7.append(fck7[n] + mums7[n])


	fucks8 = list()
	for n in range(len(fck8)):
		fucks8.append(fck8[n] + mums8[n])
	fucks9 = list()
	for n in range(len(fck9)):
		fucks9.append(fck9[n] + mums9[n])
	fucks10 = list()
	for n in range(len(fck10)):
		fucks10.append(fck10[n] + mums10[n])
	fucks11 = list()
	for n in range(len(fck11)):
		fucks11.append(fck11[n] + mums11[n])
	fucks12 = list()
	for n in range(len(fck12)):
		fucks12.append(fck12[n] + mums12[n])
	fucks13 = list()
	for n in range(len(fck13)):
		fucks13.append(fck13[n] + mums13[n])
	fucks14 = list()
	for n in range(len(fck14)):
		fucks14.append(fck14[n] + mums14[n])
	for n in fucks2:
		second_diag[2].append(n)
	for n in fucks3:
		second_diag[3].append(n)
	for n in fucks4:
		second_diag[4].append(n)
	for n in fucks5:
		second_diag[5].append(n)
	for n in fucks6:
		second_diag[6].append(n)
	for n in fucks7:
		second_diag[7].append(n)
	for n in fucks8:
		second_diag[8].append(n)
	for n in fucks9:
		second_diag[9].append(n)
	for n in fucks10:
		second_diag[10].append(n)
	for n in fucks11:
		second_diag[11].append(n)
	for n in fucks12:
		second_diag[12].append(n)
	for n in fucks13:
		second_diag[13].append(n)
	for n in fucks14:
		second_diag[14].append(n)



	if dictionary[position][0] == "Q" or dictionary[position][0] == "B":
		if dictionary[reposition][0] in white_list:
			return "Ваш ход некорректный.Сходите еще раз.", None
		else:
			mamka1 = list()
			for n in range(len(first_diag)):
				if position in first_diag[n]:
					mamka1 = copy(first_diag[n])
					break
			mamka2 = list()
			for n in range(len(second_diag)):
				if position in second_diag[n]:
					mamka2 = copy(second_diag[n])
					break
			if reposition not in mamka1 and reposition not in mamka2:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				sumka = list()
				my_mother = [mamka1,mamka2]
				for n in range(2):
					if reposition in my_mother[n]:
						sumka = copy(my_mother[n])
						break
				if abs(sumka.index(reposition)-sumka.index(position)) == 1:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
				else:
					if int(position[1]) > int(reposition[1]):
						kkk = sumka[sumka.index(position)+1:sumka.index(reposition)+1]
						if reposition in kkk:
							kkk.remove(reposition)
						indicator = 0
						for n in kkk:
							if n == "•":
								indicator += 1
							else:
								indicator -= 100
						if indicator >= 0:
							dictionary[reposition] = copy(dictionary[position])
							dictionary[reposition][1] += 1
							dictionary[position] = ["•",0]
							return dictionary
						else:
							return indicator,"Ваш ход некорректный.Сходите еще раз.1", None
					elif int(reposition[1]) > int(position[1]):
						kkk = sumka[sumka.index(reposition)+1:sumka.index(position)+1]
						if position in kkk:
							kkk.remove(position)
						indicator = 0
						for n in kkk:
							if n == "•":
								indicator += 1
							else:
								indicator -= 100
						if indicator >= 0:
							dictionary[reposition] = copy(dictionary[position])
							dictionary[reposition][1] += 1
							dictionary[position] = ["•",0]
							return dictionary
						else:
							return indicator,"Ваш ход некорректный.Сходите еще раз.", None



	elif dictionary[position][0] == "q" or dictionary[position][0] == "b":
		if dictionary[reposition][0] in black_list:
			return "Ваш ход некорректный.Сходите еще раз.", None
		else:
			mamka1 = list()
			for n in range(len(first_diag)):
				if position in first_diag[n]:
					mamka1 = copy(first_diag[n])
					break
			mamka2 = list()
			for n in range(len(second_diag)):
				if position in second_diag[n]:
					mamka2 = copy(second_diag[n])
					break
			if reposition not in mamka1 and reposition not in mamka2:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				sumka = list()
				my_mother = [mamka1,mamka2]
				for n in range(2):
					if reposition in my_mother[n]:
						sumka = copy(my_mother[n])
						break
				if abs(sumka.index(reposition)-sumka.index(position)) == 1:
					dictionary[reposition] = copy(dictionary[position])
					dictionary[reposition][1] += 1
					dictionary[position] = ["•",0]
					return dictionary
				else:
					if int(position[1]) > int(reposition[1]):
						kkk = sumka[sumka.index(position)+1:sumka.index(reposition)+1]
						if reposition in kkk:
							kkk.remove(reposition)
						indicator = 0
						for n in kkk:
							if n == "•":
								indicator += 1
							else:
								indicator -= 100
						if indicator >= 0:
							dictionary[reposition] = copy(dictionary[position])
							dictionary[reposition][1] += 1
							dictionary[position] = ["•",0]
							return dictionary
						else:
							return "Ваш ход некорректный.Сходите еще раз.1", None
					elif int(reposition[1]) > int(position[1]):
						kkk = sumka[sumka.index(reposition)+1:sumka.index(position)+1]
						if position in kkk:
							kkk.remove(position)
						indicator = 0
						for n in kkk:
							if n == "•":
								indicator += 1
							else:
								indicator -= 100
						if indicator >= 0:
							dictionary[reposition] = copy(dictionary[position])
							dictionary[reposition][1] += 1
							dictionary[position] = ["•",0]
							return dictionary
						else:
							return "Ваш ход некорректный.Сходите еще раз.", None





#аналогично для короля
def hod_king(dictionary,position,reposition):
	white_list = ["₽","R","N","B","Q","K"]
	black_list = ["p","r","n","b","q","k"]

	some = "ABCDEFGH"
	numers = ["1","2","3","4","5","6","7","8"]
	dop_znach = list()
	try:
		dop_znach.append(position[0]+numers[numers.index(position[1])+1])
	except IndexError:
		dop_znach.append(" ")
	try:
		dop_znach.append(position[0]+numers[numers.index(position[1])-1] if numers.index(position[1])-1 >= 0 else " ")
	except IndexError:
		dop_znach.append(" ")
	try:
		dop_znach.append(some[some.index(position[0])+1]+position[1])
	except IndexError:
		dop_znach.append(" ")
	try:
		dop_znach.append(some[some.index(position[0])-1]+position[1] if some.index(position[0])-1 >= 0 else " ")
	except IndexError:
		dop_znach.append(" ")
	try:
		dop_znach.append(some[some.index(position[0])+1]+numers[numers.index(position[1])+1])
	except IndexError:
		dop_znach.append(" ")
	try:
		dop_znach.append(some[some.index(position[0])+1]+numers[numers.index(position[1])-1] if numers.index(position[1])-1 >= 0 else " ")
	except IndexError:
		dop_znach.append(" ")
	try:
		dop_znach.append(some[some.index(position[0])-1]+numers[numers.index(position[1])+1] if some.index(position[0])-1 >= 0 else " ")
	except IndexError:
		dop_znach.append(" ")
	try:
		if some.index(position[0])-1 < 0 or numers.index(position[1])-1 < 0:
			dop_znach.append(" ")
		else:
			dop_znach.append(some[some.index(position[0])-1]+numers[numers.index(position[1])-1])
	except IndexError:
		dop_znach.append(" ")
	while " " in dop_znach:
		dop_znach.remove(" ")
	if dictionary[position][0] == "K":
		if dictionary[reposition][0] in white_list:
			return "Ваш ход некорректный.Сходите еще раз.", None
		else:
			if reposition not in dop_znach:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dictionary[reposition] = copy(dictionary[position])
				dictionary[reposition][1] += 1
				dictionary[position] = ["•",0]
				return dictionary
	elif dictionary[position][0] == "k":
		if dictionary[reposition][0] in black_list:
			return "Ваш ход некорректный.Сходите еще раз.", None
		else:
			if reposition not in dop_znach:
				return "Ваш ход некорректный.Сходите еще раз.", None
			else:
				dictionary[reposition] = copy(dictionary[position])
				dictionary[reposition][1] += 1
				dictionary[position] = ["•",0]
				return dictionary


















#Основная программы которая позволяет играть в шахматы двум игрокам

white_list = ["₽","R","N","B","Q","K"]
black_list = ["p","r","n","b","q","k"]
main_string = "ABCDEFGH"
main_numbers = "12345678"
necessary = list()
for n in main_string:
	for k in main_numbers:
		necessary.append(n+k)
ar = copy(main_dict)
while True:
	print_chess(ar)
	print("\nХод Белых:  (Вводите координаты фигур через пробел по примеру: a5 a6)\n")
	while True:
		the = input("::: ").split()
		if len(the) != 2:
			print("Некорректный ввод, попробуйе еще раз")
			continue
		elif the[0].upper() not in necessary or the[1].upper() not in necessary:
			print("Некорректный ввод, попробуйе еще раз")
			continue
		elif ar[the[0].upper()] in black_list:
			print("Сейчас ход белых!Попробуйте еще раз")
			continue
		else:
			if ar[the[0].upper()][0] == "₽":
				sss = hod_peshki(ar,the[0].upper(),the[1].upper())
				if type(sss) == dict:
					ar = copy(sss)
					break
				else:
					print(sss[0])
					continue
			elif ar[the[0].upper()][0] == "N":
				sss = hod_knight(ar,the[0].upper(),the[1].upper())
				if type(sss) == dict:
					ar = copy(sss)
					break
				else:
					print(sss[0])
					continue
			elif ar[the[0].upper()][0] == "B" or ar[the[0].upper()][0] == "Q":
				sss = hod_bishop(ar,the[0].upper(),the[1].upper())
				if type(sss) == dict:
					ar = copy(sss)
					break
				else:
					print(sss[0])
					continue
			elif ar[the[0].upper()][0] == "R" or ar[the[0].upper()][0] == "Q":
				sss = hod_rook(ar,the[0].upper(),the[1].upper())
				if type(sss) == dict:
					ar = copy(sss)
					break
				else:
					print(sss[0])
					continue
			elif ar[the[0].upper()][0] == "K":
				sss = hod_king(ar,the[0].upper(),the[1].upper())
				if type(sss) == dict:
					ar = copy(sss)
					break
				else:
					print(sss[0])
					continue
	print_chess(ar)
	print("\nХод Чёрных:  (Вводите координаты фигур через пробел по примеру: a5 a6)\n")
	while True:
		the = input("::: ").split()
		if len(the) != 2:
			print("Некорректный ввод, попробуйе еще раз")
			continue
		elif the[0].upper() not in necessary or the[1].upper() not in necessary:
			print("Некорректный ввод, попробуйе еще раз")
			continue
		elif ar[the[0].upper()] in white_list:
			print("Сейчас ход черных!Попробуйте еще раз")
			continue
		else:
			if ar[the[0].upper()][0] == "p":
				sss = hod_peshki(ar,the[0].upper(),the[1].upper())
				if type(sss) == dict:
					ar = copy(sss)
					break
				else:
					print(sss[0])
					continue
			elif ar[the[0].upper()][0] == "n":
				sss = hod_knight(ar,the[0].upper(),the[1].upper())
				if type(sss) == dict:
					ar = copy(sss)
					break
				else:
					print(sss[0])
					continue
			elif ar[the[0].upper()][0] == "b" or ar[the[0].upper()][0] == "q":
				sss = hod_bishop(ar,the[0].upper(),the[1].upper())
				if type(sss) == dict:
					ar = copy(sss)
					break
				else:
					print(sss[0])
					continue
			elif ar[the[0].upper()][0] == "r" or ar[the[0].upper()][0] == "q":
				sss = hod_rook(ar,the[0].upper(),the[1].upper())
				if type(sss) == dict:
					ar = copy(sss)
					break
				else:
					print(sss[0])
					continue
			elif ar[the[0].upper()][0] == "k":
				sss = hod_king(ar,the[0].upper(),the[1].upper())
				if type(sss) == dict:
					ar = copy(sss)
					break
				else:
					print(sss[0])
					continue







