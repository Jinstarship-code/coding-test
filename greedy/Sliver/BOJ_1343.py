#BOJ_1343 폴리오미노

string = input()

# .과 x로 나누자.
xstring = list(string.split('.'))
dotstring = list(string.split('X'))

xstring = list(filter(None, xstring))
dotstring = list(filter(None, dotstring))

# 문자열 계산하기
for i in range(len(xstring)):
  if len(xstring[i]) % 2 == 1:
    string = -1
    break
  if len(xstring[i]) % 4 == 0:
    xstring[i] = xstring[i].replace('X', 'A')
  elif (len(xstring[i]) - 2) % 4 == 0:
    xstring[i] = 'A' * (len(xstring[i]) - 2) + 'B' * (len(xstring[i]) % 4)
  elif len(xstring[i]) % 2 == 0:
    xstring[i] = xstring[i].replace('X', 'B')

# 문자열합쳐주기
answer = ''
if string != -1:
  if string[0] == 'X':
    if len(xstring) == len(dotstring):
      for i in range(len(xstring)):
        answer += xstring[i]
        answer += dotstring[i]
    else:
      for i in range(len(dotstring)):
        answer += xstring[i]
        answer += dotstring[i]
      answer += xstring[-1]
  else:
    if len(xstring) == len(dotstring):
      for i in range(len(xstring)):
        answer += dotstring[i]
        answer += xstring[i]
    else:
      for i in range(len(xstring)):
        answer += dotstring[i]
        answer += xstring[i]
      answer += dotstring[-1]
else:
  answer = -1

print(answer)
"""
뭔가 쉽게 할 수 있는 방법이 있을거 같은데..


나의 풀이 방법
 - 입력받은 문자열을 X와 .을 각각 담는 리스트로 split한다.
 - 폴리노미오가 'AAAA' (4개) 'BB'(2개) 이므로 4로 나눠지는지 2로나눠지는지에 따라 두개중 하나를 넣으면 된다.
 - 다만, 2로 나눠지는 경우엔 이 문자열의 길이가 4보다 길 경우엔 'AAAA'를 넣어줘야 하기 때문에, (문자열 길이-2)%4를 해서  
    xstring[i] = 'A' * (len(xstring[i]) - 2) + 'B' * (len(xstring[i]) % 4) 와 같이 문자열을 대체해준다.
- 마지막으로, 각 리스트에 담긴 원소들을 합쳐준다.
  
"""
