def dict_sort():
	list_of_tuples = [
		('Russia', '25'),
		('France', '132'),
		('Germany', '132'),
		('Spain', '178'),
		('Italy', '162'),
		('Portugal', '17'),
		('Finland', '3'),
		('Hungary', '2'),
		('The Netherlands', '28'),
		('The USA', '610'),
		('The United Kingdom', '95'),
		('China', '83'),
		('Iran', '76'),
		('Turkey', '65'),
		('Belgium', '34'),
		('Canada', '28'),
		('Switzerland', '26'),
		('Brazil', '25'),
		('Austria', '14'),
		('Israel', '12')
  	]

	sorted_list_of_tuples = sorted(list_of_tuples, key=lambda item: item[0])
	sorted_list_of_tuples = sorted(sorted_list_of_tuples, key=lambda item: int(item[1]))

	for pair in sorted_list_of_tuples:
		print(pair[0], pair[1])

if __name__ == '__main__':
	dict_sort()