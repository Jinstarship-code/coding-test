n = input()
a = n

n = list(n.split('0'))
n = list(filter(None, n))
a = list(a.split('1'))
a = list(filter(None, a))

print(len(n) if len(n) <= len(a) else len(a))
"""
 문자열로 나타내었을때, '1'의 집단의 수랑 '0'의 집단의 수를 비교해서 집단의 수가 적은 쪽이 뒤집는 횟수도 적다.
"""
