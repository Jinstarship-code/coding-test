n,k = map(int,input().split())

arr = [i for i in range(1,n+1)]
exitArr = []
i = k-1
while True:
   if len(arr) == 1:
       exitArr.append(arr[0])
       break
    
   if i == len(arr)-1:
    exitArr.append(arr.pop(i))
    i = 0
   else:
       exitArr.append(arr.pop(i))
   i += k-1

   while i>= len(arr):
       i -= len(arr)
   
# 출력 
print('<',end='')
for i in exitArr:
    if i != exitArr[-1]:
        print(str(i)+', ',end='')
    else:
        print(str(i)+'>')

"""
    원을 계속 돌아야해서 list의 i의 값이 다시 되돌아가게 설정해주어야한다.
    (주의)
        되돌아가는 설정을 한번만 해주게 되면, k의 값이 큰 경우 i의 값을 계산했는데됴,
        여전히 len(arr)의 범위를 넘어갈 수 있다.
        그래서 나 같은 경우 while을 통해서 계속 빼는 작업을 해주었다.
        - 지금 생각해보면 %을 이용해서 하는 방법도 있을수 있겠다.




"""