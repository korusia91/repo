def dodawanie(a,b):
	return a + b
try:
	a = int(input('podaj a: '))
	b = int(input('podaj b: '))
	print(dodawanie(a,b))
except ValueError as ve:
	print('Bład danych')
input()