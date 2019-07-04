#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys

print("0: グー, 1: チョキ, 2:パー")
print("じゃんけん...")

a = input()
if(a != "0" and a != "1" and a != "2"):
    print("0, 1, 2のいずれかを入力してください")
    sys.exit()

a = int(a)
b = random.randint(0,2)

dict = {0:"グー", 1:"チョキ", 2:"パー"}

print("あなた: " + dict[a] + ", CPU: " + dict[b])

if a == b:
    print("あいこです")
elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
    print("あなたの勝ちです")
else:
    print("CPUの勝ちです")

#<< あなた: グー, CPU: チョキ
#<< あなたの勝ちです
