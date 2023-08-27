def solution(id_list, report, k):
    answer = [0] * len(id_list) 
    report = list(set(report)) # �ߺ��� �Ű� ����
    count = [0 for id in id_list] # id_list������� �Ű���� 
    mem = [[] for id in id_list]  # �Ű���� ����� �ε����� �Ű��� ����� ����
    
    for i in range(len(report)):
        report[i] = report[i].split()
        count[id_list.index(report[i][1])] += 1
        mem[id_list.index(report[i][0])] += [report[i][-1]]
        
    for i in range(len(mem)):
        for j in range(len(mem[i])):
            if count[id_list.index(mem[i][j])] >= k:
                answer[i] += 1

    return answer



"""
 - 1 ���� 1�Ű�
    - �Ѹ��� ������״� �Ű� 1�� �� �̻� 1������
 - k �� �Ű� ���� ������ ���� -> �Ű��� �������� ��������

 - ���� ���ϼ��� ������� ����.
"""