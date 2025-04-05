import sys

def find_name_and_price():
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
		return
	else:
		try:
			# comp - тикер, company_name - возвращаемый элемент, т.е. цикл for..in
			company = next((company_name for company_name, comp in COMPANIES.items() if comp.lower() == sys.argv[1].lower()), None)
			if (company != None):
				tag = sys.argv[1].upper()
				print(company, STOCKS[tag])
			else:
				print("Unknown ticker")
		except:
			print("Unknown ticker")

if __name__ == '__main__':
	find_name_and_price()