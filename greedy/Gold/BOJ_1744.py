n = int(input())

arr = []
minus_arr = []
for _ in range(n):
  arr.append(int(input()))
divide_index = -1
cnt = 0


# �迭�� �ް��� ����(a * b) �� ����Ʈ�� �����ϴ� �Լ�
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


# �ϴ� �����ؼ� ���� ������ �Ǵ� �ε����� Ȯ���ϴ� ����
arr.sort()
for i in range(len(arr)):
  # ���� [1,1]�� ����Ʈ�� ������ �־����� �߸��� ���� ����Ѵ�. �׷��� arr[0]�� �����־���.
  if arr[i] >= 0 and arr[0] != 1:
    divide_index = i

  if divide_index != -1:
    break

# 1�� ������ Ȯ��
cnt = arr.count(1)

# ����Ʈ �ڿ������� 1�� Ȯ���ؼ� ���� �ε����� Ȯ���ϴ� ����
one_index = -1
for i in range(len(arr) - 1, -1, -1):
  if arr[i] == 1:
    one_index = i
    break

## ����Ʈ�� ������ ����
# ������ ���� ���� �ְ� 1�� �ִ� ��� => ������ ����Ʈ + 2���� �����ϴ� ����Ʈ
if divide_index != -1 and one_index != -1:
  minus_arr = arr[:divide_index + 1]
  arr = arr[one_index + 1:]
# 1�� ���� �������� �ִ°��
elif divide_index != -1:
  minus_arr = arr[:divide_index]
  arr = arr[divide_index:]
# �������� ���� 1�� �ִ� ���
elif one_index != -1:
  arr = arr[one_index + 1:]

# Calc()�� ���� arr �������� ����
arr.sort(reverse=True)

minus_arr = Calc(minus_arr)
arr = Calc(arr)

# answer
print(sum(minus_arr) + sum(arr) + cnt)
"""
�ݷʰ� �ʹ� ����.. �Ф�
 - ����� Ǯ������,
 - ���̵��� ���� ���� �ִ��ε�, �� ���� ������ �ִٰ� ������. ������ �������� ����� ������� ���. ���� ���� ��� ������������ �����ؼ� �� ���� �����ϰ� �Ǹ� ����� �Ǽ� �ִ��� ���̵ǰ�, ����� ��� ������������ �����ؼ� ���ϰԵǸ� �ִ��� ������ �� �ְ� �ȴ�. �⺻���ΰ��� �� ���̵��� Ǯ����.
 - �ٸ�, 0,1 �� �ɸ����� �Ǵµ�, 1*1 ���� 1+1�� ���� ũ�Ƿ�, �� ���� ��� 1�� count�ؼ� ���߿� ���� �����Ҷ� +�� ���� ����� ��Ÿ���� ���־���. 0�� ���, ������ 1���� �־��ְ� �������� ����� ����Ʈ�� �־��־���.
 �� ������, 0�� ������ ������ �ְԵǸ� (����)*(����) = (���)�� ���� �����ϱ� ������, ���� ������ �ϳ���� 0�� �ϳ��� �־��༭ ���Ѱ��� 0�� �ִ밡 �ǰ� ���־���.


"""
