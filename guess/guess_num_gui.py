#code:utf-8
import random
import tkinter as tk
import tkinter.messagebox as tmsg

# 常數
NUM_DIGITS = 3
MAX_GUESSES = 10
NONE_STRING = '沒有一個數字有猜中!'
SUCCESS_STRING = '恭喜, 你猜對了!'
NUM_GUESSES = 0
SECRET_NUM = ''
END_LINE = '\n------\n'

# functions
def buttonClick():
    if not checkGuessNum():
        showMaxGuessMessage()
        return None
    guess = inputEditBox.get()
    result = getClues(guess, SECRET_NUM)
    rirekiBox.insert(tk.END, result + END_LINE)
    if result == SUCCESS_STRING:
        showMaxGuessMessage()

# 建立隨機數字
def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    # print(secretNum)
    return secretNum

# 檢查猜測的數字
def getClues(guess, secretNum):
    if guess == secretNum:
        return SUCCESS_STRING
    
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
        return NONE_STRING
    else:
        clues.sort()
        clues.insert(0, '你已經猜測 {} 次:'.format(NUM_GUESSES))
        return '\n'.join(clues)

# 檢查目前猜測次數
def checkGuessNum():
    global NUM_GUESSES
    if NUM_GUESSES >= MAX_GUESSES:
        return False
    NUM_GUESSES += 1
    return True

# 猜測次數已達上限
def showMaxGuessMessage():
    global SECRET_NUM

    result = tmsg.askyesno(title = '猜數字的次數已達到上限!', 
        message = '公佈答案答案是 {}, 有想要再進行一次遊戲?'.format(SECRET_NUM)
    )

    if not result:
        root.destroy()
    else:
        initGame()

# 建立視窗物件給予 root 變數
root = tk.Tk()

# 視窗長寬
root.geometry('600x400')

# 視窗 title
root.title('猜數字遊戲')

# label
inputTitleLabel = tk.Label(root, text = '請輸入3位數字', font = ("Helvetica", 14))
inputTitleLabel.place(x = 20, y = 20)

# 輸入框
inputEditBox = tk.Entry(width = 5, font = ("Helvetica", 28))
inputEditBox.place(x = 20, y = 60)

# 輸入按鈕
inputButton = tk.Button(
        root, text = '確認', 
        font = ("Helvetica", 14), 
        command = buttonClick
    )
inputButton.place(x = 160, y = 60)

# 顯示文字框
rirekiBox = tk.Text(root, font = ("Helvetica", 14))
rirekiBox.place(x = 300, y = 0, width = 300, height = 400)

# 初始
def initGame():
    global NUM_GUESSES,SECRET_NUM
    # 猜測次數歸 0
    NUM_GUESSES = 0
    # 重新取號碼
    SECRET_NUM = getSecretNum()
    # 清空輸入框和文字框
    rirekiBox.delete('1.0', 'end')
    inputEditBox.delete(0, 'end')

# init
initGame()

# 顯示視窗
root.mainloop()