from fractions import Fraction
from functools import reduce


dice_dist = {
    2: Fraction(1, 36), 3: Fraction(2, 36),
    4: Fraction(3, 36), 5: Fraction(4, 36),
    6: Fraction(5, 36), 7: Fraction(6, 36),
    8: Fraction(5, 36), 9: Fraction(4, 36),
    10: Fraction(3, 36), 11: Fraction(2, 36),
    12: Fraction(1, 36)
}


def prob_sum(L):
    return sum(dice_dist[x] for x in L)


def input_again():
    t = int(input(("1：一样 2：不一样")))
    if t == 1:
        return True
    return False

def dice():
    # 输入并计算各例子的输赢之和
    lost = list(map(int, input("输入失败点数列表：").split()))
    win = list(map(int, input("输入胜利点数列表：").split()))
    p_lost = prob_sum(lost)
    p_win = prob_sum(win)

    # 输入赢的倍数
    b = int(input("输入倍数：")) - 1

    real_lost = p_lost / (p_lost + p_win)
    real_win = p_win / (p_lost + p_win)
    round_num = 1 / (p_lost + p_win)

    f = real_win - real_lost / b

    print("失败概率:", real_lost)
    print("成功概率:", real_win)
    print("预期轮数：", round_num)
    print("投资比例：", f)
    print()

    # 输入资金
    a = int(input("输入资金："))
    print(f"请投入${float(a*f)}")

    if_again = input_again()
    while if_again:
        print(if_again)
        a = int(input("输入资金："))
        print(f"请投入${float(a*f)}")
        if_again = input_again()
    dice()

dice()
