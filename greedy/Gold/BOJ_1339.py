
# 풀이 아이디어는 떠올렸는데, 10을 거듭제곱을해서 
# 알파벳마다 먼저 가치를 부여해주는것을 생각치 못했다.
# 밑은 거의 남의 코드.
n = int(input())
alphaDict = {}
arr = []
for _ in range(n):
  arr.append(input())

for string in arr:
  for i in range(len(string)):
    if string[i] not in alphaDict:
      alphaDict[string[i]] = 10 **(len(string)-1-i)
    else:
      alphaDict[string[i]] += 10 **(len(string)-1-i)

alphaDict = sorted(alphaDict.items(),key=lambda x: x[1], reverse=True)

alpha_num = {}
num = 9
for alpha in alphaDict:
  alpha_num[alpha[0]] = num
  num -= 1

answer = 0
for string in arr:
  num = ""
  for ch in string:
    num += str(alpha_num[ch])
  answer += int(num)

print(answer)


"""
 len가 같을때,
 첫째 자리 알파벳이 같은 문자열중에 누가더 앞에있느냐가 중요
 
ex) ABB, BBA 일경우 B가 9이면 최댓값이된다.
"""
