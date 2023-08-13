from itertools import combinations

def solution(nums):
    answer = 0
    primes = []
    tmp = [False,False] + [True]*3000
    
    cmp = list(combinations(nums,3))
    for i in range(2,max(nums)*3+1):
        if tmp[i]:
            primes.append(i)
            for j in range(2*i,max(nums)*3+1,i):
                tmp[j] = False
    
    for i in range(len(cmp)):
        if sum(cmp[i]) in primes:
            answer +=1
        
    return answer


"""
# 에레토스테네스체의 기본 파이썬 코드
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)

풀이 방법
    1. 에라토스테네스체를 통해 prime 배열을 생성한다.
    2. itertools의 combinations을 가져와 3개를 뽑는 경우의 수의 배열을 만든다.

"""