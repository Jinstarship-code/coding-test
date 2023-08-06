def solution(nums):
    answer = 0
    choice = len(nums)//2
    nums = list(set(nums))
    
    if len(nums) <= choice:
        answer = len(nums)
    else:
        answer = choice
    return answer

"""
set을 이용해서 풀면 쉽게 풀수 있다.
최대 종류를 구하면 되니,
    choice를 변수를 만들어 N/2의 수를 저장해두고
    set을 이용해서 중복 수를 제거한 리스트에 choice 만큼 뽑으면 쉽게 답을 구할 수있다.
"""