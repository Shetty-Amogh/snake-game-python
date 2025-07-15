import os

#----------------- variables -------------------
map = [
["P",".","A"],
[".",".","."],
[".",".","."]
]
mapLen = 3
gameOn = True
snakeX = 0
snakeY = 0
arrSnakeX = [0]
arrSnakeY = [0] 
#-------------------functions--------------------
def printMap():
    for y in range(mapLen):
        for x in range(mapLen):
            print(map[y][x], end="")
        print()


def moveSnake():
    global arrSnakeX
    global arrSnakeY
    for i in range(len(arrSnakeX),0,-1):
        print("to code")

#------------------- main game ------------------

while (gameOn == True):
    printMap()
    inputMove = input("Your move : ")
    print(arrSnakeX)

    #-------------------- move cases -------------
    if inputMove == "d" or inputMove == "D":
        if map[snakeY][snakeX + 1] == "A":
            map[snakeY][snakeX + 1] = map[snakeY][snakeX]
            snakeX += 1
            arrSnakeX.append(snakeX)
            arrSnakeY.append(snakeY)
            moveSnake()
        else :
            temp =  map[snakeY][snakeX + 1]
            map[snakeY][snakeX + 1] =  map[snakeY][snakeX]
            map[snakeY][snakeX] = temp
            snakeX += 1
    elif inputMove == "s" or inputMove == "S":
        if map[snakeY+1][snakeX] == "A":
            map[snakeY+1][snakeX] = map[snakeY][snakeX]
            snakeY += 1
            arrSnakeX.append(snakeX)
            arrSnakeY.append(snakeY)
            moveSnake()
        else :
            temp =  map[snakeY+1][snakeX]
            map[snakeY+1][snakeX] =  map[snakeY][snakeX]
            map[snakeY][snakeX] = temp
            snakeY += 1
    elif inputMove == "exit":
        break
