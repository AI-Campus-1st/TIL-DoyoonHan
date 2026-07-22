import math

def quadratic(a, b, c):
    try:
        root = float(math.sqrt((b**2) - (4*a*c)))
    except ValueError:
        # 4ac 가 b^2 보다 커서 sqrt에 negative value가 들어간 경우.
        print("공식에 사용될 값이 잘못되었습니다.")
        return 0

    # +의 경우
    pos_ans = (-b + root)/(2*a)

    # -의 경우
    neg_ans = (-b - root)/(2*a)

    print(pos_ans, neg_ans)
    return 0


if __name__== "__main__":
    print("근의 공식에 사용될 a, b, c 값을 입력하세요.")
    a = int(input("a: "))
    b = int(input("b: ")) 
    c = int(input("c: "))
    quadratic(a, b, c)