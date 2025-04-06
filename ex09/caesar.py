import sys

def shift_letter(letter, shift):
	letter_num = ord(letter)
	if (letter_num <= 127 and letter_num >= 32):
		if (letter.isalpha()):
			if (letter.isupper()):
				base = ord('A')
				shifted = (letter_num - base + shift) % 26 + base
				return chr(shifted)

			base = ord('a')
			shifted = (letter_num - base + shift) % 26 + base
			return chr(shifted)
		else:
			return letter
	else:
		return None

def caesar():
	if (len(sys.argv) != 4):
		return

	if (sys.argv[1] == "decode"):
		str = ""
		for letter in sys.argv[2]:
			str += shift_letter(letter, -(int(sys.argv[3])))
		print(str)
	elif (sys.argv[1] == "encode"):
		str = ""
		for letter in sys.argv[2]:
			str += shift_letter(letter, int(sys.argv[3]))
		print(str)
	else:
		return

if __name__ == '__main__':
	caesar()
