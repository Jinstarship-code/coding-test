def solution(board, moves):
    answer = 0
    basket = []
    
    # moves�� ���鼭 ������ �ٱ��Ͽ� �־��ִ� ����
    for move in moves:
        move -= 1 # index�� 0���� �����ϹǷ� 
        for i in range(len(board)):     # �ٱ��Ͽ� �־��ִ� ����
            if board[i][move] != 0:
                basket.append(board[i][move])
                board[i][move] = 0
                break
        for i in range(len(basket)-1): # �ٱ��Ͽ� �ְ� ������ ��Ʈ���� ����
            if len(basket) == 1:
                break
            if basket[i] == basket[i+1]:
                basket.pop()
                basket.pop()
                answer += 2
                break
                
    print(basket)
    return answer


"""

������ ����������

! �ٱ����� ũ��� ����! 
! moves�� �ؼ� �̵��� �ٱ��Ͽ��� ��� �������� return.
! ���� 2���� �����ϱ� 2�� ����� �����Ѵ�.

- ������ ������, �Ĳ��� �а� �����ϸ� ���� Ǯ���ִ� ������.

"""