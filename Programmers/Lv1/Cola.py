def solution(a, b, n):
    answer = 0
    
    while n >= a:
        answer += (n//a)*b
        n = (n//a)*b + n%a
    
            
    return answer


"""
    �������� b�� 1�ΰ�쿡 ���ؼ��� ���ͼ� b�� 1�̶�� �����ϰ� Ǯ�� �ִµ�, 
    b�� 2�̻��ΰ�쵵 ������ �װ��� �����ؼ�Ǯ�� ���� Ǯ���ִ�.


"""