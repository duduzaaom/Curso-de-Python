class Task:
    id_count = 0

    def __init__(self, description: str, programmer: str, workload: int):
        Task.id_count += 1

        self.id = Task.id_count
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.task_completed = False

    def is_finished(self):
        return self.task_completed
    
    def mark_finished(self):
        self.task_completed = True

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {"FINISHED" if self.task_completed else "NOT FINISHED"}"
    

class OrderBook:
    def __init__(self):
        self._orders = []
        self._programmers = set()

    def add_order(self, description, programmer, workload):
        self._orders.append(Task(description, programmer, workload))
        self._programmers.add(programmer)

    def all_orders(self):
        return self._orders
    
    def programmers(self):
        return list(self._programmers)
    
    def mark_finished(self, id: int):
        for task in self._orders:
            if task.id == id:
                task.mark_finished()
                return
            
        raise ValueError("There is no task with the given id.")
    
    def finished_orders(self):
        return [task for task in self._orders if task.is_finished()]
    
    def unfinished_orders(self):
        return [task for task in self._orders if not task.is_finished()]
    
    def status_of_programmer(self, programmer: str):
        finished_amount = 0
        unfinished_amount = 0

        finished_time = 0
        unfinished_time = 0

        if programmer in self.programmers():
            for task in self.all_orders():
                if task.programmer == programmer:
                    if task.is_finished():
                        finished_amount += 1
                        finished_time += task.workload
                    else:
                        unfinished_amount += 1
                        unfinished_time += task.workload

            return finished_amount, unfinished_amount, finished_time, unfinished_time
        
        raise ValueError("There is no programmer with this name.")
                    

class OrderBookApplication:
    def __init__(self):
        self.orderbook = OrderBook()

    def add_order(self):
        description = input("description: ")
        programmer_workload = input("programmer and workload estimate: ")

        programmer = programmer_workload.split()[0]
        workload = int(programmer_workload.split()[1])

        self.orderbook.add_order(description, programmer, workload)

        print("added!")

    def execute(self):
        print("commands:")
        print("0 exit\n1 add order\n2 list finished tasks\n3 list unfinished tasks\n4 mark task as finished\n5 programmers\n6 status of programmer\n")

        while True:
            command = int(input("command: "))

            if command == 0:
                break
            elif command == 1:
                self.add_order()
            elif command == 2:
                pass
                



if __name__ == "__main__":
    program = OrderBookApplication()
    # program.execute()
    program.add_order()

    for task in program.orderbook.all_orders():
        print(task)
