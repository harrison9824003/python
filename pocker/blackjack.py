import random, sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = 'backside'

def main():
    # 玩家初始金額
    money = 5000
    while True:
        # 檢查金額餘額是否足夠
        if money <=0:
            print('你能使用的金額額度已用完!')
            sys.exit()
        
        # 輸入要下注的金額
        print('現在剩餘金額: {}'.format(money))
        bet = getBet(money)

        # 初始排組
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # 玩家動作
        print('這次下注金額為: {}'.format(bet))
        while True:
            # 顯示目前拿到的牌
            displayHands(playerHand, dealerHand, False)
            print()

            if getHandValue(playerHand) > 21:
                break
        
            move = getMove(playerHand, money - bet)

            # 動作判斷
            # 增注
            if move == 'D':
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('下注增加到 {}'.format(bet))
            # 發牌
            if move in ('H', 'D'):
                newCard = deck.pop()
                rank, suit = newCard
                print('你的牌組為 {} {}'.format(rank, suit))
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21:
                    continue
            # 結束動作
            if move in ('S'):
                break
        
        # 莊家動作        
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('莊家拿牌 ...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
                input('請按下 Enter 繼續 ...')
                print('\n\n')
            
        # 最終結果
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        if dealerValue > 21:
            print('莊家輸了, 你贏得金額: ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('你輸了金額 ${}!'.format(bet))
            money -= bet
        elif playerValue > dealerValue:
            print('你贏了獎金 ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('平手金額將不扣除')
        
        input('請按下 enter 繼續 ...')
        print('\n\n')

# 取得玩家下注金額
def getBet(maxBet):
    while True:
        print('這次要下注金額? (1-{}), 或是輸入 「QUIT」 退出遊戲'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('遊戲結束')
            sys.exit()
        
        if not bet.isdecimal():
            print('金額限定輸入阿拉伯數字')
            continue
        
        bet = int(bet)

        if 1 <= bet <= maxBet:
            return bet
        else:
            print('輸入金額不正確')
            continue

# 取得一副新的52張牌
def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

# 顯示現有的牌
# showDealerHand 是否顯示莊家底牌
def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    # 要顯示莊家底牌
    if showDealerHand:
        print('莊家:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        # 隱藏莊家第一張底牌
        print('莊家: ???')
        displayCards([BACKSIDE] + dealerHand[1:])
    
    print('你的牌: ', getHandValue(playerHand))
    displayCards(playerHand)

# 取得牌組的點數
def getHandValue(cards):
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('J', 'Q', 'K'):
            value += 10
        else:
            value += int(rank)

    # 處理 A, 有剩餘空間多加 10
    value += numberOfAces

    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10

    return value

# 顯示牌組圖案
def displayCards(cards):
    rows = ['', '', '', '', '']
    for i, card in enumerate(cards):
        rows[0] = '___ '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '| # | '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    
    for row in rows:
        print(row)

# 取得玩家動作
def getMove(playerHand, money):
    while True:
        moves = ['(H)it', '(S)tand']

        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in('H','S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move

if __name__ == '__main__':
    main()