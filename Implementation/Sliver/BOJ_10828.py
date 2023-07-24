import sys
n = int(sys.stdin.readline())

arr = []
answer = []

for _ in range(n):
  string = input()
  if 'push' in string:
    string = list(string.split())
    arr.append(int(string[1]))
  elif string == 'pop':
    if len(arr)==0:
      answer.append(-1)
    else:
      answer.append(arr.pop())
  elif string == 'size':
    answer.append(len(arr))
  elif string == 'empty':
    if len(arr) == 0:
      answer.append(1)
    else:
      answer.append(0)
  elif string == 'top':
    if len(arr)==0:
      answer.append(-1)
    else:
      answer.append(arr[-1])


for i in range(len(answer)):
  print(answer[i])


"""
    python의 기본문법들을 잘 숙지하고 있었다면, 쉽게 풀수 있는 문제이다.
    다만, 처음에 input()으로 입력을 받았는데 시간초과되어서
    sys.stdin.readline()으로 변경해주는 정답처리가 되었다.      
      
"""
    