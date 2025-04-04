def processReplacing(str):
	result = []
	in_quotes = False
	for char in str:
		if char == '"':
			in_quotes = not in_quotes
			result.append(char)
		elif char == ',' and not in_quotes:
			result.append("\t")
		else:
			result.append(char)
	return ''.join(result) + '\n'

def replaceCommaToTab():
	with open("ds.csv", "r", encoding="utf-8") as file:
		content = file.readlines()

	with open("ds.csv", "w", encoding="utf-8") as file:
		for line in content:
			file.write(processReplacing(line.strip()))


if __name__ == '__main__':
	replaceCommaToTab()