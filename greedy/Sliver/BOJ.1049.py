n,m = map(int,input().split())


arr =[]
for _ in range(m):
  arr +=[list(map(int,input().split()))]

arr1 = sorted(arr,key=lambda x:x[0])
arr2 = sorted(arr,key=lambda x:x[1])
cmp1 = arr1[0]
cmp2 = arr2[0]

answer =[]
while True:
  a,b=cmp1
  c,d=cmp2
  if n > 6:
    b *= 6
    d *= 6
    answer.append(min(a,b,c,d))
    n -= 6
  else:
    b *=n
    d *=n
    answer.append(min(a,b,c,d))
    break
    
print(sum(answer))


"""
나의 풀이의 경우
    묶음가격으로 정렬을 하나하고, 낱개가격으로 정렬을 또 하나해서
    각 배열의 0번 인덱스만 비교해주면 최소값이 도출되므로
    cmp1,cmp2라는 배열을 두었다.
    
    이후, n -= 6 을하면서 answer배열에 계속 min값을 추가해주었다.
    
"""