def solution(n, m, section):
    answer = 1
    ran = section[0] + m - 1
    for i in range(1,len(section)):
        if ran >= section[i]: 
            continue
        else:
            ran = section[i]+m-1
            answer +=1
        
    return answer

"""
nĭ m������ �ѷ� section,

�ϳ��ϳ��� ���ؼ� ĥ�ϸ� �ð��ʰ��� ����.
����,, section�� ���س����鼭 ran�̶�� ��ĥ�ϴ� ������ ������ �����
section�� for������ ���鼭 ���� ���̸� continue�ϰ� �ƴϸ� +1���ִ� ������ Ǯ����.
"""