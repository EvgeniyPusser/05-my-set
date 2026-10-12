from collections import deque


class MyStackInt:
    def __init__(self):
        self._stack = deque()

    def push(self, num):
        if not self._stack:
            current_max = num
        else:
            current_max = max(num, self._stack[-1][1])

        self._stack.append((num, current_max))

    def pop(self):
        if not self._stack:
            raise IndexError("pop from empty stack")

        return self._stack.pop()[0]

    def max(self):
        if not self._stack:
            raise IndexError("max from empty stack")

        return self._stack[-1][1]

