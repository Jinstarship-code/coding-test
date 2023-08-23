def solution(today, terms, privacies):
    answer = []
    termsDict = {}
    
    today = list(today.split('.'))
    for i in range(len(today)):
        today[i] = int(today[i])
        
    for i in range(len(terms)):
        terms[i] = terms[i].split(' ')
        terms[i][1] = int(terms[i][1])
        termsDict[terms[i][0]] = terms[i][1]
        
    for i in range(len(privacies)):
        privacies[i] = privacies[i].replace(' ','.').split('.')
        privacies[i][0] = int(privacies[i][0])
        privacies[i][1] = int(privacies[i][1]) + termsDict[privacies[i][3]]
        privacies[i][2] = int(privacies[i][2])-1
        
        if privacies[i][1]  > 12 and privacies[i][1]% 12 != 0:
            privacies[i][0] += privacies[i][1]//12
            privacies[i][1] = privacies[i][1]%12
        elif privacies[i][1] % 12 == 0:
            privacies[i][0] += privacies[i][1] //12 -1
            privacies[i][1] = 12            
            
            
        if privacies[i][2] == 0:
            privacies[i][2] = 28
            privacies[i][1] -= 1
            # 1�� 1�Ͽ��� 12�� 28�ϱ��� �Ǵ� ��ȿ�Ⱓ �����ؾ���.
            if privacies[i][1] == 0:
                privacies[i][1] = 12
                privacies[i][0] -= 1
        
        if privacies[i][0] < today[0]:
            answer.append(i+1)
        elif privacies[i][0] > today[0]:
            continue
        else: # ������ ���� ��
            if privacies[i][1] < today[1]:
                answer.append(i+1)
            elif privacies[i][1] > today[1]:
                continue
            else: # ���� ���� ��
                if privacies[i][2] < today[2]:
                    answer.append(i+1)
                
    print(privacies)
    return answer

"""
�������� n�� ����� ��ȿ���.
���� ��¥�� �������� �ı��ؾ��ϴ� ������ ��ȣ(��������)�� ����ض�.

�Ѷ� �Ѷ� �ͱ۾���..��������.....
"""