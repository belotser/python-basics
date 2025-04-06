def names_extractor():
	file_mails = open("mails.txt", "r")
	mails_list = file_mails.read().split('\n')
	pairs_list = []
	for mail in mails_list:
		pair = mail.split('@')[0].split('.')
		pair[0] = pair[0].capitalize()
		pair[1] = pair[1].capitalize()
		pair.append(mail)
		pairs_list.append(pair)
	file_mails.close()

	tsv_file_data = open("employees.tsv", "w")
	header = "Name\tSurname\tE-mail\n"
	content = header
	for pair in pairs_list:
		content += pair[0] + '\t'
		content += pair[1] + '\t'
		content += pair[2] + '\n'
	tsv_file_data.write(content)
	tsv_file_data.close()


if __name__ == '__main__':
	names_extractor()
