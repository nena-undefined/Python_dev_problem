#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#入力受け取り
s = input()

#文字列を"+"で分割
a = s.split("+")

sum = 0
for ele in a:
    #文字列->整数にしておく
    sum += int(ele)

print(sum)
