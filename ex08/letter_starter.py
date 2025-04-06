import sys

def letter_starter():
	if (len(sys.argv) == 2):
		tsv_file_data = open("employees.tsv", "r")
		data_list = tsv_file_data.read().splitlines()
		for data_str in data_list:
			splitted_data_str = data_str.split('\t')
			if (splitted_data_str[2] == sys.argv[1]):
				print(f"""Dear {splitted_data_str[0]}, welcome to our team. We are sure that it will be a pleasure to work with
you. That’s a precondition for the professionals that our company hires.""")
				return

if __name__ == '__main__':
	letter_starter()
