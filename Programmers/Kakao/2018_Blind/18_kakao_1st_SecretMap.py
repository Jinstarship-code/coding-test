def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        answer.append(str(bin(arr1[i]|arr2[i]))[2:].zfill(n).replace('1','#').replace('0',' '))
    
    return answer

"""
Ǯ�� ����:

   1. for���� ���� �� ����Ʈ�� ���鼭 bin�� ����ؼ� answer�� �־��ش�.  
   2. bin(arr1[i]|arr2[i]) => �� �ϸ� �� ������ ��(1)�� ����(0) �� ���ɰ��̴�.
   3. �״���, bin���� �ٴ� ob�� �����ְ�([2:]) 
   4. .zfill(n)�� ����� ������ �տ� ������ ũ�⸸ŭ 0�� �پ��־���Ѵ�. (������ ũ�Ⱑ 6�ε� �������� 4�ڸ��ϼ� �ִ�)
   5. �������� ���ڸ� ���� �������� ��ȯ
"""