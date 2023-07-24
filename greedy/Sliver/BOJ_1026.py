n = int(input())
arrA = list(map(int,input().split()))
arrB = list(map(int,input().split()))
arrA.sort()

reverseB = sorted(arrB,reverse=True)
answer = 0
for i in range(len(arrA)):
  answer += arrA[i] * reverseB[i]
print(answer)

"""
len N   arr A and B
S = A[0]*B[0]+...+A[N-1]*B[n-1]
A만 재배열해서 S의 최솟값만들기.


문제의 조건에선 B를 재벼열 하지 말라고했는데,,

생각해보니 answer의 최솟값을 구하는 문제인데, B도 내림차순으로 재배열해서
구하면 답은 나오게 되어 있는데,, 굳이 안할 이유가.
"""