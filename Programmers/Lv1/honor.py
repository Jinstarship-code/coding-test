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
            else:   # goat �迭�� ��ȭ��Ű�� score�� ��� answer�� �������� �߰��ؾ��Ѵ�.
                answer.append(goat[-1])
                
           
    return answer
"""
���� ����(1)

�� ������ �ٽ��� k < score�� k > score �� �� ��찡 �ִٴ� ���̴�.
    1. k < score�� ��쿡��, ���� �Ӹ��ӿ� �������´�� �״�� �ڵ带 ¥�� Ǯ�� �׽�Ʈ���̽���
    Ǯ �� ���� ���̴�.
    
    2. k > score�� ���,
        �� ��찡 �ٽ��ε�, �� ��쿣 len(k)��ŭ�� �迭�� ����� �� �ƴ϶� len(score)��ŭ
        �迭�� ����� ����ϸ� �ȴ�.
        �������, k = 5 score=3�̶�� answer =3�� ���� ����ϸ� �ȴ�.
"""