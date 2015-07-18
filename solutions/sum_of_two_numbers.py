import shlex

tokenizer = shlex.shlex(posix=True)
tokenizer.whitespace_split=True

T = int(tokenizer.get_token())

for i in range(T):
    a = int(tokenizer.get_token())
    b = int(tokenizer.get_token())
    print a+b
