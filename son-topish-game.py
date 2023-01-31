# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:05:02 2023

@author: Jushkin Saparmatov
"""

import random as r

def son_top (x=10):
    son = r.randint(1,x)
    print(f"Men 1 dan {x} gacha o'yladim. Topa olasizmi?")
    tahminlar = 0
    while True:
        tahminlar += 1
        tahmin = int(input(">>>"))        
        if tahmin>son:
            print("Xato. Men o'ylagan son bundan kichkina. Yana urinib ko'ring:")
        elif tahmin<son:
            print("Xato. Men o'ylagan son bundan katta. Yana urinib ko'ring:")
        else: 
            break
    
    print(f"Tabriklaymiz, {tahminlar} ta tahmin bilan topdingiz!")
    return tahminlar

def son_top_pc (x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    tahminlar = 0
    while True:
        tahminlar +=1
        if quyi != yuqori:
            tahmin = r.randint(quyi, yuqori)
        else: 
            tahmin = quyi
        javob = input(f"Siz {tahmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = tahmin - 1
        elif javob == "+":
            quyi = tahmin + 1
        else:
            break
    print(f"Men {tahminlar} ta tahmin bilan topdim!")
    return tahminlar


def play (x=10):
    yana = True
    while yana:
        tahminlar_user = son_top(x)
        tahminlar_pc = son_top_pc(x)
        
        if tahminlar_user>tahminlar_pc:
            print(f"Yutdim! {tahminlar_pc} ta tahmin bilan!")
        elif tahminlar_user<tahminlar_pc:
            print(f"Yutdingiz! Siz {tahminlar_user} ta tahmin bilan!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0): "))
play()   