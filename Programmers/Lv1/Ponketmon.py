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
set�� �̿��ؼ� Ǯ�� ���� Ǯ�� �ִ�.
�ִ� ������ ���ϸ� �Ǵ�,
    choice�� ������ ����� N/2�� ���� �����صΰ�
    set�� �̿��ؼ� �ߺ� ���� ������ ����Ʈ�� choice ��ŭ ������ ���� ���� ���� ���ִ�.
"""