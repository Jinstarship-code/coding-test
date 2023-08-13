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
# �����佺�׳׽�ü�� �⺻ ���̽� �ڵ�
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)

Ǯ�� ���
    1. �����佺�׳׽�ü�� ���� prime �迭�� �����Ѵ�.
    2. itertools�� combinations�� ������ 3���� �̴� ����� ���� �迭�� �����.

"""