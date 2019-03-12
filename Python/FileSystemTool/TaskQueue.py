from inspect import isfunction


class TaskQueue:
    def __init__(self):
        self.task_queue = []

    def add_task(self, task):
        assert isfunction(task)
        self.task_queue.append(task)
