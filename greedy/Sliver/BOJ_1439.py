n = input()
a = n

n = list(n.split('0'))
n = list(filter(None, n))
a = list(a.split('1'))
a = list(filter(None, a))

print(len(n) if len(n) <= len(a) else len(a))
"""
 ���ڿ��� ��Ÿ��������, '1'�� ������ ���� '0'�� ������ ���� ���ؼ� ������ ���� ���� ���� ������ Ƚ���� ����.
"""
