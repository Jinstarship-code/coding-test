def solution(new_id):
    answer = ''
    # 1�ܰ�
    new_id = new_id.lower()
    
    # 2�ܰ�
    new_id = new_id.replace('~','').replace('!','').replace('@','').replace('#','').replace('$','').replace('%','').replace('^','').replace('&','').replace('*','').replace('(','').replace(')','').replace('=','').replace('+','').replace('[','').replace('{','').replace('}','').replace(']','').replace(':','').replace('?','').replace(',','').replace('<','').replace('>','').replace('/','')
    
    # 3 ~ 6�ܰ�
    while True:
        # '..' > 2 �ΰ͵��� for�� ���鼭 '.'���� ġȯ����
        tmp = '.' *(len(new_id))
        if len(new_id) >1:
            for i in range(len(new_id),0,-1):
                if tmp in new_id:
                    new_id = new_id.replace(tmp,'.')
                tmp = '.' * i
        # Ȥ�ó� ���ڿ��� ��������� ä����.(5�� ������ 4������ �տ� ������)        
        if len(new_id) == 0:
            new_id += 'a'
        # �� ��,�� '.' ���� �۾� (���� �Ѵ� '.' �ΰ��� loop�� �ѹ� ����ͼ� �����)            
        if new_id[0] == '.':
            new_id = new_id[1:]
        elif new_id[-1] == '.':
            new_id = new_id[:-1]

        # '.' �� ���ڿ��� ������ ���ŵǸ� ���ڿ��� �Ǵµ� ���ڿ��� ä���ִ� �۾�        
        if len(new_id) == 0:
            new_id += 'a'
        
        # 6�ܰ������ �Բ�, �Ϻ��ϰ� ��ü���� ���� ���ڿ�üũ
        if len(new_id) > 15:
            new_id = new_id[:15]
            continue
        elif len(new_id) < 3:
            new_id += new_id[-1]
            if len(new_id) < 3:
                new_id += new_id[-1]
                if new_id[-1] != '.':
                    break
            
        # �� ���������� üũ
        if new_id[0] != '.' and new_id[-1] != '.':
            break
                
        
    return new_id

"""
 id :  3 ~ 15��
 - lower, - , _ , . (��, .�� ÷�� ���� ���Ұ���  and ����x)
    ~ ! @ # $ % ^ & * ( ) = + [ { ] } : ? , < > / 
    1. �빮�� -> �ҹ��� (o)
    2. ������ ����� ��� ��������
    3. .. -> .
    4. . ÷ �� ����
    5. if new_id = ''   =>  +'a'
    6. len(new_id) >= 16   => only 15   but, . ÷�� �̸� ����
    7. len(new_id) <= 2     => new_id�� ������ ���ڸ� len 3�� �ɶ����� ����.    



# ���� Ǯ��(���� ��) - sub�� ���� ������ ������.. 
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