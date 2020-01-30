num = 2
primes = set()
var = 1
for i in range(10000):
    for x in primes:
        
            if float( num / x) == int(num / x):
                num = num + 1
                var = 0
                break
            else:
                var = 1

    if var == 1:
        primes.add(num)
        print(num)
        num = num + 1

