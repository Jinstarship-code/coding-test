def solution(babbling):
    answer = 0
    ong = ["aya","ye","woo","ma"]
    
    for i in range(len(babbling)):
        for on in ong:
            if (on in babbling[i]) and (on*2 not in babbling[i]):
                babbling[i]=babbling[i].replace(on,'*')
    
        if all(char =='*' for char in babbling[i]):
            answer +=1
    
    print(babbling)
    return answer



"""
 �˾��̸� �迭�� �����صΰ� 
 �� ���ڿ����� for���� ���鼭 replace�� ���ְ� ����
 all �Լ��� ��� '*'�� �̷�����ִٸ� �����Ҽ� �ִ� �����̹Ƿ� answer +=1�� ���ش�.



"""