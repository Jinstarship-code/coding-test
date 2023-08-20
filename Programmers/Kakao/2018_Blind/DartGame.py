def solution(dartResult):
    answer = [] # �� ���庰 ������ ���� ����
    dartArr= [] # ���庰 ����(���ڿ�)
    powScore = {'S':1,'D':2,'T':3} # �������� dict���� ���� �ش�Ǵ� ���ڿ���ŭ ���������ְ�
    index = 0
    for i in range(len(dartResult)):
        if dartResult[i].isalpha():
            # (i+1)�� number ���ڶ�� �ɼ��� x
            if i+1 == len(dartResult) or dartResult[i+1].isnumeric():
                dartArr.append(dartResult[index:i+1])
                index = i+1
            # (i+1)�� �ɼ��϶�.
            else:
                dartArr.append(dartResult[index:i+2])
                index = i+2
    
    
    if len(dartArr[0]) == 2:
        answer.append(pow(int(dartArr[0][0]),powScore[dartArr[0][1]]))
    elif len(dartArr[0])==3:
        if dartArr[0][1].isalpha():
            if dartArr[0][2] == '#':
                answer.append(-1*pow(int(dartArr[0][0]),powScore[dartArr[0][1]]))
            else:
                answer.append(pow(int(dartArr[0][0]),powScore[dartArr[0][1]])*2)
        else: #10�ε� �ɼ�x
            answer.append(pow(10,powScore[dartArr[0][2]]))
    # 10�� �ɼǱ��� �ִ� ���
    else:
        if dartArr[0][3] == '#':
            answer.append(-1*pow(10,powScore[dartArr[0][2]]))
        else:
            answer.append(pow(10,powScore[dartArr[0][2]])*2)
    
    
    for i in range(1,len(dartArr)):
        if len(dartArr[i]) == 2:
            answer.append(pow(int(dartArr[i][0]),powScore[dartArr[i][1]]))
        elif len(dartArr[i]) == 3:
            if dartArr[i][2] == '#':
                answer.append(-1*pow(int(dartArr[i][0]),powScore[dartArr[i][1]]))
            elif dartArr[i][2] == '*':
                answer.append(pow(int(dartArr[i][0]),powScore[dartArr[i][1]])*2)
                answer[i-1] = answer[i-1]*2
            else: # 10�� �ɼ�x
                answer.append(pow(10,powScore[dartArr[i][2]]))
        else: #10�� �ɼ�o
            if dartArr[i][3] == '#':
                answer.append(-1*pow(10,powScore[dartArr[i][2]]))
            else:
                answer.append(pow(10,powScore[dartArr[i][2]])*2)
                answer[i-1] *= 2
                
    print(answer)
    return sum(answer)

"""
1. 3 times
2. 0 ~ 10 score
3. S D T
4. *(���� ����*2+���� ����*2) #
5. * ù��°�� ���� (��������*2)
6. * ��ø���� ** �̸� (������ ����*2+���� ����*4+���� ����*2)
7. * # ��ø����
8. S,D,T�� �ѹ����� ����
9. * # �� �������� ��������.


tip) 10�϶��� �׻� ����ؾ��Ѵ�.
--------------------------------------------------------------

Ǯ�� Ǯ���µ�,, �ʹ� �ϵ��ڵ������� Ǯ������ ����.
�Ʒ��� ����� �ش��� �����Դ�. ���� ������ �־���

import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

"""