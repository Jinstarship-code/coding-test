def solution(babbling):
    answer = 0
    ong = ["aya","ye","woo","ma"]
    
    for i in range(len(babbling)):
        for on in ong:
            if (on in babbling[i]) and (on*2 not in babbling[i]):
                babbling[i]=babbling[i].replace(on,'*')
    
        if all(char =='*' for char in babbling[i]):
            answer +=1
    
    print(babbling)
    return answer



"""
 옹알이를 배열에 저장해두고 
 각 문자열마다 for문을 돌면서 replace를 해주고 나서
 all 함수로 모두 '*'로 이루어져있다면 발음할수 있는 문자이므로 answer +=1을 해준다.



"""