__author__ = 'tim'

import shlex

def shrink_array(S, arr):
    prev = None
    cnt = 1
    idx = 0
    for ch in S:
        if prev is None:
            prev = ch
        elif prev != ch:
            arr.append(cnt if prev == 'K' else -cnt)
            cnt = 1
            prev = ch
        else:
            cnt += 1
        idx += 1
    arr.append(cnt if prev == 'K' else -cnt)


tokenizer = shlex.shlex(posix=True)
tokenizer.whitespace_split=True

T = int(tokenizer.get_token())

while T > 0:
    T -= 1
    S = tokenizer.get_token()
    arr = []
    shrink_array(S, arr)
    ans = -1<<63
    sum = 0
    min_sum = 0
    ans_l = 0
    ans_r = 0
    min_pos = -1
    for idx in range(len(arr)):
        sum += arr[idx]
        cur = sum - min_sum
        if cur > ans:
            ans = cur
            ans_l = min_pos + 1
            ans_r = idx
        if sum < min_sum:
            min_sum = sum
            min_pos = idx

    if ans < 0:
        print -ans
    else:
        for idx in range(len(arr)):
            if arr[idx] < 0:
                ans += -arr[idx]
        print ans


