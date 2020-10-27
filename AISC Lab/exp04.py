import argparse


class Node:

    #----- Initalize node with pattern gfunction the blanklocation and the move used to reach that state -----#
    def __init__(self, pattern, gfunc, move='start'):
        self.pattern = pattern
        self.gfunc = gfunc
        self.move = move
        for (row, i) in zip(pattern, range(3)):
            if 0 in row:
                self.blankloc = [i, row.index(0)]
                # print(self.blankloc[0],self.blankloc[1])

    #----- equal magic function to check if states are equal or node element by element-----#
    def __eq__(self, other):
        if other == None:
            return False

        if isinstance(other, Node) != True:
            raise TypeError

        for i in range(3):
            for j in range(3):
                if self.pattern[i][j] != other.pattern[i][j]:
                    return False
        return True

    #----- magic function to retrive an element from the node like an array -----#
    def __getitem__(self, key):
        if isinstance(key, tuple) != True:
            raise TypeError
        if len(key) != 2:
            raise KeyError

        return self.pattern[key[0]][key[1]]

    #----- function to calculate hfunction according to given goal -----#
    def calc_hfunc(self, goal):
        self.hfunc = 0
        for i in range(3):
            for j in range(3):
                # print (i,j)
                if self.pattern[i][j] != goal.pattern[i][j]:
                    self.hfunc += 1
        if self.blankloc != goal.blankloc:
            self.hfunc -= 1  # Remove one counter if the blank location is displaced because it overestimates the goal

        self.ffunc = self.hfunc+self.gfunc

        return self.hfunc, self.gfunc, self.ffunc

    #----- Function to move the blank tile left if possible -----#
    def moveleft(self):
        if self.blankloc[1] == 0:
            return None

        left = [[self.pattern[i][j] for j in range(3)]for i in range(3)]
        left[self.blankloc[0]][self.blankloc[1]
                               ] = left[self.blankloc[0]][self.blankloc[1]-1]
        left[self.blankloc[0]][self.blankloc[1]-1] = 0

        return Node(left, self.gfunc+1, 'LEFT')

    #----- Function to move the blank tile right if possible -----#
    def moveright(self):
        if self.blankloc[1] == 2:
            return None

        right = [[self.pattern[i][j] for j in range(3)]for i in range(3)]
        right[self.blankloc[0]][self.blankloc[1]
                                ] = right[self.blankloc[0]][self.blankloc[1]+1]
        right[self.blankloc[0]][self.blankloc[1]+1] = 0

        return Node(right, self.gfunc+1, 'RIGHT')

    #----- Function to move the blank tile up if possible -----#
    def moveup(self):
        if self.blankloc[0] == 0:
            return None

        up = [[self.pattern[i][j] for j in range(3)]for i in range(3)]
        up[self.blankloc[0]][self.blankloc[1]
                             ] = up[self.blankloc[0]-1][self.blankloc[1]]
        up[self.blankloc[0]-1][self.blankloc[1]] = 0

        return Node(up, self.gfunc+1, 'UP')

    #----- Function to move the blank tile down if possible -----#
    def movedown(self):
        if self.blankloc[0] == 2:
            return None

        down = [[self.pattern[i][j] for j in range(3)]for i in range(3)]
        down[self.blankloc[0]][self.blankloc[1]
                               ] = down[self.blankloc[0]+1][self.blankloc[1]]
        down[self.blankloc[0]+1][self.blankloc[1]] = 0

        return Node(down, self.gfunc+1, 'DOWN')

    #----- Function to check and perform all the moves according to possiblity and weather the next move is closed or not -----#
    #----- Close this node and all the new nodes to open list -----#
    def moveall(self, game):
        left = self.moveleft()
        left = None if game.isclosed(left) else left
        right = self.moveright()
        right = None if game.isclosed(right) else right
        up = self.moveup()
        up = None if game.isclosed(up) else up
        down = self.movedown()
        down = None if game.isclosed(down) else down

        game.closeNode(self)
        game.openNode(left)
        game.openNode(right)
        game.openNode(up)
        game.openNode(down)

        return left, right, up, down

    #----- Function to print the array in beautifed format -----#

    def print(self, l2):
        l1 = []
        l1.append(self.move)
        l1.append(self.gfunc)
        l1.append(self.hfunc)
        l1.append(self.pattern[0])
        l1.append(self.pattern[1])
        l1.append(self.pattern[2])
        l2.insert(0, l1)

    def printl(l2):
        for i in range(len(l2)):
            print("(STATE-{},{},f(n) = {})".format(
                l2[i][1], l2[i][0], l2[i][1]+l2[i][2]))
            print(l2[i][3])
            print(l2[i][4])
            print(l2[i][5])
            print("\n")


class Game:

    #---- Initilaize Node with start, goal, a hashtable of open nodes, a hashtable of closed Node and add the start to the open node ----#
    #---- Open nodes is a hash table based on 'f function' and Closed nodes is a hash table based on 'h function' ----#
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.open = {}
        self.closed = {}
        _, _, ffunc = self.start.calc_hfunc(self.goal)
        self.open[ffunc] = [start]

    #---- Function to check weather a node is in closed node or not ----#
    def isclosed(self, node):
        if node == None:  # return True if no node
            return True

        # calculate hfucntion to check in that list of the hash table
        hfunc, _, _ = node.calc_hfunc(self.goal)

        if hfunc in self.closed:
            for x in self.closed[hfunc]:
                if x == node:
                    return True

        return False

    #---- Function to add a node to the closed list and remove it from the open nodes list ----#
    def closeNode(self, node):
        if node == None:  # return back if no node
            return

        hfunc, _, ffunc = node.calc_hfunc(self.goal)
        # remove from the list of the ffunction of the hash table for open nodes
        self.open[ffunc].remove(node)
        if len(self.open[ffunc]) == 0:
            # remove the attribute for a ffunction if its list is empty
            del self.open[ffunc]

        if hfunc in self.closed:
            self.closed[hfunc].append(node)
        else:
            self.closed[hfunc] = [node]

        return

    #---- Function to add a node to the open list after its initilaized ----#
    def openNode(self, node):
        if node == None:
            return

        # Calculate ffucntion to add the node to the list of that ffucntion in hash table
        _, _, ffunc = node.calc_hfunc(self.goal)
        if ffunc in self.open:
            self.open[ffunc].append(node)
        else:
            self.open[ffunc] = [node]

        return

    #---- Function to solve the game using A star algorithm ----#
    def solve(self):

        presentNode = None
        l2 = []
        while(presentNode != self.goal):
            i = 0
            while i not in self.open:
                i += 1  # Check for the list with least 'ffunction' to pick a node from that list
            presentNode = self.open[i][-1]
            # Expand that node for next possible moves
            presentNode.moveall(self)

    #---- Print the solution in reverse direction i.e. from goal to start----#
        while presentNode.move != 'start':
            presentNode.print(l2)
            # do reverse move that what was done to reach the state to backtrack along the solution
            if presentNode.move == 'UP':
                presentNode = presentNode.movedown()
            elif presentNode.move == 'DOWN':
                presentNode = presentNode.moveup()
            elif presentNode.move == 'RIGHT':
                presentNode = presentNode.moveleft()
            elif presentNode.move == 'LEFT':
                presentNode = presentNode.moveright()

            hfunc, _, _ = presentNode.calc_hfunc(self.goal)
            for i in self.closed[hfunc]:
                if i == presentNode:
                    presentNode = i

        Node.printl(l2)
        return


if __name__ == '__main__':
    startrow = [int(i) for i in input(
        "Enter the start state space separated >>>>").split(" ")]
    goalrow = [int(i) for i in input(
        "Enter the goal state space separated >>>>").split(" ")]
    x = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    #----- Assert if Input is correct -----#
    assert set(x) == set(startrow)
    assert set(x) == set(goalrow)

    #----- Reformat Input -----#
    startloc = [startrow[0:3], startrow[3:6], startrow[6:]]
    goalloc = [goalrow[0:3], goalrow[3:6], goalrow[6:]]

    #----- Initalize start and end node -----#
    start = Node(startloc, 0)
    goal = Node(goalloc, 0, 'goal')

    #----- Initilaize Game -----#
    game = Game(start, goal)
    game.solve()  # Solve Game
