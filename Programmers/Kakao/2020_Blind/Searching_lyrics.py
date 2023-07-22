from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_idx = bisect_right(a, right_value)
    left_idx = bisect_left(a, left_value)
    return right_idx-left_idx

arr = [[] for _ in range(10001)]
reversed_arr = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []

    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])

    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_by_range(arr[len(q)],q.replace('?','a'),q.replace('?','z'))
        else:
            res = count_by_range(reversed_arr[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
        answer.append(res)