# 틱택토 게임
import time

def print_board():                  # 3x3 공간 출력
    row1 = f' {board[0]} | {board[1]} | {board[2]}'
    row2 = f' {board[3]} | {board[4]} | {board[5]}'
    row3 = f' {board[6]} | {board[7]} | {board[8]}'

    print(row1, row2, row3, sep='\n')

def player1_turn():     # 첫번째 플레이어 선택
    while True:
        try:
            x = int(input('두고싶은 위치를 선택하세요 :'))
            if x not in range(1, 10):
                print('숫자를 잘못 입력하셨습니다.')
            else:                                           # 1~9 위치에서 골랐을 때
                if board[x-1] in ['●', '○']:  # 이미 누군가 둔 위치면 입력 불가
                    print('이미 입력되어 있는 위치 입니다.')
                else:
                    board[x-1] = '●'
                    break
        except ValueError:                      # 숫자가 아닌 다른 걸 입력했을 때 예외처리
            print('숫자로 입력해주세요.')

def player2_turn():
    while True:
        try:
            x = int(input('두고싶은 위치를 선택하세요 :'))
            if x not in range(1, 10):
                print('숫자를 잘못 입력하셨습니다.')
            else:  # 1~9 위치에서 골랐을 때
                if board[x - 1] in ['●', '○']:  # 이미 누군가 둔 위치면 입력 불가
                    print('이미 입력되어 있는 위치 입니다.')
                else:
                    board[x - 1] = '○'
                    break
        except ValueError:  # 숫자가 아닌 다른 걸 입력했을 때 예외처리
            print('숫자로 입력해주세요.')

def check_win(board):        # 승리 조건 확인
    win_list = [
        (board[0] == board[1] == board[2] != ' '), # 첫 번째 가로줄
        (board[3] == board[4] == board[5] != ' '), # 두 번째 가로줄
        (board[6] == board[7] == board[8] != ' '), # 세 번째 가로줄
        (board[0] == board[3] == board[6] != ' '), # 첫 번째 세로줄
        (board[1] == board[4] == board[7] != ' '), # 두 번째 세로줄
        (board[2] == board[5] == board[8] != ' '), # 세 번째 세로줄
        (board[0] == board[4] == board[8] != ' '), # 대각선
        (board[2] == board[4] == board[6] != ' ')  # 반대 대각선
    ]

    return any(win_list)

while True:
    board = [i + 1 for i in range(9)]  # 9개의 빈공간 생성
    cnt = 0  # 9번 반복 체크
    print_board()

    while True:     # 게임 시작
        player1_turn()
        cnt += 1
        print_board()
        if check_win(board) == True:        # 승리조건을 만족하면 종료
            print('player1이 승리헀습니다.')
            break
        if cnt == 9:                        # 므든 공간이 채우고 승부가 나지 않으면
            print('무승부입니다.')
            break
        time.sleep(1)

        player2_turn()
        cnt += 1
        print_board()
        if check_win(board) == True:
            print('player2이 승리헀습니다.')
            break
        time.sleep(1)

    game_try = input('게임을 다시 하시려면 1, 그만하려면 다른 숫자를 입력하세요 : ')    # 게임을 다시 시작할지 선택
    if game_try != '1':
        print('게임을 종료합니다.')
        break
