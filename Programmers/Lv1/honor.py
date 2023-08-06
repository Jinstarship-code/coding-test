def solution(k, score):
    answer = []
    goat=[]
    
    if k <= len(score):
        for i in range(k):
            goat.append(score[i])
            answer.append(min(goat))
    else:
        for i in range(len(score)):
            goat.append(score[i])
            answer.append(min(goat))
            
    goat.sort(reverse=True)
    
    if k < len(score):
        for i in range(k,len(score)):
            if score[i] > goat[-1]:
                goat.pop()
                goat.append(score[i])
                goat.sort(reverse=True)
                answer.append(goat[-1])
            else:   # goat 배열을 변화시키는 score가 없어도 answer엔 최저점을 추가해야한다.
                answer.append(goat[-1])
                
           
    return answer
"""
명예의 전당(1)

이 문제의 핵심은 k < score와 k > score 이 두 경우가 있다는 것이다.
    1. k < score의 경우에선, 직접 머리속에 생각나는대로 그대로 코드를 짜고 풀면 테스트케이스를
    풀 수 있을 것이다.
    
    2. k > score의 경우,
        이 경우가 핵심인데, 이 경우엔 len(k)만큼의 배열을 만드는 게 아니라 len(score)만큼
        배열을 만들고 출력하면 된다.
        예를들어, k = 5 score=3이라면 answer =3만 만들어서 출력하면 된다.
"""