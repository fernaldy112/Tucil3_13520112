from Node import Node

def kurang_i(array):
    # Menghitung Kurang(i)
    kurangi = [0 for i in range(16)]
    total = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                kurangi[array[i]-1] += 1
                total += 1
        if array[i] == 16:
            idx16 = i
    print("\nKurang(i):")
    for i in range(len(kurangi)):
        if (i < 9):
            print(' ', end='')
        print(i+1, kurangi[i])
    return idx16, total

def isSolvable(idx16, total):
    # Menentukan apakah puzzle bisa diselesaikan
    x = 0
    if (idx16 == 1 or idx16 == 3 or idx16 == 4 or idx16 == 6 or idx16 == 9 or idx16 == 11 or idx16 == 12 or idx16 == 14):
        x = 1
    print("\nsum(Kurang(i)) + X = " + str(total + x))
    return (total + x)%2 == 0

def isMoveableLeft(array):
    idx = array.index(16)
    prohibited = [0, 4, 8, 12]
    return not (idx in prohibited)

def isMoveableRight(array):
    idx = array.index(16)
    prohibited = [3, 7, 11, 15]
    return not (idx in prohibited)

def isMoveableUp(array):
    idx = array.index(16)
    prohibited = [0, 1, 2, 3]
    return not (idx in prohibited)

def isMoveableDown(array):
    idx = array.index(16)
    prohibited = [12, 13, 14, 15]
    return not (idx in prohibited)

def moveLeft(array):
    idx = array.index(16)
    newArray = [array[i] for i in range(16)]
    temp = newArray[idx-1]
    newArray[idx-1] = newArray[idx]
    newArray[idx] = temp
    return newArray

def moveRight(array):
    idx = array.index(16)
    newArray = [array[i] for i in range(16)]
    temp = newArray[idx+1]
    newArray[idx+1] = newArray[idx]
    newArray[idx] = temp
    return newArray

def moveUp(array):
    idx = array.index(16)
    newArray = [array[i] for i in range(16)]
    temp = newArray[idx-4]
    newArray[idx-4] = newArray[idx]
    newArray[idx] = temp
    return newArray

def moveDown(array):
    idx = array.index(16)
    newArray = [array[i] for i in range(16)]
    temp = newArray[idx+4]
    newArray[idx+4] = newArray[idx]
    newArray[idx] = temp
    return newArray

def isEverGenerated(newArray, generated):
    found = False
    i = 0
    while (i < len(generated) and not found):
        if (generated[i].puzzle == newArray):
            found = True
        else:
            i += 1
    return found

def generate(node, generated):
    lastmove = node.moves[len(node.moves)-1]
    newArrays = []
    newMoves = []
    if (isMoveableUp(node.puzzle) and lastmove != "down"):
        newArray = moveUp(node.puzzle)
        if not isEverGenerated(newArray, generated):
            newArrays.append(newArray)
            newMoves.append("up")
    if (isMoveableRight(node.puzzle) and lastmove != "left"):
        newArray = moveRight(node.puzzle)
        if not isEverGenerated(newArray, generated):
            newArrays.append(newArray)
            newMoves.append("right")
    if (isMoveableDown(node.puzzle) and lastmove != "up"):
        newArray = moveDown(node.puzzle)
        if not isEverGenerated(newArray, generated):
            newArrays.append(newArray)
            newMoves.append("down")
    if (isMoveableLeft(node.puzzle) and lastmove != "right"):
        newArray = moveLeft(node.puzzle)
        if not isEverGenerated(newArray, generated):
            newArrays.append(newArray)
            newMoves.append("left")
    return newArrays, newMoves

def action(array, direction):
    if (direction == "initial"):
        return array
    elif (direction == "left"):
        return moveLeft(array)
    elif (direction == "right"):
        return moveRight(array)
    elif (direction == "up"):
        return moveUp(array)
    elif (direction == "down"):
        return moveDown(array)

def display(array):
    for i in range(4):
        for j in range(4):
            if (array[i*4+j] == 16):
                print("  ", end = ' ')
            elif (array[i*4+j] < 10):
                print(" " + str(array[i*4+j]), end = ' ')
            else:
                print(str(array[i*4+j]), end = ' ')
        print()
    print()
    