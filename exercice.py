#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
# import sys
from exo6 import frequence
from turtle import *
# import re


# TODO: Définissez vos fonction ici
def calc_masse_volume(a=2, b=4, c=6, mv=10) -> tuple:
    volume = (math.pi * 4*a*b*c)/3
    masse = mv * volume
    return volume, masse

def proportion(sentence: str):
    dct_in_order = frequence(sentence)
    max, letter = 0, ""
    for key, value in dct_in_order.items():
        if value > max:
            max = value
            letter = key
    return letter

def draw_branch(branch_len, pen_size, angle): #CP
    if branch_len > 0 and pen_size > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        left(angle * 2)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)

def tree():
    color("green")
    draw_branch(70,7,40)
    speed(100)
    done()

def saisie_valide(dna: str) -> bool:
    letters = ["a", "t", "g", "c"]
    
    if len(dna) < 1: return False
    
    for letter in dna:
        if letter not in letters:
            return False

    return True

def saisie() -> str:
    dna = input(f"Veuillez saisir une chaine d'ADN valide : ")
    while not saisie_valide(dna):
        dna = input(f"Veuilleuz saisir une chaine d'ADN valide (a, t, g, c): ")
    return dna

def sequence(dna: str, sequence: str) -> int:
    return dna.count(sequence)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    tree()
    
    # print(calc_masse_volume())

    # dna = saisie()
    # print(dna)
    # print(sequence(dna, "tta"))


