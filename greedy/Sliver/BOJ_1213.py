string = input()
string_cnt = [0] * 26
for ch in string:
  string_cnt[ord(ch) - 65] += 1

odd = 0
center = ''
alpha = ''

for i in range(26):
  if string_cnt[i] % 2 == 1:
    odd += 1
    center += chr(i + 65)
  alpha += chr(i + 65) * (string_cnt[i] // 2)

if odd > 1:
  print("I'm Sorry Hansoo")
else:
  print(alpha + center + alpha[::-1])
"""
 알파벳을 담는 배열을 만들어서
 입력받은 스트링을 -'A'를 한 값(인덱스)에 +1을 해준다

 그 후, for문을 돌면서 odd가 2이상인지를 확인하고 odd가 1인 곳에 center를 체크한다.
 참고로, palindrome은 odd가 2이상이면 성립되지 않는다. 따라서 odd가 잇으면 1개만 나올 것이다.
 그후 앞의 문자열 + center + 반대로 하면 답이 나올 것이다.

"""
