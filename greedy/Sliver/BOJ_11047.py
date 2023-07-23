n,k = map(int,input().split())

values = []
for i in range(n):
  values.append(int(input()))

values = sorted(values, reverse = True)

cnt = 0
for value in values:
  if value > k:
    continue
  
  cnt += k//value
  k = k%value

  if k < 5:
    cnt += k
    break

print(cnt)

"""
풀이 과정
    1. 가치를 내림차순으로 재배열하고
    2. 가치를 for문을 돌면서 나누고 더하고


"""