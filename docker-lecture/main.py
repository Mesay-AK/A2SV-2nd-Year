def fizbuzz(n):
    # FizzBuzz function that prints numbers from 1 to n
    # If the number is divisible by 3, print 'Fizz' 
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    user = input('Enter a number: ')
    fizbuzz(int(user))
    