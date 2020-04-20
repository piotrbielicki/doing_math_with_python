""" Unit converter """

def print_menu():
	print('1. kilograms to pounds')
	print('2. pounds to kilograms')
	print('3. fahrenheits to celsius')
	print('4. celsius to fahrenheits')

def kg_lb():
	kg = float(input('Enter mass in kilograms: '))
	lb = (kg * 2.20462262)
	
	print('Mass in pounds: {}'.format(lb))

def lb_kg():
	lb = float(input('Enter mass in pounds: '))
	kg = (lb *0.45359237)
	
	print('Mass in kilograms: {}'.format(kg))


def f_c():
	f = float(input('Enter temperature in fahrenheits: '))
	c = ((f-32)/1.8)
	
	print('Temperature in celsius: {}'.format(c))

def c_f():
	c = float(input('Enter temperature in celsius: '))
	f = ((c*1.8) + 32)
	
	print('Temperature in fahrenheits: {}'.format(f))

print_menu()
a = int(input('Choose converter: '))


if a == 1:
	kg_lb()
elif a == 2:
	lb_kg()
elif a == 3:
	f_c()
elif a == 4:
	c_f()
