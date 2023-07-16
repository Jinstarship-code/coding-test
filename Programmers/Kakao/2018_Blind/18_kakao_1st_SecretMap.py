def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        answer.append(str(bin(arr1[i]|arr2[i]))[2:].zfill(n).replace('1','#').replace('0',' '))
    
    return answer

"""
풀이 설명:

   1. for문을 통해 각 리스트를 돌면서 bin을 계산해서 answer에 넣어준다.  
   2. bin(arr1[i]|arr2[i]) => 를 하면 두 지도의 벽(1)과 공백(0) 이 계산될것이다.
   3. 그다음, bin에서 붙는 ob를 없애주고([2:]) 
   4. .zfill(n)을 사용해 이진수 앞에 지도의 크기만큼 0이 붙어주어야한다. (지도의 크기가 6인데 이진수는 4자리일수 있다)
   5. 이진수의 숫자를 벽과 공백으로 변환
"""