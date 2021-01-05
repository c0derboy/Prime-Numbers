prime_numbers = [2, ]
stop = 100

for n in range(2, stop):
	for i in prime_numbers:
		if n%i != 0:
			prime_numbers.append(n)
			break
		break
print(prime_numbers)
print(f'There are {len(prime_numbers)} prime numbers until {stop}')
print('This is V1.1')