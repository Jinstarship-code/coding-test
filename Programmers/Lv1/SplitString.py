def CmpNumber(x,notx):
    if x == notx:
        return True;
    else:
        return False;

def solution(s):
    answer = 0
    notx = 0
    x = 0
    
    prev = ''
    for i in range(len(s)):
        if prev == '': # �и��� �ϰ� �ٷ� ���� �̰ų� ó���ΰ��
            prev = s[i]
            x += 1
            if len(s)-1 == i:
                answer += 1
                break
            continue
            
            
        # �и��� ���� ��
        if prev == s[i]:
            x += 1
        else:
            notx += 1
            
        if CmpNumber(x,notx):
            prev = ''
            answer += 1
            x = 0
            notx = 0
        else:
            if len(s)-1 == i:
                answer += 1
                break
            
    return answer

"""
    - ù���� x�� 1ȸ�� �����ؾ��Ѵ�.
    - ������ �����ϱ� ������� �ѹ������ϸ� ���� Ǯ�� �ִ�.
"""