# Python3 implementation of Min Heap

import array
import sys
from HeapElement import HeapElement
from Node import Node

class MinHeap:
    def __init__(self):
        self.array = []
        self.size = 0

    def parentIndx(indx):
        return (indx - 1)/2

    def leftChild(indx):
        return(2 * indx) +1

    def rightChild(indx):
        return (2 * indx) +2

    def swap(self,indx1, indx2):
        temp = self.array[indx1]
        self.array[indx1] = self.array[indx2]
        self.array[indx2] = temp

    #add an element to the MinHeap
    def add(self, HeapElement, priority):
        curr = Node(HeapElement, priority)

        #put new node in the array
        self.array.append(curr)
        currIndx = len(self.array)
        parent = array[parentIndx(currIndx)]

        #percolate up
        while curr.priority < parent.priority and currIndx != 0:
            parentIndx = parentIndx(currIndx)
            swap(currIndx, parentIndx)
            currIndx = parentIndx
            parent = array[parentIndx(currIndx)]

        size = size + 1 

   #poll (lowest priority)
    def poll():
        rootVal = array[0]
        array[0] = array[size - 1]
        size = size - 1
        currNodeIndx = 0

       #percolate down
        while(True):
            if leftChild(currNodeIndx) >= size:
                break
            childNodeIndx = -1
            if size == 2:
                childNodeIndx = 1
            elif array[leftChild(currNodeIndx)] != None and array[rightChild(currNodeIndx)] != None and array[leftChild(currNodeIndx)].priority > array[rightChild(currNodeIndx)].priority:
                childNodeIndx = rightChild(currNodeIndx) 
            else:
                childNodeIndx = leftChild(currNodeIndx)

            if array[currNodeIndx].priority < array[childNodeIndx].priority:
                break

            swap(currNodeIndx, childNodeIndx)
            currNodeIndx = childNodeIndx

        return rootVal.value


    def size(self):
        return self.size

    def peek(self):
        if self.array[0] == None:
            return None
        return self.array[0].value

    def printTree(self):
        self.printTree(0,"")

    def printTree(self, index, indent):
        if index >= self.size:
            return
        self.printTree(self.rightChild(index), indent + "    ")
        print(indent + self.array[index].value)
        self.printTree(self.leftChild(index), indent + "    ")



