n = int(input())

arr = []
for i in range(n):
  arr.append(int(input()))

arr.sort(reverse=True)

lift_up = [0] * n
lift_up[0] = arr[0]

for i in range(1, n):
  lift_up[i] = (arr[i] * (i + 1))

print(max(lift_up))

"""
문제 :
 n 개의 줄
 k 개의 줄을사용해 w인 물체를 들어올리면
 각 로프는 w/k의 하중을 받는다.
 w/k의 최댓값은?

===============================
줄의 중량을 내림차순으로 정렬한다. 

최대 버틸수 있는 중량을 찾는 것이니, 
k개줄을 사용했을때 최소중량을 가진 줄이 최대중량을 넘기면 안된다.
따라서,  최소중량 * k 을 하면 k개 줄을 사용했을때의 최대중량이 도출된다.

# (이해 안되시는 분을 위해)
   (최소중량 * k) / k   (이 식이 w/k이다.) 이 계산 값을 넘어가면 최소중량을 가진 줄이 버티질 못한다.    
"""
