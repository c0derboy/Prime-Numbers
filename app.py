import datetime

stop = input('Specify the range of numbers. (Use Ctrl + C if Lagged)')
start_time = datetime.datetime.now()
prime_numbers = [2]

for n in range(3, int(stop)):
	is_prime = True
	for i in prime_numbers:
		if n%i == 0:
			is_prime = False
			break
	if is_prime == False:
		continue
	prime_numbers.append(n)
			

print(prime_numbers)
print(f'There are {len(prime_numbers)} prime numbers until {stop}')
print('This is V1.12')

end_time = datetime.datetime.now()
duartion = (end_time - start_time).total_seconds() * 1000
print(f'{duartion} mili seconds')