import sys

n = list(sys.stdin.readline().rstrip())

n.sort(reverse=True)
answer = ''

# 각 자리수의 합 
check_3 = 0
for i in n:
  check_3 += int(i)

if '0' not in n or check_3 % 3 != 0:
  print(-1)
else:
  answer = ''.join(n)
  print(answer)

"""
    수학 상식: 3의 배수는 각자리수의 합이 3으로 나눠지면 3의 배수이다.
    
    추가로 30의 배수이니까, 문자열에 '0'이 존재하면 10씩 나눌수 있으므로
    3의배수를 확인하면 된다.

"""