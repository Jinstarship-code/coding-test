# 문자열을 입력받으면 list로 나누기 쉽다.
s = list(input())

# 9->6으로 전환해주는 과정(근데 이렇게 하지말고, replace()를 쓰자)
for i in range(len(s)):
  if s[i] == '9':
    s[i] = '6'
for i in range(len(s)):
  s[i] = int(s[i])

dp = [1 for i in range(9)]
dp[6] = 2
cnt = 1

# 본격적인 count작업
for i in range(len(s)):
  if dp[s[i]] > 0:
    dp[s[i]] -= 1
  else:
    cnt += 1
    for j in range(9):
      if j != 6:
        dp[j] += 1
      else:
        dp[j] += 2

    dp[s[i]] -= 1

print(cnt)
"""
  기본적인 아이디어
  1. dp[]  를 0~8까지를 생성해주고 한세트를 샀다고 가정하고 각 dp[i]에 +1을 넣어주고 count를 한다.(6에는 +2)
  2. 9같은 경우 6과 공유를 할수 잇으므로 문자열에 9 를 6으로 교체해줬다.(다풀고생각해보니 for문 돌필요 없고 replace()를 쓰도록하자.)
  3. for문 돌면서 dp[s[i]] 에 해당되는 값을 -1씩해주고 dp[s[i]] ==0이라면 초를 하나사야하므로 dp를 다시 +1,+2해준다.

"""
