import time


# Node and ImprovedQueue class from Chapter 24, 26.
class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            # If list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # Find the last node
            last = self.last
            # Append the new node
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo


# ----------------------------------------------------------------------------------------------------------------------

# Ex 26.1

class QueueList:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        first_item = self.items[0]
        del self.items[0]
        return first_item


# Test
queue = QueueList()
queue.insert("Mark")
queue.insert("John")
queue.insert("Tom")
print(queue)
queue.remove()
print(queue)

# Comparison of both implementations
def compare_queue_ADT(queue_length, queue_list, improv_queue):
    """"Compares the performance of QueueList and ImprovedQueue for a priority_queue_linkedlist of length queue_length"""
    # Compare the performance when inserting items into the queues.
    # First QueueList
    start1 = time.process_time()
    for i in range(queue_length):
        queue_list.insert(i)
    end1 = time.process_time()

    # Secondly ImprovedQueue
    start2 = time.process_time()
    for i in range(queue_length):
        improv_queue.insert(i)
    end2 = time.process_time()

    print("QueueList insert total time taken: {0}, ImprovedQueue insert total time taken: {1}".format(end1 - start1,
                                                                                                      end2 - start2))
    # Conclusion: QueueList is much faster than ImprovedQueue

    # Compare the performance when removing items from the queues.
    # First QueueList
    start1 = time.process_time()
    for i in range(queue_length):
        queue_list.remove()
    end1 = time.process_time()

    # Secondly ImprovedQueue
    start2 = time.process_time()
    for i in range(queue_length):
        improv_queue.remove()
    end2 = time.process_time()

    print("QueueList remove total time taken: {0}, ImprovedQueue remove total time taken: {1}".format(end1 - start1,
                                                                                                      end2 - start2))
    # Conclusion: ImprovedQueue is much faster than QueueList

improv_queue = ImprovedQueue()
queue_list = QueueList()
compare_queue_ADT(200000, queue_list, improv_queue)

