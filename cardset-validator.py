
from constraint import *

problem = Problem()

cardSet = [[None for n in range(15)] for card in range(8)]

oCellIndex = [
    [0,0],[0,2],[0,8],[0,10],[0,12],[0,13],
    [1,0],[1,2],[1,10],[1,12],
    [2,0],[2,2],[2,4],[2,5],[2,7],[2,10],
    [3,0],[3,4],[3,5],[3,7],
    [4,0],[4,2],[4,5],[4,6],
    [5,0],[5,2],[5,6],[5,7],
    [6,8],[6,9],[6,10],[6,12],
    [7,8],[7,9],[7,10],[7,12],
        ]
#vars named: letter for shape, number for card and position
openCells = [
    'a0','a2','a8','a10','a12','a13',
    'b0','b2','b10','b12',
    'c0','c2','c4','c5','c7','c10',
    'd0','d4','d5','d7',
    'e0', 'e2', 'e5', 'e6',
    'f0', 'f2', 'f6', 'f7',
    'g8', 'g9', 'g10', 'g12',
    'h8', 'h9', 'h10', 'h12',
]
for x in range(0,len(oCellIndex)):
    cell = oCellIndex[x]
    cardSet[cell[0]][cell[1]] = openCells[x]

# distribute one-off shapes as seed (fixedVars)
"""#colors 1:orange, 2:red, 3:green, 4:blue, 5:teal, 6:purple

cardSet[7][2] = 1    #h2
cardSet[4][4] = 2    #e4
cardSet[6][6] = 3    #g6
cardSet[1][8] = 4    #b8
cardSet[5][10]= 5    #f10
cardSet[3][12]= 6    #d12

# declare missing shapes
cardSet[1][14] = 6   #b14
cardSet[3][14] = 4   #d14
cardSet[4][14] = 3   #e14
cardSet[5][14] = 1   #f14
cardSet[6][14] = 2   #g14
cardSet[7][14] = 5   #h14
"""



seedVars = ['d12', 'f10', 'b8', 'g6', 'e4', 'h2',]
problem.addVariable('h2',range(1,2))
problem.addVariable('e4',range(2,3))
problem.addVariable('g6',range(3,4))
problem.addVariable('b8',range(4,5))
problem.addVariable('f10',range(5,6))
problem.addVariable('d12',range(6,7))

fixedVars = seedVars + ['h14', 'g14', 'f14', 'e14', 'd14', 'b14']
problem.addVariable('b14',range(6,7))
problem.addVariable('d14',range(4,5))
problem.addVariable('e14',range(3,4))
problem.addVariable('f14',range(1,2))
problem.addVariable('g14',range(2,3))
problem.addVariable('h14',range(5,6))


#set of unpaired cells: 'c2' 'e5' 'f7' 'a8' 'c10' 'a13'
orphans = frozenset(['c2', 'e5', 'f7', 'a8', 'c10', 'a13'])


#cards are collections of every two coloumns
cards = []
for y in range(7):
    card = []
    for x in range(8):
        if cardSet[x][y*2] != None:
            card.append(cardSet[x][y*2])
        if cardSet[x][y*2+1] != None:
            card.append(cardSet[x][y*2+1])
    for seed in seedVars:

        if int(seed[1:]) == y+1 or int(seed[1:]) :
            card.append(seed)
    #print(card)
    if len(card) >0:
        s = frozenset(card)
    cards.append(card)


# paired cells are consecutive [even, odd] pairs in a card
pairedCells = []
#for card in cards:
 #   print(card)
    #for y in range(3):
     #   if int(card[y*2][1:]) +1 == int(card[y*2+1][1:]):
      #      print(card[y],card[y+1])
        #if card[4*2] !=
 #       print(card[y], card[y][1:])


#initializing constraint variables
for x in cardSet:
    for y in x:
        if y != None and y not in fixedVars:
            problem.addVariable(y, range(1,7))

#orphans should be one of each
problem.addConstraint(AllDifferentConstraint(), orphans)

# rows may not have duplicate values
for x in cardSet:
    lineType = []
    for y in x:
        if y != None:
            lineType.append(y)
    if len(lineType) > 0:
        s = frozenset(lineType)
    problem.addConstraint(AllDifferentConstraint(),s)


#cards may not have duplicate values
for card in cards:
    problem.addConstraint(AllDifferentConstraint(), card)

#print(cardSet[7][4])

#TODO:  impliment constraint on paired cells (first produce list of pairs

solution = problem.getSolution()

#print(solution)

#for key in solution:
#    print(key, solution[key])

def printSet():
    for line in cardSet:
        pLine = []
        for item in line:
            if item in solution:
                pLine.append(str(solution[item])+" ")
            elif item == None:
                pLine.append(None)
            else:
                pLine.append(str(item)+" ")
        print(pLine)

printSet()

