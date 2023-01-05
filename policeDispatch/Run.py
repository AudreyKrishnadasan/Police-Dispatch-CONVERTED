from MinHeap import MinHeap
from HeapElement import HeapElement

class Run: 

    def main():
        heap = MinHeap()
        nums = [56, 28, 7, 5, 51, 16, 79, 83, 97, 37, 75, 69, 24, 90]
        for x in nums:
            heap.add(HeapElement(x), x)

        heap.printTree()

    if __name__=="__main__":
        main()