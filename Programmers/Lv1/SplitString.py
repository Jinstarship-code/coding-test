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
        if prev == '': # 분리를 하고난 바로 다음 이거나 처음인경우
            prev = s[i]
            x += 1
            if len(s)-1 == i:
                answer += 1
                break
            continue
            
            
        # 분리를 위해 비교
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
    - 첫글자 x도 1회로 포함해야한다.
    - 문제가 이해하기 어려워도 한번이해하면 쉽게 풀수 있다.
"""