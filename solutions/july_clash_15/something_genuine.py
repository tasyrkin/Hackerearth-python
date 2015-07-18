__author__ = 'tim'

import shlex

MOD = 1000000007

tokenizer = shlex.shlex(posix=True)
tokenizer.whitespace_split=True

N = int(tokenizer.get_token())

sq = [i*i for i in range(0, N+1)]

arr = [0 for i in range(N)]
sets = [[None for _ in range(N+1)] for _ in range(N)]
result = 0
for idx in range(N):
    arr[idx] = int(tokenizer.get_token())
    sets[idx][1] = set()
    sets[idx][1].add(arr[idx])
    result += 1

for idx in range(N):
    for length in range(2, N-idx+1):
        sets[idx][length] = sets[idx][length-1]
        sets[idx][length].add(arr[idx+length-1])
        size = len(sets[idx][length])
        result = (result + sq[size]) % MOD

print result