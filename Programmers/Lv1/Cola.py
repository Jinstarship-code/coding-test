def solution(a, b, n):
    answer = 0
    
    while n >= a:
        answer += (n//a)*b
        n = (n//a)*b + n%a
    
            
    return answer


"""
    문제에선 b가 1인경우에 대해서만 나와서 b가 1이라고 착각하고 풀수 있는데, 
    b가 2이상인경우도 있으니 그것을 주의해서풀면 쉽게 풀수있다.


"""