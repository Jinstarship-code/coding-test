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
    주의할점. goal이 항상 card1과 card2의 합의 길이가 되는 것이아니고,
    그 중간에서 goal이 완성될 수 있다.

    그래서 나같은 경우 for문에서 break될시 -1을 넣어서 -1의 값이 있으면 No
    그렇지 않으면 goal이 완성 되었으므로 Yes를 출력한다.


"""