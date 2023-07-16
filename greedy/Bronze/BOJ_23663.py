T = int(input())

while T != 0:
  n,m = map(int,input().split())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))
  
  if len(a) > len(b):
    print("No")
  else:
    print("Yes")
  
  T -=1

  """
  문제 설명:
    Red Player, White Player둘이 이상한 바둑을 하고 있음
    각각 n, m 개의 pile들을 가지고 있는데, 한턴에 한 뭉텅이씩 
    제거가 가능함.

    쉽게 n의 수를 list a로 받고, m의 수를 list b로 받은뒤
    len(a) > len(b)이면 red 플레이어가 지는거고,
    그반대면 red가 이기는 경우가됨.
  """