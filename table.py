""" Table Gen"""

def table_gen(x,y):
	for i in range(1,y+1):
		print('{} x {} = {}'.format(x, i, x*i))

if __name__ == '__main__':	
	x = input('Enter a number: ')
	y = input('Enter a number of times you want multiplicate: ')
	table_gen(int(x), int(y))

