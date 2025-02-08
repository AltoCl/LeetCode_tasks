# Design a number container system that can do the following:
#
# Insert or Replace a number at the given index in the system.
# Return the smallest index for the given number in the system.
# Implement the NumberContainers class:
#
# NumberContainers() Initializes the number container system.
# void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
# int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.

import heapq

class NumberContainers:
    def __init__(self):
        self.index_val = {}
        self.res = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_val:
            prevNum = self.index_val[index]
            if prevNum == number:
                return
            self.res[prevNum].discard(index)

        if number not in self.res:
            self.res[number] = set()
        self.res[number].add(index)
        self.index_val[index] = number

    def find(self, number: int) -> int:
        if number not in self.res or not self.res[number]:
            return -1
        return min(self.res[number])