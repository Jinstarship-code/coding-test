#BOj_2960

n, k = map(int, input().split())

arr = []

# n까지 있는 arr 만들기
for i in range(2, n + 1):
  arr.append(i)

answer = 0

# 하나하나씩 뺴면서 답을 구해간다.
while k!=0:
  i = 0
  tmp = arr.pop(i)
  k -= 1
  
  if k == 0:
    print(tmp)
    break

  for i in range(n//tmp+1):
    if tmp * i in arr:
      arr.remove(tmp*i)
      k -= 1
      if k == 0:
        print(tmp*i)
        break
  
"""


"""