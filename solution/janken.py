#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys

print("0: グー, 1: チョキ, 2:パー")
print("じゃんけん...")

#入力受け取り
a = input()

#入力が0, 1, 2以外の文字の時
if(a != "0" and a != "1" and a != "2"):
    print("0, 1, 2のいずれかを入力してください")
    sys.exit()

#文字列->整数
a = int(a)

#CPUがどの手を出すかランダムで決める
b = random.randint(0,2)

#各整数をじゃんけんの手に対応づける
dict = {0:"グー", 1:"チョキ", 2:"パー"}

print("あなた: " + dict[a] + ", CPU: " + dict[b])

#あいこの時
if a == b:
    print("あいこです")
#勝つ時
elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
    print("あなたの勝ちです")
#負ける時
else:
    print("CPUの勝ちです")
