import random


directions = ["left", "middle", "right"]
score_you = 0
score_cpt = 0


def cpt_action(direction_you, round_): # True 是你的回合，False 是对方回合
    global score_you, score_cpt
    direction_cpt = random.choice(directions)
    print(f"电脑选择了{direction_cpt}")
    if direction_you == direction_cpt:
        print("球被扑救了")
    elif round_:
        score_you += 1
        print("你得分了")
    else:
        score_cpt += 1
        print("电脑得分了")


def ifround(round_):
    if round_:
        print("你的回合")
    else:
        print("对手的回合")


def earlyend(round_num, score_you, score_cpt):
    if round_num == 3 and score_you == 2 and score_cpt == 0:
        print("You win")
        exit()
    if round_num == 4:
        if (score_you == 2 and score_cpt <= 1) or (score_you == 1 and score_cpt == 0):
             print("You win")
             exit()
        if score_you == 0 and score_cpt == 2:
             print("You lose")
             exit()


round_ = True
round_num = 1
while True:
    print(f"现在是第{round_num}回合", end=" ")
    ifround(round_)
    direction_you = input("请输入你选择的方向\n")
    cpt_action(direction_you, round_)
    print(f"现在的比分是{score_you}:{score_cpt}")
    earlyend(round_num, score_you, score_cpt)
    if round_num >= 5:
        if score_you > score_cpt:
            print("You win")
            exit()
        if score_cpt > score_you:
            print("You lose")
            exit()
    round_ = not round_
    round_num += 1