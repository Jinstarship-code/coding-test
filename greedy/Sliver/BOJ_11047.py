n,k = map(int,input().split())

values = []
for i in range(n):
  values.append(int(input()))

values = sorted(values, reverse = True)

cnt = 0
for value in values:
  if value > k:
    continue
  
  cnt += k//value
  k = k%value

  if k < 5:
    cnt += k
    break

print(cnt)

"""
Ǯ�� ����
    1. ��ġ�� ������������ ��迭�ϰ�
    2. ��ġ�� for���� ���鼭 ������ ���ϰ�


"""