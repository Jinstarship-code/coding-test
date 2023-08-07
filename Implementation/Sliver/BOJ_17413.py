# BOJ_17413
import re

string = input()
arr = []

# 태그가 없는 문자열을 받으면 그냥 " "을 기준으로 나눠서 각자 뒤집으면 되기에
if '<' not in string:
  arr = list(string.split(" "))
else:  # 태그가 있는 경우 arr배열에 태그와 각 문자를 나눠서 arr에 append해주었다.
  startIndex = -1
  lastIndex = -1
  for i in range(len(string)):
    if string[i] == '<':
      startIndex = i
    elif string[i] == '>':
      lastIndex = i

    if lastIndex == i:
      arr.append(string[startIndex:lastIndex + 1])
    elif i != 0 and startIndex == i:
      arr += list(string[lastIndex + 1:startIndex].split(' '))
    elif string[i] != '>' and i == len(string) - 1:
      arr += list(string[lastIndex + 1:i + 1].split(' '))

# 답 출력 과정(end를 이용해서 개행되지 않게 조절하였다.)
for i in range(len(arr) - 1):
  if '<' in arr[i]:
    print(arr[i], end='')
  elif '<' not in arr[i] and '<' in arr[i + 1]:
    print(arr[i][-1::-1], end='')
  elif '<' not in arr[i] and '<' not in arr[i + 1]:
    print(arr[i][-1::-1], end=' ')

# 마지막으로 남은 문자를 출력.
if '<' in arr[-1]:
  print(arr[-1])
else:
  print(arr[-1][-1::-1])
"""
해설을 안보고 하려니 너무 긴 코드가 나와버렸다.
밑과 같이 간결한 코드가 나올 수 있으니 더 연습하자.

import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":       # 열린 괄호를 만나면
        i += 1 
        while word[i] != ">":      # 닫힌 괄호를 만날 때 까지
            i += 1 
        i += 1               # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i+=1
        tmp = word[start:i] # 숫자,알파벳 범위에 있는 것들을
        tmp.reverse()       # 뒤집는다
        word[start:i] = tmp
    else:                   # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i+=1                # 그냥 증가시킨다

print("".join(word))



"""
