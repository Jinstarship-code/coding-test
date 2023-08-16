def FindYakSoo(n):
    tmp = []
    
    for i in range(1,int(n**(1/2))+1):
        if n % i ==0:
            tmp.append(i)
            if i**2 != n:
                tmp.append(n//i)
    return len(tmp)


def solution(number, limit, power):
    answer = 0
    arr = []
    arr.append(1)
    for i in range(2,number+1):
        arr.append(FindYakSoo(i))
    
    for i in range(len(arr)):
        if arr[i] > limit:
            arr[i] = power
    
    return sum(arr)

"""
    약수구하는 방법만 할줄 알면 쉽게 풀수있다.
    여기서 n의 제곱근이 정수일때 한번만 넣어주면된다.


"""