def omok():
    # False일 경우 게임종료/ 보드만들기 성공.
    board_creation = True
    while board_creation:
        board_size = int(input("판 크기를 입력해 주세요: "))
        # 사용자가 0을 입력하면 게임 종료
        if board_size == 0:
            board_creation = False
            print("게임이 종료되었습니다.")
            break
        elif board_size < 5:
            print("판 크기는 5 이상이어야 합니다. 다시 입력해 주세요.")
            continue
        else:
            board_creation = False

    board = create_board(board_size)

    gameplay = True
    player = True  # True: 플레이어1, False: 플레이어2

    print("0을 입력하면 게임이 종료됩니다.")
    print("게임 시작!")
    while gameplay:
        print_board(board)

        if player:
            coordinate = input("1플레이어 바둑돌 위치 x y: ")
            stone = 'O'
        else:
            coordinate = input("2플레이어 바둑돌 위치 x y: ")
            stone = 'X'
        try:
            if coordinate == '0':
                print("게임이 종료되었습니다.")
                break
            coordinates = coordinate.split()
            board, success = replace_stone(board, int(coordinates[0]), int(coordinates[1]), stone, board_size)
        except IndexError:
            print("잘못된 입력입니다. 다시 입력해 주세요.")
            continue
        except ValueError:
            print("잘못된 입력입니다. 다시 입력해 주세요.")
            continue

        if not success:
            # 돌을 놓지 못했으므로 플레이어를 바꾸지 않고 다시 입력 받음
            continue

        # 돌을 놓은 후 승리 조건 확인
        if check_winner(board, stone, board_size):
            print_board(board)
            if player:
                print("1플레이어가 이겼습니다!")
                print("게임이 종료되었습니다.")
            else:
                print("2플레이어가 이겼습니다!")
                print("게임이 종료되었습니다.")
            gameplay = False
        else:
            # 돌을 놓고 플레이어 변경
            player = not player

def print_board(board):
    for row in board:
        print(' '.join(row))


def create_board(size: int):
    board = []
    for i in range(size):
        row = ['+'] * size
        board.append(row)
    return board

def replace_stone(board, row: int, col: int, stone: str, board_size: int):
    try:
        if board[board_size - 1 - col][row] != '+':
            print("이미 돌이 놓여져 있습니다. 다른 위치를 선택해 주세요.")
            return board, False
        else:
            board[board_size - 1 - col][row] = stone
            return board, True
    except IndexError:
        print("잘못된 좌표입니다. 다시 입력해 주세요.")
        return board, False

def check_winner(board, stone: str, board_size: int):
    # 가로, 세로, 대각선 방향으로 5개의 돌이 연속으로 있는지 확인
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == stone:
                # 가로 확인
                if col <= board_size - 5 and all(board[row][col + k] == stone for k in range(5)):
                    return True
                # 세로 확인
                elif row <= board_size - 5 and all(board[row + k][col] == stone for k in range(5)):
                    return True
                # 대각선 확인 (왼쪽 위에서 오른쪽 아래)
                elif row <= board_size - 5 and col <= board_size - 5 and all(board[row + k][col + k] == stone for k in range(5)):
                    return True
                # 대각선 확인 (오른쪽 위에서 왼쪽 아래)
                elif row >= 4 and col <= board_size - 5 and all(board[row - k][col + k] == stone for k in range(5)):
                    return True                        
    return False

if __name__== "__main__":
    omok()