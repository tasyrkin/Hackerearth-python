import shlex

tokenizer = shlex.shlex(posix=True)
tokenizer.whitespace_split=True

T = int(tokenizer.get_token())

for i in range(T):
    N = int(tokenizer.get_token())
    for j in range(1, N+1):
        if j%3==0 and j%5==0:
            print('FizzBuzz')
        elif j%3==0:
            print('Fizz')
        elif j%5==0:
            print('Buzz')
        else:
            print j

