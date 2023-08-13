def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    arr = []
    for i in range(0,len(score),m):
        if i+m <len(score):
            arr += [list(score[i:i+m])]
        else:
            arr += [list(score[i:])]
    
    if len(arr[-1]) != m:
        arr.pop()
    
    for i in range(len(arr)):
        min_price = min(arr[i])
        answer += min_price*m
            
    return answer


"""
    score 배열에서 최대이익을 내는 것이므로,
    score 배열을 내림차순으로 해서 m만큼의 길이를 가진 배열을 묶어주고나서
    각 상자의 값을 계산 하면 쉽게 답을 찾을 수 있다.


"""