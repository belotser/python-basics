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
	with open("ds.csv", "r", encoding="utf-8") as file_input:
		content = file_input.readlines()

	with open("ds.tsv", "w", encoding="utf-8") as file_output:
		for line in content:
			file_output.write(processReplacing(line.strip()))


if __name__ == '__main__':
	replaceCommaToTab()