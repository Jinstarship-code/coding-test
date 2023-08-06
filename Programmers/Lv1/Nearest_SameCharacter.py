def solution(s):
    answer = []

    # 문자열을 하나하나씩 나눠 리스트에 보관.
    s = list(s[0:])
    alpha = [-1] * 26
    
    # for문을 돌면서 인덱스를 교체하면서 answer에 추가하는 과정
    for i in range(len(s)):
        tmp = ord(s[i])-ord('a')
        if alpha[tmp] == -1:
            answer.append(alpha[tmp])
        else:
            answer.append(i-alpha[tmp])
        alpha[tmp] = i
    
    return answer

"""
가장 가까운 같은 글자 문제

나 같은 경우 알파벳(26)을 담고 있는 배열을 만들어주고 난뒤,
거기에 알파벳의 인덱스를 추가하면서
-1이 아니라면 지금 인덱스 - 알파벳의 전의 인덱스를 answer에 추가해주었다.

"""