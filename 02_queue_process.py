import time

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items[0]

def process_tasks(task_list):
    queue = Queue()
    current_time = 0

    for task in task_list:
        queue.enqueue(task)

    print("Начало обработки задач...")

    while not queue.is_empty():
        task = queue.dequeue()
        task_name, duration = task

        print(f"'{task_name}' начата в момент времени {current_time}")
        current_time += duration
        print(f"'{task_name}' завершена в момент времени {current_time}")

    print("Все задачи обработаны!")

tasks = [
    ("Задача 1", 3),
    ("Задача 2", 2),
    ("Задача 3", 5),
    ("Задача 4", 1),
]

process_tasks(tasks)