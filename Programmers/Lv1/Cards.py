def solution(cards1, cards2, goal):
    answer = ''
    i,j = 0,0
    cards1.append('')
    cards2.append('')
    for k in range(len(goal)):
        if goal[k] == cards1[i]:
            i += 1
        elif goal[k] == cards2[j]:
            j += 1
        else:
            answer = -1
            break
            
    if answer == -1:
        answer = "No"
    else:
        answer = "Yes"
        
    
    return answer

"""
    ��������. goal�� �׻� card1�� card2�� ���� ���̰� �Ǵ� ���̾ƴϰ�,
    �� �߰����� goal�� �ϼ��� �� �ִ�.

    �׷��� ������ ��� for������ break�ɽ� -1�� �־ -1�� ���� ������ No
    �׷��� ������ goal�� �ϼ� �Ǿ����Ƿ� Yes�� ����Ѵ�.


"""