def solution(food):
    answer = ''
    
    for i in range(1,len(food)):
        answer += str(i)*(food[i]//2)
    tmp = answer[-1::-1]
    
    answer += '0'
    answer+=tmp
    return answer

"""

������ �����ϴ�
food �迭�� �ް�
���ڿ� �����0�� �ִ� palindrome���ڿ��� ������ָ�ȴ�.


"""