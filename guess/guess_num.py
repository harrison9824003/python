# Write your code here :-)
import random

NUM_DIGITS = 3
MAX_GUESSES = 10
NONE_STR = '沒有一個數字有猜中!'

def main():
    print('''
    猜數字遊戲!
    這裡總共有 {} 位數字,
    請輸入一組對應數字,
    若輸入的數字中:
        1. 輸入數字中有對的數字且位置也正確會顯示 「#[第幾位][數字]" Hit」
        2. 輸入數字中有隊的數字但位置不正確會顯示 「#[第幾位][數字] Blow」(有可能會重複出現提示)
        3. 沒有任何數字猜對會顯示 「{}」 
    當答對或是次數用完時遊戲會結束, 
    並詢問是否進行下一輪'''.format(NUM_DIGITS, NONE_STR))

    while True:
        secretNum = getSecretNum()
        print('已設定好一組隨機 {} 位數字'.format(NUM_DIGITS))
        print('你可以有 {} 次來猜數字的機會, 遊戲開始!'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('猜數字的次數已達到上限!')
                print('公佈答案答案是 {}'.format(secretNum))

        print('有想要再進行一次遊戲? (y or n)')
        if not input('> ').lower().startswith('y'):
            break
    print('謝謝你, 遊戲結束!')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    print(secretNum)
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return '恭喜, 你猜對了!'
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('#{}數字{} Hit'.format(int(i)+1, guess[i]))
        elif guess[i] in secretNum:
            # 檢查有正確數字, 但位置不正確
            # 要排除當前位置與匹配到的位置(兩種)有 Hit 情況
            # i 為檢查猜測的位置
            # j 為遍例 secretNum 所有數字
            for j in range(NUM_DIGITS):
                if (guess[i] == secretNum[j]) and (guess[j] != secretNum[j]) and (guess[i] != secretNum[i]):
                    clues.append('#{}數字{} Blow'.format(int(i)+1, guess[i]))
                    break
        
    if len(clues) == 0:
        return NONE_STR
    else:
        clues.sort()
        return '\n'.join(clues)

if __name__ == '__main__':
    main()
