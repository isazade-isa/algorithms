# ID 69565964


import random
from dataclasses import dataclass


@dataclass
class Intern:
    __slots__ = ['login', 'tasks', 'penalties']
    login: str
    tasks: int
    penalties: int

    def __gt__(self, other):
        if self.tasks == other.tasks:
            return self.login > other.login if self.penalties == other.penalties else self.penalties > other.penalties
        return self.tasks < other.tasks

    def __lt__(self, other):
        return other > self

    def __repr__(self):
        return self.login


def quick_sort(interns, start, end):
    if start >= end:
        return -1
    left, right = start, end
    pivot = interns[random.randint(start, end)]

    while left <= right:
        while interns[left] < pivot:
            left += 1
        while interns[right] > pivot:
            right -= 1
        if left <= right:
            interns[left], interns[right] = interns[right], interns[left]
            left += 1
            right -= 1

    quick_sort(interns, start=start, end=right)
    quick_sort(interns, start=left, end=end)


if __name__ == '__main__':
    number = int(input())
    arr = []
    for _ in range(number):
        login, tasks, penalties = input().split()
        arr.append(Intern(login, int(tasks), int(penalties)))
    quick_sort(arr, start=0, end=number-1)
    for winner in arr:
        print(winner)
