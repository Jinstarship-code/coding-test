def solution(name, yearning, photos):
    answer = []
    grium = {}
    for i in range(len(name)):
        grium[name[i]] = yearning[i]
    
    for photo in photos:
        tmp = 0
        for i in range(len(photo)):
            if photo[i] in grium:
                tmp += grium[photo[i]]
        answer.append(tmp)
        
    return answer


"""
python�� dict�� �̿��ϸ� ������ ���� Ǯ���ִ�.
�̸�(key)�� �߾�����(value)�� grium(dict)�� �����صΰ���
for���� ���鼭 �� ������ ���ϸ� ���� ���� ���� �� �ִ�.

"""