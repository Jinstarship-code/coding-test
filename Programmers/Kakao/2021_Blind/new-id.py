def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    new_id = new_id.replace('~','').replace('!','').replace('@','').replace('#','').replace('$','').replace('%','').replace('^','').replace('&','').replace('*','').replace('(','').replace(')','').replace('=','').replace('+','').replace('[','').replace('{','').replace('}','').replace(']','').replace(':','').replace('?','').replace(',','').replace('<','').replace('>','').replace('/','')
    
    # 3 ~ 6단계
    while True:
        # '..' > 2 인것들을 for문 돌면서 '.'으로 치환해줌
        tmp = '.' *(len(new_id))
        if len(new_id) >1:
            for i in range(len(new_id),0,-1):
                if tmp in new_id:
                    new_id = new_id.replace(tmp,'.')
                tmp = '.' * i
        # 혹시나 빈문자열이 생겼을경우 채워줌.(5번 과정을 4번과정 앞에 해줬음)        
        if len(new_id) == 0:
            new_id += 'a'
        # 맨 앞,뒤 '.' 제거 작업 (양쪽 둘다 '.' 인경우는 loop를 한번 돌고와서 실행됨)            
        if new_id[0] == '.':
            new_id = new_id[1:]
        elif new_id[-1] == '.':
            new_id = new_id[:-1]

        # '.' 인 문자열이 위에서 제거되면 빈문자열이 되는데 빈문자열을 채워주는 작업        
        if len(new_id) == 0:
            new_id += 'a'
        
        # 6단계과정과 함께, 완벽하게 교체하지 않은 문자열체크
        if len(new_id) > 15:
            new_id = new_id[:15]
            continue
        elif len(new_id) < 3:
            new_id += new_id[-1]
            if len(new_id) < 3:
                new_id += new_id[-1]
                if new_id[-1] != '.':
                    break
            
        # 찐 마지막으로 체크
        if new_id[0] != '.' and new_id[-1] != '.':
            break
                
        
    return new_id

"""
 id :  3 ~ 15자
 - lower, - , _ , . (단, .은 첨과 끝에 사용불가능  and 연속x)
    ~ ! @ # $ % ^ & * ( ) = + [ { ] } : ? , < > / 
    1. 대문자 -> 소문자 (o)
    2. 조건을 벗어나는 모든 문자제거
    3. .. -> .
    4. . 첨 끝 제거
    5. if new_id = ''   =>  +'a'
    6. len(new_id) >= 16   => only 15   but, . 첨끝 이면 제거
    7. len(new_id) <= 2     => new_id의 마지막 문자를 len 3이 될때까지 붙임.    



# 좋은 풀이(남의 것) - sub란 것을 몰랐기 떄문에.. 
import re

def solution(new_id):
    st = new_id
    st = st.lower()
 ** st = re.sub('[^a-z0-9\-_.]', '', st)   
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st


"""