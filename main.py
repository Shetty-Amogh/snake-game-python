import os

#----------------- variables -------------------
map = [
["P",".","A"],
[".",".","."],
[".",".","L"]
]
mapLen = 3
gameOn = True
snakeX = 0
snakeY = 0
tempX = 0
tempY = 0
arrSnakeX = [0]
arrSnakeY = [0] 
#-------------------functions--------------------
def printMap():
    for y in range(mapLen):
        for x in range(mapLen):
            print(map[y][x], end="")
        print()


def moveSnakePos():
    global arrSnakeX
    global arrSnakeY
    for i in range(len(arrSnakeX),0,-1):
        if i == 1:
            arrSnakeX[i-1] = snakeX
            arrSnakeY[i-1] = snakeY
        elif i == 2:
            map[arrSnakeX[i-1]] = map[arrSnakeX[i-2]]
            map[arrSnakeY[i-1]] = map[arrSnakeY[i-2]]
            arrSnakeX[i-1] = arrSnakeX[i-2]
            arrSnakeY[i-1] = arrSnakeY[i-2]
        else:
            map[arrSnakeX[i-1]] = map[arrSnakeX[i-2]]
            map[arrSnakeY[i-1]] = map[arrSnakeY[i-2]]
            arrSnakeX[i-1] = arrSnakeX[i-2]
            arrSnakeY[i-1] = arrSnakeY[i-2]

def moveSnake():
    for i in range(len(arrSnakeX)):
        if i ==0:
         continue
        else:
         map[arrSnakeX[i+1]] = map[arrSnakeX[i]]

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
            moveSnakePos()
        else :
            temp =  map[snakeY][snakeX + 1]
            map[snakeY][snakeX + 1] =  map[snakeY][snakeX]
            map[snakeY][snakeX] = temp
            snakeX += 1
            moveSnakePos()
    elif inputMove == "s" or inputMove == "S":
        if map[snakeY+1][snakeX] == "A":
            map[snakeY+1][snakeX] = map[snakeY][snakeX]
            snakeY += 1
            arrSnakeX.append(snakeX)
            arrSnakeY.append(snakeY)
            moveSnakePos()
        else :
            temp =  map[snakeY+1][snakeX]
            map[snakeY+1][snakeX] =  map[snakeY][snakeX]
            map[snakeY][snakeX] = temp
            snakeY += 1
            moveSnakePos()
    elif inputMove == "exit":
        break
