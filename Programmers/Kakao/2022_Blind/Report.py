def solution(id_list, report, k):
    answer = [0] * len(id_list) 
    report = list(set(report)) # 중복된 신고 제거
    count = [0 for id in id_list] # id_list순서대로 신고받은 
    mem = [[] for id in id_list]  # 신고받은 사람의 인덱스에 신고한 사람들 나열
    
    for i in range(len(report)):
        report[i] = report[i].split()
        count[id_list.index(report[i][1])] += 1
        mem[id_list.index(report[i][0])] += [report[i][-1]]
        
    for i in range(len(mem)):
        for j in range(len(mem[i])):
            if count[id_list.index(mem[i][j])] >= k:
                answer[i] += 1

    return answer



"""
 - 1 유저 1신고
    - 한명의 대상한테는 신고가 1번 그 이상도 1번으로
 - k 번 신고 받은 유저는 정지 -> 신고한 유저에게 메일전송

 - 받은 메일수를 순서대로 리턴.
"""