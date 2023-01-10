# Python3 implementation of Min Heap
import sys
from HeapElement import HeapElement
from Node import Node

class MinHeap:
    def __init__(self):
        self.array = []
        self.size = 0

    def parentFind(self, indx):
        return int((indx - 1)/2)

    def leftChild(self, indx):
        return int((2 * indx) +1)

    def rightChild(self, indx):
        return int((2 * indx) +2)

    def swap(self,indx1, indx2):
        temp = self.array[indx1]
        self.array[indx1] = self.array[indx2]
        self.array[indx2] = temp

    #add an element to the MinHeap
    def add(self, HeapElement, priority):
        curr = Node(HeapElement, priority)
        
        #put new node in the array
        self.array.append(curr)
        currIndx = self.size 
        parentNode = self.array[self.parentFind(currIndx)]
        

        #percolate up
        while currIndx != 0 and curr.priority < parentNode.priority:
            parentIndx = self.parentFind(currIndx)
            self.swap(currIndx, parentIndx)
            currIndx = parentIndx
            parentNode = self.array[self.parentFind(currIndx)]

        self.size = self.size + 1 

   #poll (lowest priority)
    def poll(self):
        rootVal = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.array.pop(self.size - 1) 
        self.size = self.size - 1
        currNodeIndx = 0

       #percolate down
        while(True):
            if self.leftChild(currNodeIndx) >= self.size:
                break
            childNodeIndx = -1
            if self.size == 2:
                childNodeIndx = 1
            elif (not self.rightChild(currNodeIndx) >= self.size) and self.array[self.leftChild(currNodeIndx)].priority > self.array[self.rightChild(currNodeIndx)].priority:
                childNodeIndx = self.rightChild(currNodeIndx) 
            else:
                childNodeIndx = self.leftChild(currNodeIndx)

            if self.array[currNodeIndx].priority < self.array[childNodeIndx].priority:
                break

            self.swap(currNodeIndx, childNodeIndx)
            currNodeIndx = childNodeIndx

        return rootVal


    def size(self):
        return self.size

    def peek(self):
        if not(self.array):
            return None
        return self.array[0].value

    def printTree(self, index, indent):
        if index >= self.size:
            return
        self.printTree(self.rightChild(index), indent + "    ")
        print(indent, self.array[index].value.value)
        self.printTree(self.leftChild(index), indent + "    ")
    
    def printArray(self):
        if self.size == 0:
            print("{}")
        result = "{" #+ str(self.array[0].value.value)
        
        for x in self.array:
            result += ", " + str(x.value.value)
            
        print(result + "}")
