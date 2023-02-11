import datetime,random
# 生日悖論
# 建立所有 birthday
def getbirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYead = datetime.date(2022, 1, 1)

        # 取得隨機日期差
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364)) 
        birthday = startOfYead + randomNumberOfDays
        birthdays.append(birthday)
    
    return birthdays

# 檢查生日是否有重複
def getMatch(birthdays):
    # 所有生日不重複
    if len(birthdays) == len(set(birthdays)):
        return None
    
    for i, birthdayA in enumerate(birthdays):
        for j, birthdayB in enumerate(birthdays[i + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA

# 月份文字轉換
MONTHS = ('一月', '二月', '三月', '四月', '五月', '六月', '七月',
            '八月', '九月', '十月', '十一月', '十二月')

while True:
        print('請輸入你要幾個生日?(最多 100 個)')
        response = input('> ')
        if response.isdecimal() and (0 < int(response) <= 100):
            numBirthday = int(response)
            break
print()

print('你輸入的數字為', numBirthday)
birthdays = getbirthdays(numBirthday)
for i,birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

match = getMatch(birthdays)

# 顯示結果
if match != None:
    monthName = MONTHS[match.month -1]
    dateText = '{} {}'.format(monthName, match.day)
    print('有許多人的生日為', dateText)
else:
    print('沒有生日有重複')
print()

print('隨機產生', numBirthday, ' 100,000 次')
input('按下 enter 繼續...')

simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, '開始...')
    birthdays = getbirthdays(numBirthday)
    if(getMatch(birthdays)) != None:
        simMatch = simMatch + 1
print('100,000 完成')

probability = round(simMatch / 100_000 * 100, 2)
print('執行 100,000 次取', numBirthday, '個生日比對是否重複')
print('總共有', simMatch, '次重複')
print('有重複次數為', simMatch)
print('判斷重複比例為', probability, '%')
