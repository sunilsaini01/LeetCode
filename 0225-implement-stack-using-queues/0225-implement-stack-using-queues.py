from collections import deque

class MyStack(object):

    def __init__(self):
        self.input_queue = deque()
        self.output_queue = deque()

    def push(self, x):
        self.output_queue.append(x)

        while self.input_queue:
            self.output_queue.append(
                self.input_queue.popleft()
            )

        self.input_queue, self.output_queue = (
            self.output_queue,
            self.input_queue
        )

    def pop(self):
        return self.input_queue.popleft()

    def top(self):
        return self.input_queue[0]

    def empty(self):
        return not self.input_queue