#BOJ_1343 �������̳�

string = input()

# .�� x�� ������.
xstring = list(string.split('.'))
dotstring = list(string.split('X'))

xstring = list(filter(None, xstring))
dotstring = list(filter(None, dotstring))

# ���ڿ� ����ϱ�
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

# ���ڿ������ֱ�
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
���� ���� �� �� �ִ� ����� ������ ������..


���� Ǯ�� ���
 - �Է¹��� ���ڿ��� X�� .�� ���� ��� ����Ʈ�� split�Ѵ�.
 - ������̿��� 'AAAA' (4��) 'BB'(2��) �̹Ƿ� 4�� ���������� 2�γ����������� ���� �ΰ��� �ϳ��� ������ �ȴ�.
 - �ٸ�, 2�� �������� ��쿣 �� ���ڿ��� ���̰� 4���� �� ��쿣 'AAAA'�� �־���� �ϱ� ������, (���ڿ� ����-2)%4�� �ؼ�  
    xstring[i] = 'A' * (len(xstring[i]) - 2) + 'B' * (len(xstring[i]) % 4) �� ���� ���ڿ��� ��ü���ش�.
- ����������, �� ����Ʈ�� ��� ���ҵ��� �����ش�.
  
"""
