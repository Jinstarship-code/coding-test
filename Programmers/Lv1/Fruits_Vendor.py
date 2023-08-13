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
    score �迭���� �ִ������� ���� ���̹Ƿ�,
    score �迭�� ������������ �ؼ� m��ŭ�� ���̸� ���� �迭�� �����ְ���
    �� ������ ���� ��� �ϸ� ���� ���� ã�� �� �ִ�.


"""