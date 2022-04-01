from Puzzle import *
from queue import PriorityQueue
import time

def readFile():
    # Melakukan pembacaan file
    filename = input("\nInput file name: ")
    f = open("../test/" + filename, "r")
    lines = f.read()
    array = []
    temp = ""
    for text in lines:
        if (text != ' ' and text != '\n'):
            temp += text
        else:
            array.append(int(temp))
            temp = ""
    array.append(int(temp))
    return array

def solve(array):
    # Menyelesaikan puzzle
    idx16, total = kurang_i(array)
    found = False
    if (isSolvable(idx16, total)):
        generated = []
        q = PriorityQueue()
        newNode = Node(array, 0, ["initial"])
        solution = [i+1 for i in range(16)]
        generated.append(newNode)
        q.put((newNode.countCost(), len(generated), newNode))
        while not(q.empty()) and not(found):
            currentNode = q.get()[2]
            if (currentNode.puzzle == solution):
                found = True
            else:
                newArrays, newMoves = generate(currentNode, generated)
                i = 0
                for newArray in newArrays:
                    newNode = Node(newArray, currentNode.level + 1, currentNode.moves + [newMoves[i]])
                    generated.append(newNode)
                    q.put((newNode.countCost(), len(generated), newNode))
                    i += 1
        return currentNode, found, len(generated)
    else:
        dummyNode = Node(array, 0, ["initial"])
        return dummyNode, found, 0

if __name__ == '__main__':
    array = readFile()
    start = time.time()
    resultNode, solved, n = solve(array)
    end = time.time()
    if solved:
        tempArray = [array[i] for i in range(16)]
        print()
        for i in range(len(resultNode.moves)):
            print("Move: " + resultNode.moves[i])
            print()
            tempArray = action(tempArray, resultNode.moves[i])
            display(tempArray)
        print("Waktu Eksekusi Program: " + str(end-start))
        print("Jumlah simpul yang dibangkitkan: " + str(n))
        print()
    else:
        print("\nInitial matrix:")
        display(array)
        print("Puzzle tidak dapat diselesaikan\n")
    


        


