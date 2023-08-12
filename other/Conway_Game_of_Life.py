# 規則
# 1.當細胞為存活狀態, 他身邊有 2 或 3 個活細胞, 則保持存活狀態
# 2.當細胞為死亡狀態, 他身邊有 3 個活細胞, 則變成存活狀態
# 3.其餘條件都會變成死亡細胞或保持死亡
import copy, random, sys, time

# 設定寬高
WIDTH = 79
HEIGHT = 20

ALIVE = '0'
DEAD = ' '

nextCells = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE
        else:
            nextCells[(x, y)] = DEAD


while True:

    print('\n' * 50)
    cells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')
        print()
    print('按下 Ctrl-C 離開')

    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1
            if cells[(x, above)] == ALIVE:
                numNeighbors +=1
            if cells[(right, above)] == ALIVE:
                numNeighbors +=1
            if cells[(left, y)] == ALIVE:
                numNeighbors +=1
            if cells[(right, y)] == ALIVE:
                numNeighbors +=1
            if cells[(left, below)] == ALIVE:
                numNeighbors +=1
            if cells[(x, below)] == ALIVE:
                numNeighbors +=1
            if cells[(right, below)] == ALIVE:
                numNeighbors +=1

            if cells[(x, y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and (numNeighbors == 3):
                nextCells[(x, y)] = ALIVE
            else:
                nextCells[(x, y)] = DEAD
    
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()
