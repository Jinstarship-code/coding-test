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
python의 dict을 이용하면 굉장히 쉽게 풀수있다.
이름(key)의 추억점수(value)를 grium(dict)에 저장해두고난뒤
for문을 돌면서 각 점수를 더하면 쉽게 답을 구할 수 있다.

"""