#code:utf-8
import random
import tkinter as tk
import tkinter.messagebox as tmsg

class guessClass:
    # 數字長度
    NUM_DIGITS = 3
    # 最多猜測數字
    MAX_GUESSES = 10
    NONE_STRING = '沒有一個數字有猜中!'
    SUCCESS_STRING = '恭喜, 你猜對了!'
    # 當下已猜測次數
    NUM_GUESSES = 0
    # 答案
    SECRET_NUM = ''
    # 換行
    END_LINE = '\n------\n'

    # functions
    def buttonClick(self):
        if not self.checkGuessNum():
            self.showMaxGuessMessage()
            return None
        guess = inputEditBox.get()
        result = self.getClues(guess, self.SECRET_NUM)
        rirekiBox.insert(tk.END, result + self.END_LINE)
        if result == self.SUCCESS_STRING:
            self.showMaxGuessMessage()

    # 建立隨機數字
    def getSecretNum(self):
        numbers = list('0123456789')
        random.shuffle(numbers)

        secretNum = ''
        for i in range(self.NUM_DIGITS):
            secretNum += str(numbers[i])
        return secretNum

    # 檢查猜測的數字
    def getClues(self, guess, secretNum):
        if guess == secretNum:
            return self.SUCCESS_STRING
        
        clues = []    
        for i in range(len(guess)):        
            if guess[i] == secretNum[i]:
                clues.append('#{}數字{} Hit'.format(int(i)+1, guess[i]))
            elif guess[i] in secretNum:
                # 檢查有正確數字, 但位置不正確
                # 要排除當前位置與匹配到的位置(兩種)有 Hit 情況
                # i 為檢查猜測的位置
                # j 為遍例 secretNum 所有數字
                for j in range(self.NUM_DIGITS):
                    if (guess[i] == secretNum[j]) and (guess[j] != secretNum[j]) and (guess[i] != secretNum[i]):
                        clues.append('#{}數字{} Blow'.format(int(i)+1, guess[i]))
                        break
            
        if len(clues) == 0:
            return self.NONE_STRING
        else:
            clues.sort()
            clues.insert(0, '你已經猜測 {} 次:'.format(self.NUM_GUESSES))
            return '\n'.join(clues)

    # 檢查目前猜測次數
    def checkGuessNum(self):
        if self.NUM_GUESSES >= self.MAX_GUESSES:
            return False
        self.NUM_GUESSES += 1
        return True

    # 猜測次數已達上限
    def showMaxGuessMessage(self):

        result = tmsg.askyesno(title = '猜數字的次數已達到上限!', 
            message = '公佈答案答案是 {}, 有想要再進行一次遊戲?'.format(self.SECRET_NUM)
        )

        if not result:
            root.destroy()
        else:
            self.initGame()
    
    # 初始
    def initGame(self):
        # 猜測次數歸 0
        self.NUM_GUESSES = 0
        # 重新取號碼
        self.SECRET_NUM = self.getSecretNum()
        # 清空輸入框和文字框
        rirekiBox.delete('1.0', 'end')
        inputEditBox.delete(0, 'end')

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

guessObj = guessClass()
# 輸入按鈕
inputButton = tk.Button(
        root, text = '確認', 
        font = ("Helvetica", 14), 
        command = guessObj.buttonClick
    )
inputButton.place(x = 160, y = 60)

# 顯示文字框
rirekiBox = tk.Text(root, font = ("Helvetica", 14))
rirekiBox.place(x = 300, y = 0, width = 300, height = 400)

# init
guessObj.initGame()

# 顯示視窗
root.mainloop()