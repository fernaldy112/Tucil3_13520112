from Puzzle import *
from queue import PriorityQueue

# Melakukan pembacaan file
filename = input("Input file name: ")
f = open("test/" + filename, "r")
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

idx16, total = kurang_i(array)
if (isSolvable(idx16, total)):
    found = False
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
    if found:
        print(len(generated))
        print(currentNode.level)
        print(currentNode.moves)
        # for i in range (len(generated)):
        #     print(generated[i].puzzle)
        #     print(generated[i].moves)
    else:
        print("Not found")
else:
    print("Puzzle tidak dapat diselesaikan")


        


