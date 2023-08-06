def solution(s):
    answer = []

    # ���ڿ��� �ϳ��ϳ��� ���� ����Ʈ�� ����.
    s = list(s[0:])
    alpha = [-1] * 26
    
    # for���� ���鼭 �ε����� ��ü�ϸ鼭 answer�� �߰��ϴ� ����
    for i in range(len(s)):
        tmp = ord(s[i])-ord('a')
        if alpha[tmp] == -1:
            answer.append(alpha[tmp])
        else:
            answer.append(i-alpha[tmp])
        alpha[tmp] = i
    
    return answer

"""
���� ����� ���� ���� ����

�� ���� ��� ���ĺ�(26)�� ��� �ִ� �迭�� ������ְ� ����,
�ű⿡ ���ĺ��� �ε����� �߰��ϸ鼭
-1�� �ƴ϶�� ���� �ε��� - ���ĺ��� ���� �ε����� answer�� �߰����־���.

"""