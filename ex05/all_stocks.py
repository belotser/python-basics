import sys

def allStocks():
	COMPANIES = {
		'Apple': 'AAPL',
		'Microsoft': 'MSFT',
		'Netflix': 'NFLX',
		'Tesla': 'TSLA',
		'Nokia': 'NOK'
  	}

	STOCKS = {
		'AAPL': 287.73,
		'MSFT': 173.79,
		'NFLX': 416.90,
		'TSLA': 724.88,
		'NOK': 3.37
	}

	if (len(sys.argv) != 2):
		sys.exit()

	input_str = sys.argv[1]
	input_args = input_str.split(',')
	clear_input_args = []
	for i in range(0, len(input_args)):
		clear_input_args.append(input_args[i].strip())
		if (clear_input_args[i] == "" or clear_input_args[i].isspace()):
			sys.exit()

	for arg in clear_input_args:
		company = next((company_name for company_name, comp in COMPANIES.items() if comp.lower() == arg.lower()), None)
		if (company != None):
			tag = arg.upper()
			print(tag, "is a ticker symbol for", company)
		else:
			try:
				company = arg.lower()
				print(company, "stock price is", STOCKS[COMPANIES[company.capitalize()]])
			except:
				print(arg, "is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
	allStocks()