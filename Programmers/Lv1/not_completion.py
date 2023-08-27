import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    print(collections.Counter(participant))
    return list(answer.keys())[0]



"""
# 나의 풀이 
def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for a,b in zip(participant, completion):
        if a != b:
            return a

    return participant[-1]
"""