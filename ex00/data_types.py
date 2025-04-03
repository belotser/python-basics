def data_types():
	typesList = [type(12).__name__, type("строка").__name__,
				  type(3.4).__name__, type(False).__name__,
				  type([1, 2]).__name__, type({"name": "Alice", 1: 4}).__name__,
				  type((1, 2, 3, 5, 7)).__name__, type({1, 2, 1, 1, 1, 2}).__name__]
	print("[" + ", ".join(typesList) + "]")

if __name__ == '__main__':
	data_types()