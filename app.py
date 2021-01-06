import datetime

stop = input('Set the number limit. Stop app.py with Ctrl + C')
start_time = datetime.datetime.now()
prime_numbers = []

def generator():
	D = {}
	q = 2
	while True:
		if q == stop:
			break
		if q not in D:
			yield q
			D[q*q] = [q]
		else:
			for i in D[q]:
				D.setdefault(q + i, []).append(i)
			del D[q]	
		q += 1
for b in generator():
	prime_numbers.append(b)

print(prime_numbers)
print(f'There are {len(prime_numbers)} prime numbers until {stop}')

end_time = datetime.datetime.now()
duartion = (end_time - start_time).total_seconds() * 1000
print(f'{duartion} mili seconds')