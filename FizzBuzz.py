n = 15

for x in range(1, n+1):
    tres = False
    cinco = False
    if x % 3 == 0:
        tres = True
    if x % 5 == 0:
        cinco = True
    if tres and cinco:
        print('FizzBuzz')
    if tres and not cinco:
        print('Fizz')
    if cinco and not tres:
        print('Buzz')
    if not cinco and not tres:
        print(x)
