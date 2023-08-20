def solution(dartResult):
    answer = [] # 각 라운드별 점수를 담을 예정
    dartArr= [] # 라운드별 점수(문자열)
    powScore = {'S':1,'D':2,'T':3} # 제곱수를 dict으로 만들어서 해당되는 문자열만큼 제곱시켜주게
    index = 0
    for i in range(len(dartResult)):
        if dartResult[i].isalpha():
            # (i+1)가 number 숫자라면 옵션이 x
            if i+1 == len(dartResult) or dartResult[i+1].isnumeric():
                dartArr.append(dartResult[index:i+1])
                index = i+1
            # (i+1)이 옵션일때.
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
        else: #10인데 옵션x
            answer.append(pow(10,powScore[dartArr[0][2]]))
    # 10에 옵션까지 있는 경우
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
            else: # 10에 옵션x
                answer.append(pow(10,powScore[dartArr[i][2]]))
        else: #10에 옵션o
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
4. *(이전 점수*2+지금 점수*2) #
5. * 첫번째도 가능 (지금점수*2)
6. * 중첩가능 ** 이면 (이이전 점수*2+이전 점수*4+지금 점수*2)
7. * # 중첩가능
8. S,D,T는 한번씩만 존재
9. * # 가 있을수도 없을수도.


tip) 10일때를 항상 고려해야한다.
--------------------------------------------------------------

풀긴 풀었는데,, 너무 하드코딩식으로 풀었던거 같다.
아래는 깔끔한 해답을 가져왔다. 아직 갈길이 멀었다

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