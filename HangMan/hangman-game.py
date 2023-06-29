#!/usr/bin/env python
# coding: utf-8


from random import choice
from os import name, system
from time import sleep, time
from new_inpt_time import inputimeout
import json

def draw_hg(chars, n=0):
    for i in chars:
        print(i)

    for i in range(n):
        print(space+'  |')
    print(space+'  ====')

def draw_letter(word, right_words):
    print("    Category : ", ctg.capitalize())
    print('    Hang-man-word :   ', end='')
    global c
    for i in word:
        w = '_'
        if i in right_words or i=='-':
            w = i.upper()
            if i=='-':w='-'
            c+=1
        print(f' {w} ', end='')
    
    let = 'letters' if len(word)-c > 1 else 'letter'
    print(f" (#{len(word)-c} {let} remaining)")

def backspace():
    system('cls' if name in ['nt', 'dos'] else 'clear')

def check(word, right_letters):
    add=0
    if '-' in word: add =1
    return len(set(word))==len(right_letters)+add

def game_over(word):
    backspace()
    print(ascii_img)
    print("\n     Correct-word : " + word.upper())
    print("""
                 ____                                                        
                / ___|  __ _  _ __ ___    ___          ___ __   __ ___  _ __ 
               | |  _  / _` || '_ ` _ \  / _ \ _____  / _ \\ \ / // _ \| '__|
               | |_| || (_| || | | | | ||  __/|_____|| (_) |\ V /|  __/| |   
                \____| \__,_||_| |_| |_| \___|        \___/  \_/  \___||_|   
    """)
    sleep(4)
    backspace()
    exit()

def openJsonFile(filename):
    with open(filename, "r") as fIn:
        return json.load(fIn)

def resize_terminal(rows, columns):
    win_cmd = f"mode con: cols={columns} lines={rows}"
    lin_cmd = f"printf '\\e[8;{rows};{columns}t'"
    cmd = win_cmd if name in ['dos', 'nt'] else  lin_cmd
    system(cmd)


space=' '*5

err = {1:4, 2:3, 3:2, 4:2, 5:2, 6:1, 7:1}
fig = [space + '  +--------'] + [space+'  |']*5
err1 = [space + '  +--------', space+'  |    |  ']  
err2 = err1 + [space+'  |    O ']  
err3 = err2 + [space+'  |    |']
err4 = err2 + [space+'  |   /|']
err5 = err2 + [space+'  |   /|\\']
err6 = err5 + [space+'  |   /']
err7 = err5 + [space+'  |   / \\']


FILENAME = "HangManData.json"
categories = openJsonFile(FILENAME)
resize_terminal(40, 100)
backspace()
print("""

         _     _                                                
        | |   | |                                               
        | |__ | |  ____  ____    ____  ___  ____    ____  ____  
        |  __)| | / _  ||  _ \  / _  |(___)|    \  / _  ||  _ \ 
        | |   | |( ( | || | | |( ( | |     | | | |( ( | || | | |
        |_|   |_| \_||_||_| |_| \_|| |     |_|_|_| \_||_||_| |_|
                               (_____|                          

""")


total_time = 90 # Game-time
e_cnt, c = 0, 0
right_letters = []
used_letters = []


ascii_img = '''
                    ___________.._______
                    | .__________))______|
                    | | / /      ||
                    | |/ /       ||
                    | | /        ||.-''.
                    | |/         |/  _  \\
                    | |          ||  `/,|
                    | |          (\\`_.'
                    | |         .-`--'.
                    | |        /Y . . Y\\
                    | |       // |   | \\
                    | |      //  | . |  \\
                    | |     ')   |   |   (`
                    | |          ||'||
                    | |          || ||
                    | |          || ||
                    | |          || ||
                    | |         / | | \\
                    """"""""""|_`-' `-' |"""|
                    |"|"""""""\ \       '"|"|
                    | |        \ \        | |
                    : :         \ \       : :  
'''


try:
    print("   *Select your category : ", end='')
    print(", ".join([str(key).capitalize() for key in categories.keys()]) + ', Random')
    ctg = input("\n   [>]  Category ?? ").lower()

    if ctg in categories.keys():
        word = choice(categories[ctg])
    else: 
        if ctg != 'random':
            print(f"\r   Category {ctg} not found ..", end=' ')
            sleep(0.9)
            print("\r   *Selecting random Category... ")
            sleep(1)
        ctg = choice(list(categories.keys()))
        word = choice(categories[ctg])
    word = word.strip().lower()

    backspace()
    initial_time = time()
    
    while True:
        print(f"""
                                               
                          /\  /\ __ _  _ __    __ _         _ __ ___    __ _  _ __  
                         / /_/ // _` || '_ \  / _` | _____ | '_ ` _ \  / _` || '_ \ 
                        / __  /| (_| || | | || (_| ||_____|| | | | | || (_| || | | |
                        \/ /_/  \__,_||_| |_| \__, |       |_| |_| |_| \__,_||_| |_|
                                              |___/                                 

        Lives-Remaining : {7-e_cnt}\n
        """)

        if e_cnt==0:
            draw_hg(fig)
        else:
            draw_hg(eval(f'err{e_cnt}'), err[e_cnt])

        print()
        if used_letters:
            print(f"    Used-Letters : {', '.join(used_letters)}\n")
        draw_letter(word, right_letters)
        
        t = round(time()-initial_time)
        try:
            uc = inputimeout('    [>]  Enter letter ', timeout=total_time-t).lower()
        except:
            game_over(word)

        c=0
        if uc in '0123456789\\/!@#$%^&*()-=+_{}][|?.,<>:;\'"' or len(uc)>1 or uc=='':
            backspace()
            continue

        if uc not in right_letters:
            if uc in word and uc not in right_letters:
                right_letters.append(uc)
            else:
                if uc not in used_letters:
                    used_letters.append(uc)
                    e_cnt+=1

        if e_cnt==7:
            game_over(word)

        if check(word, right_letters):break
        
        backspace()


    if check(word, right_letters) :
        backspace()
        space=' '*15
        print('\n\n'+space+'  +---------')
        print(space+'  |     ')
        print(space+'  |    0')
        print(space+'  |  --|--        (#Hangman-is-free-now) ')
        print(space+'  |   / \\')
        print(space+'  |')
        print(space+"  =======")
        print(f"\n\t  [+]  You have WON the GAME (#Word : {word.upper()})")
        sleep(4)

except KeyboardInterrupt:
    backspace()
    print(ascii_img)
    print('\n  [~]  Exiting Now.... ')
    sleep(3)
    backspace()