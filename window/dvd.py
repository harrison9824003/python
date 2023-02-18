import sys, random, time

try:
    import bext
except ImportError:
    print('目前環境不支援 bext')
    sys.exit

# 取目前視窗寬高
WIDTH, HEIGHT = bext.size()

# 寬度減 1
WIDTH -= 1

NUMBER_OF_LOGOS = 1
PAUSE_AMOUNT = 0.2
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_LEFT, DOWN_RIGHT)

COLOR = 'color'
X = 'x'
Y = 'Y'
DIR = 'direction'

def main():
    bext.clear()

    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({
            COLOR: random.choice(COLORS),
            X: random.randint(1, WIDTH - 4),
            Y: random.randint(1, HEIGHT - 4),
            DIR: random.choice(DIRECTIONS)
        })
    
    cornerBounces = 0
    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print('   ', end = '')

            # 原本文字狀態
            originalDirection = logo[DIR]

            # TODO: 計算位置改成 <= 非 ==
            # TODO: 右側位置計算翻轉判斷, 目前空格三個
            # 文字到達左側上下角落位置
            if logo[X] <= 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] <= 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            # 文字到達右側上下
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1
            # 文字到達左側位置
            elif logo[X] <= 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] <= 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT
            # 文字到達右測位置
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT
            # 文字到達上方位置
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT
            # 文字到達下方位置
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT
            
            # 判斷方向是否相同替換顏色
            if logo[DIR] != originalDirection:
                logo[COLOR] = random.choice(COLORS)
            
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1
            
            bext.goto(5, 0)
            bext.fg('white')
            print('Corner bounces:', cornerBounces, end='')

            for logo in logos:
                bext.goto(logo[X], logo[Y])
                bext.fg(logo[COLOR])
                print('DVD', end='')
            
            bext.goto(0, 0)

            sys.stdout.flush()
            time.sleep(PAUSE_AMOUNT)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit