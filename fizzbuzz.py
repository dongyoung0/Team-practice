#fizzbuzz

#input number
n = int(input('input number: '))

#print fizzbuzz
for i in range(1,n+1):
    if i%3==0 or i%5==0:
        print(f'{i} ' + 'fizz'*(i%3==0) + 'buzz'*(i%5==0))
    else:
        print(i)
