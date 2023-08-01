import sys

arr = []
cp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for _ in range(int(sys.stdin.readline().strip())):
  a = sys.stdin.readline().strip()

  if a != 'all' and a != 'empty':
    a = list(a.split(' '))
    if a[0] == 'add':
      if int(a[1]) not in arr:
        arr.append(int(a[1]))
    elif a[0] == 'remove':
      if int(a[1]) in arr:
        arr.remove(int(a[1]))
    elif a[0] == 'check':
      if int(a[1]) in arr:
        print(1)
      else:
        print(0)
    elif a[0] == 'toggle':
      if int(a[1]) in arr:
        arr.remove(int(a[1]))
      else:
        arr.append(int(a[1]))
  else:
    if a == 'all':
      arr = cp.copy()
    elif a == 'empty':
      arr = []

"""
구현의 쉬운문제
list를 잘 써봤다면 충분히 풀수 있다.
다만, 3백만번의 처리를 해야해서 sys.stdin.readline()을 사용했다.

"""