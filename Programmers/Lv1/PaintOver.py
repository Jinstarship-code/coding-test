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
n칸 m길이의 롤러 section,

하나하나씩 비교해서 칠하면 시간초과가 난다.
따라서,, section만 비교해나가면서 ran이라는 덧칠하는 범위의 변수를 만들고
section을 for문으로 돌면서 범위 안이면 continue하고 아니면 +1해주는 식으로 풀었다.
"""