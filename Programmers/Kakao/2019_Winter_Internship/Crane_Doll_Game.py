def solution(board, moves):
    answer = 0
    basket = []
    
    # moves를 돌면서 인형을 바구니에 넣어주는 과정
    for move in moves:
        move -= 1 # index가 0부터 시작하므로 
        for i in range(len(board)):     # 바구니에 넣어주는 과정
            if board[i][move] != 0:
                basket.append(board[i][move])
                board[i][move] = 0
                break
        for i in range(len(basket)-1): # 바구니에 넣고 인형을 터트리는 과정
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

문제의 주의할점들

! 바구니의 크기는 무한! 
! moves를 해서 이동한 바구니에서 몇개가 터지는지 return.
! 인형 2개가 터지니까 2의 배수로 증가한다.

- 문제가 길지만, 꼼꼼히 읽고 이해하면 쉽게 풀수있는 문제다.

"""