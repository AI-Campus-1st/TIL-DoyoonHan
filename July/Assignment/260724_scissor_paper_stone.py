import random
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def game():
    answer_list = ["가위", "바위", "보", "종료", "그래프", "승률"]
    hands = ["가위", "바위", "보"]

    con, cur = database_creation()

    data = cur.execute('''
                SELECT * FROM winrate WHERE ID = 1
            ''').fetchall()[0]

    win, lose, draw, total = data[1], data[2], data[3], data[4]

    gameplay = True
    while gameplay:
        computer = random.choice(hands)
        player = "null"
        player = input("Player: ").strip()
        # 잘못된 단어를 입력했을 때
        if player not in answer_list:
            print(f"\033[F잘못된 입력입니다.")
            continue
        result = check_winner(player, computer)

        # 게임 종료
        if result == 3:
            print(f"\033[F게임을 종료합니다.")
            gameplay = False
            con.close()
        # 승률
        elif result == 4:
            winrate = (win/total)*100
            print(f"\033[F현재까지 승률 : {winrate:.1f}%")
        # 그래프
        elif result == 5:
            x = np.array(["win", "lose", "draw"])
            y = np.array([win, lose, draw])

            plt.bar(x,y)
            plt.show()
        # 무승부
        elif result == 0: 
            print(f"\033[FPlayer: {player},    Computer: {computer}, 무승부")
            draw += 1
            total += 1
            statement = ('''
                    UPDATE winrate
                    SET draw = ?, total = ?
                    WHERE id = 1
                ''')
            cur.execute(statement, (draw, total))
            con.commit()
        # 플레이어 승리
        elif result == 1:
            print(f"\033[FPlayer: {player},    Computer: {computer}, 플레이어 승리")
            win += 1
            total += 1
            statement = ('''
                    UPDATE winrate
                    SET win = ?, total = ?
                    WHERE id = 1
                ''')
            cur.execute(statement, (win, total))
            con.commit()
        # 플레이어 패배
        elif result == 2:
            print(f"\033[FPlayer: {player},    Computer: {computer}, 플레이어 패배")
            lose += 1
            total += 1
            statement = ('''
                    UPDATE winrate
                    SET lose = ?, total = ?
                    WHERE id = 1
                ''')
            cur.execute(statement, (lose, total))
            con.commit()
        
def check_winner(player, computer):
    # 3 종료
    if player == "종료":
        return 3
    # 4 승률
    elif player == "승률":
        return 4
    # 5 그래프
    elif player == "그래프":
        return 5

    # 0: 무승부
    elif player == computer:
        return 0
    # 1: 플레이어 승리
    elif (player == "가위" and computer == "보") or (player == "바위" and computer == "가위") or (player == "보" and computer == "바위"):
        return 1
    # 2: 플레이어 패배
    else:
        return 2
        
        
def database_creation():
    con = sqlite3.connect("winrate.db")
    cur = con. cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS winrate(
            ID int PRIMARY KEY,
            win int,
            lose int,
            draw int,
            total int 
        )''')

    present = cur.execute('''
            SELECT * FROM winrate WHERE ID = 1
        ''')

    if len(present.fetchall()) == 0:
        cur.execute("INSERT INTO winrate VALUES ('1', '0', '0' ,'0', '0')")
    
    return con, cur

if __name__ == "__main__":
    game()