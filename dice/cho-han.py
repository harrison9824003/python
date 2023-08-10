"""丁半 Cho-han 共有兩個骰子, 猜測合為基數或偶數"""

import random, sys

JAPANESE_NUMBER = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''丁半骰子遊戲, 在這個日式骰子遊戲中, 會有兩個色子進行遊戲, 玩家須猜測骰子的總合為基數或是偶數''')

# 初始籌碼
purse = 5000
while True:
    print('您好, 現在擁有', purse, '的籌碼, 請開始下注金額, 或是輸入 QUIT 離開遊戲')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('感謝你參與遊戲')
            sys.exit()
        elif not pot.isdecimal():
            print('請輸入數字')
        elif int(pot) > purse:
            print('您剩餘的籌碼', purse, '不足, 請重新輸入')
        else:
            pot = int(pot)
            break
    
    # 取得骰子
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('請輸入你的猜測, CHO 為[偶數], HAN 為[奇數]')
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('請輸入 CHO 或是 HAN')
            continue
        else:
            break
    
    print('骰出的骰子為', JAPANESE_NUMBER[dice1], '-', JAPANESE_NUMBER[dice2])
    print('骰出的骰子為', dice1, '-', dice2)

    rollIsEven = (dice2 + dice1) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet
    if playerWon:
        print('恭喜您贏得賭注', pot)
        purse = purse + pot
        print('荷官收取 10 % 小費')
        purse = purse - (pot // 10)
    else:
        purse = purse - pot
        print('您沒猜中')

    if purse == 0:
        print('您已無籌碼下注了')
        print('感謝你參與遊戲')
        sys.exit()
        


