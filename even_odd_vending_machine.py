"""
Vending machine
"""

def vending_machine(n):

	a = [i for i in range(n, 21, 2)]

	if n % 2 == 0:
		print('even ' + ', '.join(map(str, a)))
	else:
		print('odd ' + ', '.join(map(str, a)))


if __name__ == '__main__':
	n = input('Enter number: ')
	n = float(n)
	
	if n > 0 and n.is_integer():
		vending_machine(int(n))
	else:
		print('Please enter a positive integer')

