#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools
def evaluate(playArea):

    for row in playArea:
        if row.count(row[0]) == len(row) and row[0] != '_':
            return 10 if row[0] == 'x' else -10

    for col in range(len(playArea[0])):
        check = [row[col] for row in playArea]
        if check.count(check[0]) == len(check) and check[0] != '_':
            return 10 if check[0] == 'x' else -10

    if playArea[0][0] == playArea[1][1] == playArea[2][2] and playArea[0][0] != '_':
        return 10 if playArea[0][0] == 'x' else -10
    if playArea[0][2] == playArea[1][1] == playArea[2][0] and playArea[0][2] != '_':
        return 10 if playArea[0][2] == 'x' else -10

    
    return 0

def isMovesLeft(playArea):
    return any("_" in row for row in playArea)

def minmax(playArea, depth, isMax, alpha, beta):
    score = evaluate(playArea)

    if score == 10:
        return score

    if score == -10:
        return score
    
    if isMovesLeft(playArea) == False:
        return 0

    if isMax:
        optimal = -1000
        for i in range(3):
            for j in range(3):
                if playArea[i][j] == '_':
                    playArea[i][j] = 'x'
                    optimal = max(optimal, minmax(playArea, depth + 1, not isMax, alpha, beta))
                    playArea[i][j] = '_'
                    alpha = max(alpha, optimal)
                    if beta <= alpha:
                        break
    else:  
        optimal = 1000
        for i in range(3):
            for j in range(3):
                if playArea[i][j] == '_':
                    playArea[i][j] = 'o'
                    optimal = min(optimal, minmax(playArea, depth + 1, not isMax, alpha, beta))
                    playArea[i][j] = '_'
                    beta = min(beta, optimal)
                    if beta <= alpha:
                        break

    return optimal



def printplayArea(playArea):
    for row in playArea:
        print(row)

def takeMove(playArea, player):
    if player == 'o':
        print("Player's turn")
        while True:
            row = int(input("Enter the row number (0, 1, 2): "))
            col = int(input("Enter the column number (0, 1, 2): "))
            if playArea[row][col] == '_':
                playArea[row][col] = player
                break
            else:
                print("Invalid move. Try again.")
    else: 
        AgentMoves(playArea, player)


def AgentMoves(playArea, player):
    print("Agent's Move:")
    optimalVal = -1000
    optimalMove = (-1, -1)

    for i, j in itertools.product(range(3), range(3)):
        if playArea[i][j] == '_':
            playArea[i][j] = player
            moveVal = minmax(playArea, 0, False, float('-inf'), float('inf'))
            playArea[i][j] = '_'
            if moveVal > optimalVal:
                optimalMove = (i, j)
                optimalVal = moveVal

    print(f"Agent is moved at {optimalMove[0]}, {optimalMove[1]}")
    playArea[optimalMove[0]][optimalMove[1]] = player

def isGameOver(playArea):
    score = evaluate(playArea)
    return True if score in [10, -10] else isMovesLeft(playArea) == False

playArea = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

while True:
    takeMove(playArea, 'o')
    printplayArea(playArea)
    if isGameOver(playArea):
        print("Player wins!" if evaluate(playArea) == -10 else "It's a draw!")
        break

    
    takeMove(playArea, 'x')
    printplayArea(playArea)
    if isGameOver(playArea):
        print("AI wins!" if evaluate(playArea) == 10 else "It's a draw!")
        break


# In[ ]:





# In[ ]:




