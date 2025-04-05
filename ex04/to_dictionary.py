def fromTuplesToDict():
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

	dataDict = {}

	for dataStr in list_of_tuples:
		if dataStr[1] not in dataDict:
			dataDict[dataStr[1]] = []
		dataDict[dataStr[1]].append(dataStr[0])

	for key, value in dataDict.items():
		for state in value:
			print(f"{key} : {state}")

if __name__ == '__main__':
	fromTuplesToDict()