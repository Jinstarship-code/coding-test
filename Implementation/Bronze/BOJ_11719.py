while True:
  try:
    print(input())
  except EOFError:
    break
  
  """
    입력받은대로 출력하다가
    입력을 안하게 되면 (EOFError) break
  """