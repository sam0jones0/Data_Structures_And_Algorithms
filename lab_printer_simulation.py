"""Model of class waiting times for a printer."""

import random

from Queue_my import Queue


class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task is not None

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def new_print_task(num_students):
    avg_tasks_per_sec = 3600 / (num_students * 2)
    if random.randint(1, avg_tasks_per_sec) == avg_tasks_per_sec:
        return True
    else:
        return False


def simulation(num_students, num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task(num_students):
            print_queue.enqueue(Task(current_second))

        if (not print_queue.is_empty()) and (not lab_printer.busy()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    averages.append(average_wait)
    print(
        f"Average Wait {average_wait:6.2f} secs."
        + f"{print_queue.size():3d} tasks remaining."
        + f"{len(waiting_times):4d} tasks completed."
    )


averages = []
for i in range(10):
    # simulation(num_students, num_seconds, pages_per_minute)
    simulation(20, 28_800, 10)
print(f"\nTotal average wait across all simulations {sum(averages) / len(averages):6.2f} secs")


