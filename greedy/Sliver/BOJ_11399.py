n = int(input())

arr = []
arr += list(map(int,input().split()))
arr.sort()
answer = [arr[0]]
for i in range(1,len(arr)):
  answer.append(sum(arr[:i])+arr[i])

print(sum(answer))

# 1+2+3+3+4 => 1+3+6+9+13
"""
Ǯ�̹�:
    1. �� ����� �ɸ��� �ð��� ���ϰ�
    2. sum(answer)

"""
