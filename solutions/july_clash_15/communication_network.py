__author__ = 'tim'

import shlex

INF = 1<<63

tokenizer = shlex.shlex(posix=True)
tokenizer.whitespace_split=True

N = int(tokenizer.get_token())
K = int(tokenizer.get_token())
K2 = K*K
arr = [0 for _ in range(N)]
for idx in range(N):
    arr[idx] = long(tokenizer.get_token())*K2
sqs = [i*i for i in range(N)]

result = [[INF for _ in range(K+1)] for _ in range(N)]
result[0][1] = arr[0]

for i in range(1, N):
    for k in range(2, K+1):
        if k > i+1:
            break
        curr_min = INF
        for j in range(i):
            if result[j][k-1] == INF:
                curr = INF
            else:
                curr = result[j][k-1]+arr[i]+sqs[(i-j)]
            if curr_min > curr:
                curr_min = curr
        result[i][k] = curr_min

res = INF
for k in range(2, K+1):
    if res > result[N-1][k]:
        res = result[N-1][k]
print res