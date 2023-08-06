def solution(food):
    answer = ''
    
    for i in range(1,len(food)):
        answer += str(i)*(food[i]//2)
    tmp = answer[-1::-1]
    
    answer += '0'
    answer+=tmp
    return answer

"""

문제는 간단하다
food 배열을 받고
문자열 가운데에0이 있는 palindrome문자열을 만들어주면된다.


"""