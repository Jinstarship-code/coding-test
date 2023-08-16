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
    ������ϴ� ����� ���� �˸� ���� Ǯ���ִ�.
    ���⼭ n�� �������� �����϶� �ѹ��� �־��ָ�ȴ�.


"""