import sys

# size만큼 입력받고 그 size만큼의 정사각형이 존재하는지 찾는다.
def FindSquare(s):
  for i in range(n-s+1):
    for j in range(m-s+1):
      # 만약 있으면 true
      if rect[i][j] == rect[i][j+s-1] == rect[i+s-1][j] == rect[i+s-1][j+s-1]:
        return True
  return False


n, m = map(int, sys.stdin.readline().rstrip().split())

rect = []
tmp = ''
# 입출력 받아서 이중 리스트로 만들어놓음
for _ in range(n):
  tmp = sys.stdin.readline().rstrip()
  tmp = list(tmp)
  for i in range(len(tmp)):
    tmp[i] = int(tmp[i])
  rect += [tmp]

# 정사각형을 찾아야하므로 n,m중 작은 수에서부터 찾으면 된다.
size = min(n,m)

# size를 돌면서 FindSqure를 한다.
for i in range(size,0,-1):
  if FindSquare(i):
    print(i**2)
    break
  
  """
    정사각형을 찾는 문제
  """