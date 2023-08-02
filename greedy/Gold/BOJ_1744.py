n = int(input())

arr = []
minus_arr = []
for _ in range(n):
  arr.append(int(input()))
divide_index = -1
cnt = 0


# 배열을 받고나서 묶음(a * b) 한 리스트를 리턴하는 함수
def Calc(arr):
  tmp = []
  if len(arr) % 2 == 0:
    for i in range(0, len(arr), 2):
      tmp.append(arr[i] * arr[i + 1])
  else:
    for i in range(0, len(arr) - 1, 2):
      tmp.append(arr[i] * arr[i + 1])
    tmp.append(arr[-1])
  return tmp


# 일단 정렬해서 나눌 기준이 되는 인덱스를 확인하는 과정
arr.sort()
for i in range(len(arr)):
  # 만약 [1,1]인 리스트가 문제로 주어지면 잘못된 값을 출력한다. 그래서 arr[0]은 막아주었다.
  if arr[i] >= 0 and arr[0] != 1:
    divide_index = i

  if divide_index != -1:
    break

# 1의 개수를 확인
cnt = arr.count(1)

# 리스트 뒤에서부터 1을 확인해서 나눌 인덱스를 확인하는 과정
one_index = -1
for i in range(len(arr) - 1, -1, -1):
  if arr[i] == 1:
    one_index = i
    break

## 리스트를 나누는 과정
# 문제에 음수 값도 있고 1도 있는 경우 => 음수의 리스트 + 2부터 시작하는 리스트
if divide_index != -1 and one_index != -1:
  minus_arr = arr[:divide_index + 1]
  arr = arr[one_index + 1:]
# 1은 없고 음수값이 있는경우
elif divide_index != -1:
  minus_arr = arr[:divide_index]
  arr = arr[divide_index:]
# 음수값은 없고 1은 있는 경우
elif one_index != -1:
  arr = arr[one_index + 1:]

# Calc()를 위한 arr 내림차순 정렬
arr.sort(reverse=True)

minus_arr = Calc(minus_arr)
arr = Calc(arr)

# answer
print(sum(minus_arr) + sum(arr) + cnt)
"""
반례가 너무 많다.. ㅠㅠ
 - 힘들게 풀었지만,
 - 아이디어는 수의 함의 최대인데, 두 수를 묶을수 있다고 했으니. 음수는 음수끼리 양수는 양수끼리 묶어서. 음수 같은 경우 오름차순으로 정렬해서 두 수씩 곱셈하게 되면 양수가 되서 최대의 값이되고, 양수의 경우 내림차순으로 정렬해서 곱하게되면 최댓값을 도출할 수 있게 된다. 기본적인것은 이 아이디어로 풀었다.
 - 다만, 0,1 이 걸림돌이 되는데, 1*1 보다 1+1의 값이 크므로, 나 같은 경우 1을 count해서 나중에 답을 도출할때 +를 해준 결과를 나타나게 해주었다. 0의 경우, 음수에 1개만 넣어주고 나머지는 양수인 리스트에 넣어주었다.
 그 이유는, 0을 음수에 여러개 넣게되면 (음수)*(음수) = (양수)의 값을 방해하기 때문에, 만약 음수가 하나라면 0을 하나만 넣어줘서 곱한값이 0이 최대가 되게 해주었다.


"""
