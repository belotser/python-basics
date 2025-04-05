import sys

def find_price():
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
			company = sys.argv[1].lower()
			print(STOCKS[COMPANIES[company.capitalize()]])
		except:
			print("Unknown company")

if __name__ == '__main__':
	find_price()